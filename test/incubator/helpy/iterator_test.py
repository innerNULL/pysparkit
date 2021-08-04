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
        target: Dict = {1: round(2/9, 2), 2: round(4/9, 2), 3: round(1/9, 2), 5: round(2/9, 2)}
        output: Dict = hpy.iter.list_insight2item_weight(list_insight_info)
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))
        print("passed Test4list_insight.test_list_insight2item_weight_case0") 



class Test4dict_merge_series(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"

    def test_merge_dict_case0(self):
        input_0: Dict = {}
        input_1: Dict = {}
        output: Dict = hpy.iter.merge_dict(input_0, input_1, False)
        target: Dict = {}
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))

        print("Test4dict_merge_series.merge_dict_case1")   

    def test_merge_dict_case1(self):
        input_0: Dict = {"a": 1, "b": [2], "d": [0, 1]}
        input_1: Dict = {"a": [2,3], "b": [1], "c": "c", "d": 2}
        output: Dict = hpy.iter.merge_dict(input_0, input_1, False)
        target: Dict = {"a": [1, 2, 3], "b": [2, 1], "c": "c", "d": [0, 1, 2]}

        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))

        output: Dict = hpy.iter.merge_dict(input_0, input_1, True)
        target: Dict = {"a": [2,3], "b": [1], "c": "c", "d": 2} 
        self.assertTrue(target == output,
                msg=self.msg_temp.format(target, output))

        print("Test4dict_merge_series.merge_dict_case1") 


class Test4dict_inplace_func(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"

    def test_dict_inplace_func_case0(self):
        input_dict: Dict = {"a": 1, "b": 2, "c": 3}
        func_0 = lambda x: x + 1
        func_1 = lambda x, y: y - x
        func_2 = lambda x: x

        func_args_0 = {"x": "a"}
        func_args_1 = {"x": "a", "y": "b"}
        func_args_2 = {"x": "c"}

        output_0 = hpy.iter.dict_inplace_func(input_dict, func_0, func_args_0, {}, "a")
        target_0 = {"a": 2, "b": 2, "c": 3}
        self.assertTrue(target_0 == output_0,
                msg=self.msg_temp.format(target_0, output_0))

        output_1 = hpy.iter.dict_inplace_func(input_dict, func_1, func_args_1, {}, "b")
        target_1 = {"a": 1, "b": 1, "c": 3}
        self.assertTrue(target_1 == output_1,
                msg=self.msg_temp.format(target_1, output_1))

        output_2 = hpy.iter.dict_inplace_func(input_dict, func_2, func_args_2, {}, "d")
        target_2 = {"a": 1, "b": 2, "c": 3, "d": 3}
        self.assertTrue(target_2 == output_2,
                msg=self.msg_temp.format(target_2, output_2))
       
        print("Test4dict_inplace_func.test_dict_inplace_func_case0") 





