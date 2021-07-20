# -*- coding: utf-8 -*-
# file: filter_ops.py
# date: 2021-07-20


from typing import Dict, List, Union, Any


def py_dict_val_filter(
        target: Dict, filtering_rule: Union[ Dict[Any, List], List[Any] ], 
        default_filter: List = ["null", "NULL", None, "", " "]) -> bool:
    """ Filtering python `Dict` records according rule parameters.
    Args:
        target: One python `Dict` record in spark RDD.

        filtering_rule: 
            If a `List` instance, then each record without the fields in 
            `filtering_rule` should be filtered.
            If a `Dict` instance, then each record without the fields in 
            it or each record which value in its corresponding `List` in 
            `filtering_rule` should be filtered.

        default_filter: 
            A list that if the value of any fields in `filtering_rule` hits 
            `default_filter`, that record should be filtered.
    Returns:
        If current python `Dict` record should be kept or filtered.
        NOTE: `True` for keep, `False` for filter.
    """
    if isinstance(filtering_rule, List):
        filtering_rule: Dict = dict( [(x, []) for x in filtering_rule] )

    for k, v in filtering_rule.items():
        if k not in target:
            return False
        elif (target[k] in v or target[k] in default_filter):
            return False
    return True
