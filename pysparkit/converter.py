# -*- coding: utf-8 -*-
# file: converter.py
# date: 2021-07-16


import pyspark.sql
from typing import Dict, List, Union
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import rand


def json_str2spark_row(json_str: str) -> pyspark.sql.Row:
    py_dict: Dict = json.loads(json_str) 
    output: pyspark.sql.Row = pyspark.sql.Row(**py_dict)
    return output
