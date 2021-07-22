# -*- coding: utf-8 -*-
# file: datetime.py
# date: 2020-07-21


from typing import Dict, List
from datetime import datetime


def get_now_date() -> datetime.date:
    return datetime.date(datetime.now())


def get_now_time() -> datetime.time:
    return datetime.time(datetime.now())


def get_now_date_str(date_format: str="%Y-%m-%d") -> str:
    return get_now_date().strftime(date_format)


def get_now_time_str(time_format: str="%hh:%mm:%ss") -> str:
    return get_now_time().strftime(date_format)
