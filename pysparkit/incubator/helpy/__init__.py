# -*- coding: utf-8 -*-
# file: __init__.py
# date: 2020-07-21


import os
import sys
sys.path.append(os.path.dirname(__file__) + os.sep + './')


try:
    from . import datetime
    from . import path 
    from . import iterator
    from . import types
except:
    from helpy import datetime
    from helpy import path
    from helpy import iterator
    from helpy import types


dt = datetime
datetime = datetime
path = path
iter = iterator
iterator = iterator
types = types
