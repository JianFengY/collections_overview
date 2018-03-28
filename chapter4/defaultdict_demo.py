"""
Created on 2018/3/28
@Author: Jeff Yang
"""
from collections import defaultdict

user_dict = {}
users = ['Tom', 'Tom', 'Jack', 'Tom', 'Bob', 'Jack']
for user in users:
    if user not in user_dict:
        user_dict[user] = 1
    else:
        user_dict[user] += 1
print(user_dict)
print("========")

user_dict = {}
users = ['Tom', 'Tom', 'Jack', 'Tom', 'Bob', 'Jack']
for user in users:
    user_dict.setdefault(user, 0)  # 设置默认值
    user_dict[user] += 1
print(user_dict)
print("========")

# 传递一个可调用对象，key不存在时调用传入的对象，如list、int等
default_dict = defaultdict(int)
users = ['Tom', 'Tom', 'Jack', 'Tom', 'Bob', 'Jack']
for user in users:
    default_dict[user] += 1
print(default_dict)
print("========")


def gen_default():
    return {
        "name": "",
        "nums": 0,
    }


default_dict = defaultdict(gen_default)  # 函数也是可调用对象
default_dict["group1"]
print(default_dict)
print("========")
