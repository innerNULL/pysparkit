# -*- coding: utf-8 -*-
# file: iterator.py
# date: 2020-07-23


from typing import Any, Union, List, Dict, Tuple


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
        list_insight: Dict[ Any, Union[ int, List, Dict[str, int] ] ]
) -> Dict[Any, float]:
    item_weight: Dict = {}

    if "dist" not in list_insight:
        return item_weight 
    if len(list_insight) == 0 or len(list_insight["dist"]) == 0:
        return item_weight

    norm: float = sum([x[1] for x in list_insight["dist"].items()]) 
    item_weight = dict(
            [(k, v / norm) for k, v in list_insight["dist"].items()]
    )
    return item_weight

