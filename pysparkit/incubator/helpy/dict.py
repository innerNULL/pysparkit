# -*- coding: utf-8 -*-
# file: dict.py


from typing import Dict, List, Union, Any
from . import types 


def flat_dict_type(
    target_dict: 
        Dict[ Union[str, int, float], Union[str, int, float, bool] ]
) -> Dict[ Union[str, int, float], str ]:
    dict_types: Dict[ Union[str, int, float], str ] = {}

    for k, v in target_dict.items():
        if k not in dict_types:
            k_type: str = types.obj2basic_type_str(v).split("#")[0]
    return dict_types

