from pyspark import SparkContext, SparkConf
import re
from random import getrandbits


def normalize_word(word):
    normalized = word.lower().strip()

    normalized = re.sub(r'\s*-\s*', '-', normalized)
    normalized = re.sub(r'(?<!\w)[-]|[-](?!\w)|[^\w\s-]', '', normalized)
    normalized = ' '.join(normalized.split())

    return normalized


def process_file(file):
    file_path, content = file
    offset = 0
    words = content.split()
    words_with_offsets = []

    for word in words:
        offset = content.find(word, offset)
        words_with_offsets.append((normalize_word(word), f"{file_path}@{offset}"))
        offset += len(word)

    return words_with_offsets

if __name__ == "__main__":
    conf = SparkConf().setAppName("InvertedIndex").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    input_path = "./input"
    output_path = "./output/output-%8x" % getrandbits(32)

    files_rdd = sc.wholeTextFiles(input_path)

    inverted_index = (files_rdd
        .flatMap(process_file)
        .groupByKey()
        .mapValues(list)
    )

    inverted_index.coalesce(1).saveAsTextFile(output_path)

    sc.stop()
