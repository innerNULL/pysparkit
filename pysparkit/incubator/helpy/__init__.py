# -*- coding: utf-8 -*-
# file: __init__.py
# date: 2020-07-21


try:
    from . import datetime
    from . import path
except:
    from helpy import datetime
    from helpu import path


dt = datetime
datetime = datetime
path = path
