# -*- coding: utf-8 -*-
# file: ops.py
# date: 2020-08-10


from typing import Union, Any, Dict, List


def list_meta(
        items: List[Union[str, int, float]]
) -> Dict:
    output: Dict = {
            "data": items, "vals": list(set(items)), 
            "dist": {}
    }
    for item in items:
        if item not in output["dist"]:
            output["dist"][item] = {"count": 0, "frequency": 0.0}
        output["dist"][item]["count"] += 1

    for k, v in output["dist"].items():
        output["dist"][k]["frequency"] = round(
                output["dist"][k]["count"] / len(output["data"]), 2)
    return output



def token_list_with_bin_cls_meta(
        token_list: List[Union[str, int, float]], 
        bin_cls_list: List[int]
) -> Dict[ str, Dict[Union[str, int, float], float] ]:
    output: Dict[ str, Dict[Union[str, int, float], float] ] = {
            "data": token_list, "bin_cls": bin_cls_list, 
            "vals": list(set(token_list)),
            "0_meta": {}, "1_meta": {}
    }
    item_0: List = []
    item_1: List = []
    for i, token in enumerate(token_list):
        bin_cls: str = str(bin_cls_list[i])
        if bin_cls == "0":
            item_0.append(token)
        elif bin_cls == "1":
            item_1.append(token)
    output["0_meta"] = list_meta(item_0)
    output["1_meta"] = list_meta(item_1)        
    return output
