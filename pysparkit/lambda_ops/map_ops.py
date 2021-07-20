# -*- coding: utf-8 -*-
# file: map_ops.py
# date: 2021-07-16


import pyspark
import pyspark.sql
from typing import Dict, List, Union




def json_str2spark_row(json_str: str) -> pyspark.sql.Row:
    py_dict: Dict = json.loads(json_str) 
    output: pyspark.sql.Row = pyspark.sql.Row(**py_dict)
    return output


def sparksql_row2py_dict(row: pyspark.sql.Row) -> Dict:
    return row.asDict()
