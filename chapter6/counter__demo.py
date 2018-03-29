"""
Created on 2018/3/29
@Author: Jeff Yang
"""
from collections import Counter

users = ['Tom', 'Tom', 'Jack', 'Tom', 'Bob', 'Jack']
user_counter = Counter(users)  # 统计，传入可迭代对象，如list、dict等
print(user_counter)
print("========")

string_counter = Counter("hhellooo")  # 传入字符串
string_counter.update("wwworrrlld")  # 合并再统计，传入可迭代对象
print(string_counter)
print("========")

string_counter = Counter("hhellooo")  # 传入字符串
string_counter2 = Counter("wwworrrlld")
string_counter.update(string_counter2)  # 可以传入另一个Counter，因为Counter继承了dict
# top n问题，使用了数据结构--堆
top_2 = user_counter.most_common(2)  # 统计出现次数最多的前两个元素
print(top_2)
print(string_counter)
print("========")
