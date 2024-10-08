# PySpark: word count and inverted index

## Description

This project aims to implement basic examples of word count and inverted index using PySpark.

To not mess up your local environment, I recommend using a Docker container with PySpark. To simplify this process, 
I created two Dockerfiles that you can use to build your own image and then run containers with Makefile provided 
along the Dockerfiles.

## Requirements
- docker
- docker compose
- Make

## Additional information

Both Dockerfiles use:
- Python 3.12.7
- Java 17
- Node.js 18
- PySpark 3.5.3
- Apache Spark 3.5.3
- Apache Hadoop 3.4.0

If you'd like to use a different version of any of the above, feel free to change the Dockerfiles.

**If needed, you can add more text files to the `data/input` directory.**
