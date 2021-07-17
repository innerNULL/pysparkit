# -*- coding: utf-8 -*-
# file: rdd_helper.py
# date: 2021-07-16


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import rand


def print_rdd(input_rdd: pyspark.RDD, limit: int) -> None:
    for row in input_rdd.take(limit):
        print(row)



