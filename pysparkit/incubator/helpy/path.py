# -*- coding: utf-8 -*-
# file: datetime.py
# date: 2020-07-21


import os
from typing import Dict, List
from datetime import datetime
from multipledispatch import dispatch

try:
    from .. import helpy as hpy
except:
    import helpy as hpy


@dispatch(str, str)
def extend_path_by_date(
        path: str="./", date: str=hpy.datetime.get_now_date_str()
) -> str:
    output: str = path
    for item in date.split("-"):
        output = os.path.join(output, item)
    return output

