
from django.test import TestCase

# Create your tests here.

######################
# SLOTES IN PYTHON   #
######################

# class Coda:
#        __slots__ = ['phla_name', 'akhri_name']
#        def __init__(self, a , v):
#               self.phla_name = a 
#               self.akhri_name = v
#        def attrs(self):
#               return self.phla_name + " " + self.akhri_name
# x = Coda("name", "lname")
# print(x.phla_name)


"""------------------------------------------------------------------------------------------------------"""
######################
# PROPERTY IN PYTHON #
######################


# class A: 

#        def __init__(self, name):
#               self.__name = name
       
#        @property
#        def name(self):
#               return self.__name

#        @name.setter
#        def name(self, name):
#               self.__name=  name 

# a = A("ajay")
# a.name  = "boss"
# print(a.name)


"""------------------------------------------------------------------------------------------------------"""

######################
# ABC IN PYTHON      #
######################

# from abc import ABC, abstractmethod

# class SampleAbstractClass(ABC):

#        @abstractmethod
#        def do_something(self):
#               print("hello top of the world")

# class ChildAbstract(SampleAbstractClass):
       
#        def do_something(self):
#               super().do_something()
#               print("hello top of the world")

#        def not_do_anything(self):
#               print("ab to chalega")


# abc = ChildAbstract()
# # bcd = SampleAbstractClass()
# # print(bcd.do_something())
# print(abc.do_something())
# print(abc.not_do_anything())


##############################
#     RECURSION IN PYTHON    #
##############################

# def fibo_numbers(n):
#        if n == 0:
#               return 0 
#        elif n == 1: 
#               return 1 
#        else:
#               return fibo_numbers(n-1)+ fibo_numbers(n-2)
# print(fibo_numbers(50))
# def fib(n):
#     """ recursive version of the Fibonacci function """
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return  fib(n-1) + fib(n-2)

# print(fib(10))

# ---------------------------factorial of a number -----------------

def factorial(n):
    if n ==1:
        return 1
    else:
        print(n )
        return n * factorial(n-1)
print(factorial(5))


################################# PROBLEM SETS ##################################

# def romantoint(s):l
#     roman_to_integer = {
#             'I': 1,   
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
#     s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
#     return sum(map(lambda x: roman_to_integer[x], s))
# print(romantoint('XII'))


# class Solution:
#     def firstMissingPositive(self, nums) -> int:
        # list_min = nums[0]
        # list_max = nums[-1]
        # if list_min>1:
        #     return 1
        # try:
        #     import  pdb;pdb.set_trace()
        #     for i, j in enumerate(nums):
        #         if j + 1 == nums[i+1]:
        #             pass
        #         else:
        #             return j+1
        # except Exception as e:
        #     return list_max+1
                
# a = Solution()
# ###############-----testcases---------#########
# ab = [7,8,9,11,12]
# ab = [1,2,3,4,]
# ab = [-1, -2, 1,3]
# ab = [0,2,2,1,1]
# print(a.firstMissingPositive(ab))

import unittest
from fibonacci import fib
# class FibonacciTest(unittest.TestCase):
#     def testCalculation(self):
#         self.assertEqual(fib(0), 0)
#         self.assertEqual(fib(1), 1)
#         self.assertEqual(fib(5), 5) 
#         self.assertEqual(fib(10), 55)
#         self.assertEqual(fib(20), 6765)


# a = FibonacciTest()
# # a.testCalculation()

# unittest.main()

# # if name == "main": 
# #     unittest.main()

def hello(s):
    return s+"world1"

# import unittest

print(pytest)
# class HelloWorldTest(unittest.TestCase):
#     def testCalculation(self):
#         self.assertGreater(hello("hello"), "hellowor111hfjwbubeld1", msg=None)

# unittest.main() 

