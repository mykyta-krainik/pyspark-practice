from pyspark import SparkContext, SparkConf
import re
from random import getrandbits


def normalize_words(text):
    return re.findall(r'\b\w+\b', text.lower())


if __name__ == "__main__":
    config = SparkConf().setAppName("WordCount").setMaster("local[*]")
    sc = SparkContext(conf=config)

    input_path = "./input"
    output_path = "./output/output-%8x" % getrandbits(32)

    files_rdd = sc.wholeTextFiles(input_path)

    word_counts_rdd = (files_rdd
        .flatMap(
            lambda file: [((word, file[0]), 1) for word in normalize_words(file[1])]
        ).reduceByKey(
            lambda a, b: a + b
        ))

    word_counts_rdd.saveAsTextFile(output_path)

    sc.stop()
