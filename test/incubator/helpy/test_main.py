# -*- coding: utf-8 -*-
# file: reduce_ops_test.py
# date: 2020-07-20


import unittest
import datetime_test 
import path_test
import iterator_test


Test4get_now = datetime_test.Test4get_now
Test4str2datetime = datetime_test.Test4str2datetime
Test4offset_datetime_str = datetime_test.Test4offset_datetime_str

Test4extend_path_by_date = path_test.Test4extend_path_by_date

Test4list_insight = iterator_test.Test4list_insight
Test4dict_merge_series = iterator_test.Test4dict_merge_series
Test4dict_inplace_func = iterator_test.Test4dict_inplace_func




if __name__ == "__main__":
    unittest.main()
