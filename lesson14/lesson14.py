#тестирование кода, оператор assert
# assert sum([1,2,3]) == 6, "should be 6"
# модуль unitest
# import unittest
#
#
# class TestSum(unittest.TestCase):
#
#     def test_sum(self):
#         self.assertEqual(sum([1,2,3]), 6, "Should be 6")
#
#     def test_sum_tuple(self):
#         self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
#
# if __name__ == '__main__':
#     unittest.main()
#
import unittest

# def test_sum(array:list):
#     total = 0
#     assert isinstance(array,tuple) or isinstance(array,list)
#     for val in array:
#         assert isinstance(val,int) or isinstance(val,str)
#         total += val
#     return total

# if __name__ =='__main__':
#     sum(3)
#     sum([3,3])
#     sum('3333')
#     sum(['3','3'])
import unittest

class TestSum(unittest.TestCase):

def test_sum(array:list):
    total = 0
    for val in array:
        total += val
    return total

def test_sum(self):
    self.assertEqual(array,list) or (array,tuple)

def test_sum(self):
    self.assertEqual(val,int) or (val,str)

if __name__ =='__main__':
    sum(3)
    sum([3,3])
    sum('3333')
    sum(['3','3'])
    unittest.main()
