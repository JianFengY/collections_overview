"""
Created on 2018/3/29
@Author: Jeff Yang
"""

from collections import OrderedDict

user_dict = OrderedDict()
# user_dict = dict()  # Python3中dict默认也是有序的，Python2中是无序的
user_dict["b"] = "Jack"
user_dict["a"] = "Bob"
user_dict["c"] = "Tom"
print(user_dict)
print("========")

user_dict = OrderedDict()
user_dict["b"] = "Jack"
user_dict["a"] = "Bob"
user_dict["c"] = "Tom"
print(user_dict.popitem())  # ('c', 'Tom')，把最后一个元素的key和value都pop出来
print(user_dict.pop("a"))  # Bob，pop出指定key的value
print(user_dict)
print("========")

user_dict = OrderedDict()
user_dict["b"] = "Jack"
user_dict["a"] = "Bob"
user_dict["c"] = "Tom"
user_dict.move_to_end("b")  # 把指定的元素移到最后
print(user_dict)
print("========")
