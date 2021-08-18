# -*- coding: utf-8 -*-
# file: reduce_ops.py
# date: 2020-07-20


import types
from typing import Any, Union, Dict, List
try:
    from ..incubator import helpy as hpy
except:
    import helpy as hpy




# TODO
def py_dict_reduce_base(record: Dict, record_next: Dict, 
        target_fields: List[ Union[int, float, str] ]) -> Dict:
    reduce_base: Dict[Any, Dict] = {}
    output: Dict[Any, Dict] = dict( [(k, []) for k in target_fields] )


def py_dict_reduce_concat(record: Dict, record_next: Union[Dict, None], 
        target_fields: List[ Union[int, float, str] ]
    ) -> Dict[Any, List]:
    output: Dict[Any, List] = dict( [(k, []) for k in target_fields] )

    for target_field in target_fields:
        if target_field in record:
            if isinstance(record[target_field], List):
                output[target_field].extend(record[target_field])
            else:
                output[target_field].append(record[target_field])

        if record_next is not None:
            if target_field in record_next:
                if isinstance(record_next[target_field], List):
                    output[target_field].extend(record_next[target_field])
                else:
                    output[target_field].append(record_next[target_field])
    return output


def py_dict_reduce_max_min(record: Dict, record_next: Dict, 
        #value_preprocessor: Dict[ Union[str, float, int], types.FunctionType] = {}, 
        target_fields: List[ Union[int, float, str] ] = None
) -> Dict[ Union[int, float, str], Dict[str, Union[int, float]] ]:
    output: Dict[ Union[int, float, str], Dict[str, Union[int, float]] ] = {} 
    for k, v in record_next.items():
        if target_fields is not None:
            if k not in target_fields:
                continue
        if hpy.types.obj2basic_type_str(v).split("#")[0] != "numeric":
            continue
        if "pysparkit_flag" in record:
            record[k]["max"] = max(v, record[k]["max"])
            record[k]["min"] = min(v, record[k]["min"])
            output = record
        else:
            output["pysparkit_flag"] = "py_dict_reduce_max_min"
            output[k] = {}
            output[k]["max"] = max(v, record.get(k, v))
            output[k]["min"] = min(v, record.get(k, v))
    return output
