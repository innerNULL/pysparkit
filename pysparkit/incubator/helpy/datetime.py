# -*- coding: utf-8 -*-
# file: datetime.py
# date: 2020-07-21


from typing import Dict, List
from datetime import datetime, timedelta
from multipledispatch import dispatch


def str2datetime(dt_str: str, 
        dt_format: str="%Y-%m-%d"
) -> datetime:
    return datetime.strptime(dt_str, dt_format)


def datetime2str(dt: datetime, dt_format: str="%Y-%m-%d") -> str:
    return dt.strftime(dt_format)


def get_now_date() -> datetime.date:
    return datetime.date(datetime.now())


def get_now_time() -> datetime.time:
    return datetime.time(datetime.now())


def get_now_date_str(date_format: str="%Y-%m-%d") -> str:
    return get_now_date().strftime(date_format)


def get_now_time_str(time_format: str="%hh:%mm:%ss") -> str:
    return get_now_time().strftime(date_format)


@dispatch(datetime, int, int, int, int, int, int, int, int, int)
def offset_datetime(dt: datetime, 
        years: int=0, months: int=0, weeks: int=0, 
        days: int=0, hours: int=0, minutes: int=0, 
        seconds: int=0, microseconds: int=0, 
        milliseconds: int=0
) -> datetime:
    """
    NOTE: 
        `timedelta` only support days, seconds, microseconds, 
        milliseconds, minutes, hours, weeks, so for years we 
        will handle by ourself, seperately.
    """
    output_dt: datetime = dt
    time_delta: timedelta = timedelta(
            days=days, seconds=seconds, 
            microseconds=microseconds, milliseconds=milliseconds,  
            minutes=minutes, hours=hours, weeks=weeks)
    output_dt += time_delta
   
    output_dt = output_dt.replace(year=(output_dt.year + years))
    output_dt = output_dt.replace(month=(output_dt.month + months))
    return output_dt


# TODO
@dispatch(str, int, int, int, int, int, int, int, int, int)
def offset_datetime(dt: str, 
        years: int=0, months: int=0, weeks: int=0, 
        days: int=0, hours: int=0, minutes: int=0, 
        seconds: int=0, microseconds: int=0, 
        milliseconds: int=0
) -> datetime:
    return None


def offset_datetime_str(dt_str: str, dt_format: str,  
        years: int=0, months: int=0, weeks: int=0, 
        days: int=0, hours: int=0, minutes: int=0, 
        seconds: int=0, microseconds: int=0, 
        milliseconds: int=0
) -> str:
    dt: datetime = str2datetime(dt_str, dt_format)
    offset_dt: datetime = offset_datetime(dt, 
            years, months, weeks, days, hours, minutes, 
            seconds, microseconds, milliseconds)
    return datetime2str(offset_dt, dt_format)

