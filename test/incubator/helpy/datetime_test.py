# -*- coding: utf-8 -*-
# file: datetime_test.py
# date: 2020-07-20


import sys
sys.path.append("./")    
sys.path.append("../")
sys.path.append("./pysparkit/incubator")

import unittest
from datetime import datetime
import helpy as hpy


class Test4get_now(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"
        pass

    def test_get_now(self):
        now = datetime.now()
        target_date = datetime.date(now)
        target_time = datetime.time(now)
        output_date = hpy.datetime.get_now_date()
        output_time = hpy.datetime.get_now_time()

        self.assertTrue(target_date == output_date, 
                msg=self.msg_temp.format(target_date, output_date))
        print("passed Test4get_now.test_get_now")

    def test_get_now_str(self):
        now = datetime.now()
        year: str = str(now.year)
        month: str = str(now.month) if now.month > 9 else "0" + str(now.month)
        day: str = str(now.day) if now.day > 9 else "0" + str(now.day)
        output_date: str = hpy.datetime.get_now_date_str()
        target_date: str = "%s-%s-%s" % (year, month, day)

        self.assertTrue(target_date == output_date, 
                msg=self.msg_temp.format(target_date, output_date))
        print("passed Test4get_now.test_get_now_str")


class Test4str2datetime(unittest.TestCase):
    @classmethod 
    def setUpClass(self):  
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"

    def test_case0(self):
        dt_str: str = "2010-09-01"
        target: datetime = datetime(2010, 9, 1, 0, 0, 0)
        output: datetime = hpy.dt.str2datetime(dt_str, "%Y-%m-%d")
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))
        print("passed Test4str2datetime.test_case0")


class Test4offset_datetime_str(unittest.TestCase):
    @classmethod 
    def setUpClass(self):  
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"

    def test_case0(self):
        dt: str = "2010-09-01"
        dt_format: str = "%Y-%m-%d"
        output: str = hpy.dt.offset_datetime_str(dt, dt_format, 
                0, 0, 0, 0, 0, 0, 0, 0, 0)
        target: str = "2010-09-01"
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))

        output: str = hpy.dt.offset_datetime_str(dt, dt_format,
                0, 0, 0, 0, 0, 4, 1, 2, 3)
        target: str = "2010-09-01"
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))

        output: str = hpy.dt.offset_datetime_str(dt, dt_format,
                -1, 0, 0, 0, 0, 4, 1, 2, 3)
        target: str = "2009-09-01"
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))
        print("passed Test4offset_datetime_str.test_case0")


def main() -> None:
    print("Run datetime_test.py")
    unittest.main()


if __name__ == "__main__":
    main()
