# -*- coding: utf-8 -*-
# file: wrapper.py
# date: 2021-07-15


import pyspark.RDD
import pyspark.sql.types
import pyspark.sql
import pyspark.sql.DataFrame
from typing import Dict, List, Union
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark import SparkFiles
from pyspark import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import rand


def append_files(spark_session: pyspark.sql.SparkSession, 
        depend_file_paths: str=None) -> None:
    if depend_file_paths is not None:
        for dep_file in depend_file_paths:
            spark_session.sparkContext.addFile(depend_file)


def linux_pipe_with_echo(spark_session: pyspark.sql.SparkSession, 
        exec_cmd_rdd: pyspark.RDD, 
        exec_cmd: str, 
        depend_file_paths: str=None) -> pyspark.RDD:
    append_files(depend_file_paths)
    shell_cmd: str = """echo '%s' | """ + exec_cmd 
    linux_echo_pipe_cmd: str = exec_cmd_rdd.map(lambda row: shell_cmd % row)
    output_rdd: pyspark.RDD = linux_echo_pipe_cmd.map(
        lambda x: os.popen(x.encode("utf-8")).read().replace("\n", "")
    )
    return output_rdd



