# -*- coding: utf-8 -*-
# file: __init__.py
# date: 2020-08-09


import pyspark
from typing import Dict, List, Any, Union
from ..lambda_ops import reduce_ops
from ..lambda_ops import map_ops



def py_dict_rdd_agg_fields_concat(
        py_dict_rdd: pyspark.RDD,
        aggregate_key: Any, 
        concating_fields: List[Any]
) -> pyspark.RDD:
    output_rdd: pyspark.RDD = py_dict_rdd\
            .map(lambda x: (x[aggregate_key], x))\
            .foldByKey(
                {}, 
                lambda a, b: reduce_ops.py_dict_reduce_concat(a, b, concating_fields)
             )\
            .map(lambda x: map_ops.pair2dict(x, aggregate_key))
    return output_rdd
