"""
Created on 2018/3/28
@Author: Jeff Yang
"""

# namedtuple可以创建一个类对象
from collections import namedtuple


class User():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


user = User("Tom", 29, 175)
print(user.name, user.age, user.height)
print("=======")

# 相当于创建一个类：
User = namedtuple("User", ["name", "age", "height", "addr"])
user_tuple = ("Tom", 29, 175)
user = User(*user_tuple, "Beijing")  # 直接使用tuple初始化
print(user.name, user.age, user.height, user.addr)
print("=======")


# namedtuple占用内存比定义class小，代码量比较少

# 函数参数
def f(*args, **kwargs):
    pass


f("Tom", 29)  # *args以tuple形式接收参数
f(name="Tom", age=29)  # **kwargs以dict形式接收参数

# 也可以使用**初始化
User = namedtuple("User", ["name", "age", "height", "addr"])
user_dict = {
    "name": "Tom",
    "age": 29,
    "height": 175,
}
user = User(**user_dict, addr="Shanghai")  # 使用dict初始化
print(user.name, user.age, user.height, user.addr)
print("=======")

User = namedtuple("User", ["name", "age", "height", "addr"])
# _make()函数初始化不需要使用*号，只需传入可迭代对象，但是参数必须与定义的一致
user_tuple = ("Tom", 29, 175, "Guangzhou")
# user_list = ["Tom", 29, 175, "Guangzhou"]
# user_dict = {
#     "name": "Tom",
#     "age": 29,
#     "height": 175,
# }
user = User._make(user_tuple)  # _make()函数使用tuple初始化
# user = User._make(user_list)  # _make()函数使用list初始化
# user = User._make(user_dict)  # _make()函数使用dict初始化，dict也是可迭代对象
print(user.name, user.age, user.height, user.addr)
print("=======")

User = namedtuple("User", ["name", "age", "height", "addr"])
user_tuple = ("Tom", 29, 175, "Guangzhou")
# _asdict()可以将namedtuple转化为dict
user_info_dict = user._asdict()
# 也可以拆包
name, *others = user
print(user_info_dict)
print(name, others)  # Tom [29, 175, 'Guangzhou']
print("=======")
