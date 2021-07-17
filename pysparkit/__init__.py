# -*- coding: utf-8 -*-
# file: __init__.py
# date: 2021-07-16


import os
import pyspark.sql 
from typing import Dict


def get_common_spark_session(
        job_name: str, spec_conf: Dict = {
            "hive.metastore.client.socket.timeout": 360, 
            "spark.ui.showConsoleProgress": "true", 
        }) -> pyspark.sql.SparkSession:
    spark_conf = pyspark.sql.SparkSession.builder.appName(job_name)
    for k, v in spec_conf.items():
        spark_conf.config(k, v)
    spark_session: pyspark.sql.SparkSession = spark_conf\
            .enableHiveSupport()\
            .getOrCreate()
    return spark_session


def python_version_config(version: str="python3") -> None:
    if "python3" in version:
        os.environ["PYSPARK_PYTHON"]="/usr/bin/python3"
        os.environ["PYSPARK_DRIVER_PYTHON"]="/usr/bin/python3"


