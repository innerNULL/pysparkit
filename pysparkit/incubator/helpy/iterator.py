# -*- coding: utf-8 -*-
# file: iterator.py
# date: 2020-07-23


import types
from typing import Any, Union, List, Dict, Tuple
from multipledispatch import dispatch


def list_insight(
        input_list: List[Union[int, float, str, bool]], 
        cal_range: str=":" 
) -> Dict[ Any, Union[ int, List, Dict[str, int] ] ]:
    insight_info: Dict[ Any, Union[ int, List, Dict[str, int] ] ]
    insight_info = {"num": 0, "type_num": 0, "val": [], "dist": {}}

    target_list: List = eval("input_list[%s]" % cal_range)

    for item in target_list:
        insight_info["num"] += 1
        if item not in insight_info["dist"]:
            insight_info["type_num"] += 1
            insight_info["val"].append(item)
            insight_info["dist"][item] = 0
        insight_info["dist"][item] += 1
    
    return insight_info


def list_insight2item_weight(
        list_insight: Dict[ Any, Union[ int, List, Dict[str, int] ] ], 
        decimal: int=2
) -> Dict[Any, float]:
    item_weight: Dict = {}

    if "dist" not in list_insight:
        return item_weight 
    if len(list_insight) == 0 or len(list_insight["dist"]) == 0:
        return item_weight

    norm: float = sum([x[1] for x in list_insight["dist"].items()]) 
    item_weight = dict(
            [(k, round(v / norm, decimal)) for k, v in list_insight["dist"].items()]
    )
    return item_weight


@dispatch(dict, dict, bool)
def merge_dict(target_0: Dict, target_1: Dict, 
        if_overwrite: bool=True
) -> Dict:
    for k, v in target_1.items():
        if k not in target_0 or if_overwrite:
            target_0[k] = v
        else:
            if type(v) is type(target_0[k]):
                if isinstance(v, List):
                    target_0[k].extend(v)
                elif isinstance( v, (str, int, float) ): 
                    target_0[k] = [target_0[k], v]
                else:
                    # TODO
                    target_0[k] = v
            else:
            # TODO@202107261350: Consider Dict case
                if isinstance(v, List) and \
                        isinstance( target_0[k], (str, int, float) ):
                    target_0[k] = [target_0[k]]
                    target_0[k].extend(v)
                elif isinstance(target_0[k], List) and \
                        isinstance( v, (str, int, float) ): 
                    target_0[k].append(v)
                else:
                    target_0[k] = v
    return target_0


def dict_inplace_func(original_dict: Dict, 
        func: types.FunctionType, 
        self_contained_args: Dict[str, Any]={}, 
        extra_args: Dict[str, Any]={}, 
        out_field: str=None 
) -> Dict:
    """ `Dict` instance inplace style function executor.
    The function `func` will be executed with arguments 
    in `func_args` which value could be found in `original_dict`, 
    and the result will be contained in the output `Dict` 
    instance's `out_field`, and output `Dict` instance will 
    also contained all other fields in `original_dict`.
    """
    output_dict: Dict = dict(original_dict.items())

    if out_field is None:
        out_field = "dict_inplace_func_output_for_%s" % func.__name__
    
    func_args: Dict[str, Any] = {}
    for arg_name, field in self_contained_args.items():
        func_args[arg_name] = original_dict[field]
    for arg_name, arg_val in extra_args.items():
        func_args[arg_name] = arg_val
    
    func_out: Any = func(**func_args)
    output_dict[out_field] = func_out

    return output_dict


def dict_query(original_dict: Dict, 
        target_fields: List[Any]=[], 
        kept_or_filter: str="kept"
) -> Dict:
    output: Dict = {}
    keeping_fields: List = []

    if kept_or_filter == "kept":
        keeping_fields = [x for x in target_fields if x in original_dict]
    else:
        keeping_fields = [
            k for k, v in original_dict.items() if k not in target_fields
        ]

    for field in keeping_fields:
        output[field] = original_dict[field] 
    return output
