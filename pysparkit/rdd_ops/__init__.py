# -*- coding: utf-8 -*-
# file: __init__.py
# date: 2020-08-09


import pyspark
from typing import Dict, List, Any, Union
from ..lambda_ops import reduce_ops
from ..lambda_ops import map_ops
from ..incubator import helpy as hpy



def py_dict_rdd_agg_fields_concat(
        py_dict_rdd: pyspark.RDD,
        aggregate_key: Any, 
        concating_fields: List[Any]
) -> pyspark.RDD:
    output_rdd: pyspark.RDD = py_dict_rdd\
            .map(lambda x: (x[aggregate_key], x))\
            .foldByKey(
                {}, 
                lambda a, b: reduce_ops.py_dict_reduce_concat(
                    a, b, concating_fields
                )
             )\
            .map(lambda x: map_ops.pair2dict(x, aggregate_key))
    return output_rdd


#TODO@202108091423
def py_dict_rdd_distinct_by_field(
        py_dict_rdd: pyspark.RDD, distincting_keys: List
) -> pyspark.RDD:
    return None


def py_dict_rdd_join_by_field(
        py_dict_rdd_0: pyspark.RDD, py_dict_rdd_1: pyspark.RDD, 
        target_field: Union[str, int, float], 
        join_type: str="join"
) -> pyspark.RDD:
    pair_rdd_0: pyspark.RDD = py_dict_rdd_0\
            .map(lambda x: (x[target_field], x))
    pair_rdd_1: pyspark.RDD = py_dict_rdd_1\
            .map(lambda x: (x[target_field], x))

    joint_pair_rdd: pyspark.RDD = eval(
            "pair_rdd_0.{join_type}(pair_rdd_1)".format(join_type=join_type))
    joint_py_dict_rdd: pyspark.RDD = joint_pair_rdd\
            .map(lambda x: hpy.iter.merge_dict(x[1][0], x[1][1], True))
    return joint_py_dict_rdd
