# -*- coding: utf-8 -*-
# file: map_ops.py
# date: 2021-07-16


import pyspark
import pyspark.sql
from typing import Dict, List, Union, Any, Tuple




def json_str2spark_row(json_str: str) -> pyspark.sql.Row:
    py_dict: Dict = json.loads(json_str) 
    output: pyspark.sql.Row = pyspark.sql.Row(**py_dict)
    return output


def sparksql_row2py_dict(row: pyspark.sql.Row) -> Dict:
    return row.asDict()


def pair2dict(pair_record: Tuple, pair_key_name: str="key") -> Dict:
    if len(pair_record) != 2:
        raise Exception(
            "`pair_record` should be a k-v style tuple with length 2.")
    
    if isinstance(pair_record[1], Dict):
        output = pair_record[1]
        output[pair_key_name] = pair_record[0]
    else:
        output = {}
        output["val"] = pair_record[1]
        output[pair_key_name] = pair_record[0]
    return output

