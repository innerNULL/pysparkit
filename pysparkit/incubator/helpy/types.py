# -*- coding: utf-8 -*-
# file: types.py


from typing import Dict, List, Union, Any


def obj2basic_type_str(
    obj: Union[str, int, float, bool]
) -> str:
    type_str: str = ""
    if isinstance(obj, str):
        type_str = "str"
    elif isinstance(obj, bool):
        type_str = "bool"
    elif isinstance(obj, int):
        type_str = "numeric#int"
    elif isinstance(obj, float):
        type_str = "numeric#float"  
    return type_str
