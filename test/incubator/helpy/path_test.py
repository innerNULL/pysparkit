# -*- coding: utf-8 -*-
# file: path_test.py
# date: 2020-07-20


import sys
sys.path.append("./")    
sys.path.append("../")
sys.path.append("./pysparkit/incubator")

import unittest
from datetime import datetime
import helpy as hpy


class Test4extend_path_by_date(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"
        pass

    def test_case0(self):
        date: str = "2010-09-01"
        path: str = "./"
        target: str = "./2010/09/01"
        output: str = hpy.path.extend_path_by_date(path, date)
        self.assertTrue(target == output, msg=self.msg_temp.format(target, output))
        print("passed Test4extend_path_by_date.test_case0")


def main() -> None:
    print("Run %s" % __file__)
    unittest.main()


if __name__ == "__main__":
    main()
