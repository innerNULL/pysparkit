# -*- coding: utf-8 -*-
# file: reduce_ops_test.py
# date: 2020-07-20


import sys
sys.path.append("./")    
sys.path.append("../")
sys.path.append("./pysparkit/lambda_ops")

import unittest
#from pysparkit.lamba_ops import reduce_ops
import reduce_ops




class Test4py_dict_reduce_concat(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.msg_temp = "\n\tTarget: {0} \n\tOutput: {1}"
        pass

    def test_case0(self):
        record = {"a": 1, "b": "b", "c": "ccc", "d": 4}
        record_next = {"a": 2, "b": "bb", "d": 5}
        record_next_next = {"a": 3, "b": "bbb", "e": 8}
        target_fields = ["a", "b", "c"]

        target = {"a": [1, 2], "b": ["b", "bb"], "c": ["ccc"]}
        output = reduce_ops.py_dict_reduce_concat(record, record_next, target_fields)
        self.assertTrue(target == output, msg=self.msg_temp.format(target, output))

        target = {"a": [1, 2, 3], "b": ["b", "bb", "bbb"], "c": ["ccc"]}
        output = reduce_ops.py_dict_reduce_concat(output, record_next_next, target_fields)
        self.assertTrue(target == output, msg=self.msg_temp.format(target, output))

    def test_case1(self):
        record = {}
        record_next = {}
        target_fields = ["a", "b", "c"]

        target = {"a": [], "b": [], "c": []}
        output = reduce_ops.py_dict_reduce_concat(record, record_next, target_fields)
        self.assertTrue(target == output, msg=self.msg_temp.format(target, output))

        output = reduce_ops.py_dict_reduce_concat(record, None, target_fields)
        self.assertTrue(target == output, msg=self.msg_temp.format(target, output))

    def test_case2(self):
        record = {}
        record_next = {"a": 2, "b": "bb", "d": 5}
        target_fields = ["a", "b", "c"]

        target = {"a": [2], "b": ["bb"], "c": []}
        output = reduce_ops.py_dict_reduce_concat(record, record_next, target_fields)
        self.assertTrue(target == output, msg=self.msg_temp.format(target, output))


if __name__ == "__main__":
    unittest.main()
