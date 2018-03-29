"""
Created on 2018/3/29
@Author: Jeff Yang
"""

from collections import ChainMap

user_dict1 = {
    "a": "Tom",
    "b": "Bob",
}
user_dict2 = {
    "c": "John",
    "d": "Jack",
}
new_dict = ChainMap(user_dict1, user_dict2)  # 合并两个dict
print(new_dict)
for k, v in new_dict.items():
    print(k, "---", v)
print("========")

user_dict1 = {
    "a": "Tom",
    "b": "Bob",
}
user_dict2 = {
    "b": "John",
    "d": "Jack",
}
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict)
# 有相同的key时，只打印第一个
for k, v in new_dict.items():
    print(k, "---", v)
print("========")

user_dict1 = {
    "a": "Tom",
    "b": "Bob",
}
user_dict2 = {
    "c": "John",
    "d": "Jack",
}
new_dict = ChainMap(user_dict1, user_dict2)
brand_new_dict = new_dict.new_child({"aa": "aaa", "bb": "bbb"})  # 添加新元素
print(brand_new_dict)
for k, v in brand_new_dict.items():
    print(k, "---", v)
print("========")

user_dict1 = {
    "a": "Tom",
    "b": "Bob",
}
user_dict2 = {
    "c": "John",
    "d": "Jack",
}
new_dict = ChainMap(user_dict1, user_dict2)
print(new_dict.maps)  # 以列表形式展示
new_dict.maps[0]["a"] = "Mark"
print(new_dict)
print("========")
