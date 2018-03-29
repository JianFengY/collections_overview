"""
Created on 2018/3/28
@Author: Jeff Yang
"""

from collections import deque
# deque是线程安全的（由GIL保护），list不是线程安全的
import copy

user_list = ["Tom", "Jack", "Bob"]
user_name = user_list.pop()
print(user_name, user_list)
print("========")

user_deque = deque(("Tom", "Jack", "Bob"))  # 传入可迭代对象
user_deque = deque({
    "Jack": 20,
    "Bob": 20,
})  # 传入dict时会用key初始化
print(user_deque)  # deque(['Jack', 'Bob'])
print("========")

user_deque = deque(["Tom", "Jack", "Bob"])
user_deque.appendleft("John")  # 添加到左边
print(user_deque)
print("========")

user_deque = deque(["Tom", ["Jack"], "Bob"])
user_deque2 = user_deque.copy()  # 浅拷贝
user_deque3 = copy.deepcopy(user_deque)  # 深拷贝
print(id(user_deque), id(user_deque2))  # id不同
user_deque2[1].append("Mark")  # user_deque和user_deque2都会发生改变，user_deque3不变
print(user_deque, user_deque2, user_deque3)
print("========")

user_deque = deque(["Tom", "Jack", "Bob"])
user_deque2 = deque(("John", "Mark"))
# 合并deque，直接对user_deque修改，没有返回值，相应的还有extendleft()
user_deque.extend(user_deque2)
print(user_deque)
print("========")

user_deque = deque(["Tom", "Jack", "Bob"])
user_deque.insert(0, "John")  # 插入元素
user_deque.reverse()  # 反转deque，直接修改，没有返回值
print(user_deque)
print("========")
