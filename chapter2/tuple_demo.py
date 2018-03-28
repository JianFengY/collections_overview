"""
Created on 2018/3/28
@Author: Jeff Yang
"""

# tuple是不可变对象，也是Iterable对象（可迭代对象）
# 可以for循环的，都是Iterable
# 可以next()的，都是Iterator
names = ('Bob', 'Jack')
# names['0'] = 'Tom'  # 会报错
for name in names:
    print(name)
print('========')
# 拆包
user_tuple = ("Tom", 29, 175)
# name = user_tuple[0]
# age = user_tuple[1]
# height = user_tuple[2]
name, age, height = user_tuple
print(name, age, height)
print('========')

user_tuple = ("Tom", 29, 175, "Beijing")
name, *others = user_tuple  # 其他值放到列表others中
print(name, others)
print('========')

# tuple的不可变不是绝对的
user_tuple = ("Tom", [29, 175])
user_tuple[1].append("Beijing")
# 因为user_tuple[1]虽然元素改变了，但是id()并没变
# 不建议将可变类型存入tuple
print(user_tuple)  # ('Tom', [29, 175, 'Beijing'])
print('========')

# 拿C语言对比，tuple相当于struct，list相当于array
# tuple相比list的优点（immutable（不可变）的重要性）：
# 性能优化：指出全部为immutable的tuple会作为常量在编译时确定，提升速度
# 线程安全
# 可以作为dict的key（只有可哈希的对象才能作为dict的key）
# 拆包特性

user_tuple = (29, 175, "Beijing")
user_info_dict = {}
user_info_dict[user_tuple] = "Tom"
# user_info_dict[list(user_tuple)] = "Tom"  # TypeError: unhashable type: 'list'
print(user_info_dict)  # {(29, 175, 'Beijing'): 'Tom'}
