# -*- coding: utf-8 -*-
# file: iterator_test.py
# date: 2020-07-20


import sys
sys.path.append("./")    
sys.path.append("../")
sys.path.append("./pysparkit/incubator")

import unittest
from datetime import datetime
import helpy as hpy


class Test4list_insight(unittest.TestCase):
    @classmethod 
    def setUpClass(self):  
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"

    def test_list_insight_case0(self):
        input_list: List = [1,2,3,2,2,5,1,2,5]
        target: Dict = {
                "num": len(input_list), "type_num": len(set(input_list)), 
                "val": list(set(input_list)), 
                "dist": {1: 2, 2: 4, 3: 1, 5: 2}
        }
        output: Dict = hpy.iter.list_insight(input_list)
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))


        target: Dict = {
                "num": 7, "type_num": len(set(input_list)), 
                "val": list(set(input_list)), 
                "dist": {1: 2, 2: 3, 3: 1, 5: 1}
        }
        output: Dict = hpy.iter.list_insight(input_list, "0:7")
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))
        print("passed Test4list_insight.test_list_insight_case0")

    def test_list_insight2item_weight_case0(self):
        input_list: List = [1,2,3,2,2,5,1,2,5]
        list_insight_info: Dict = hpy.iter.list_insight(input_list)
        target: Dict = {1: 2/9, 2: 4/9, 3: 1/9, 5: 2/9}
        output: Dict = hpy.iter.list_insight2item_weight(list_insight_info)
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))
        print("passed Test4list_insight.test_list_insight2item_weight_case0") 


