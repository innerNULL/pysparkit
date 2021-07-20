# -*- coding: utf-8 -*-
# file: reduce_ops.py
# date: 2020-07-20


from typing import Any, Union, Dict, List


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



