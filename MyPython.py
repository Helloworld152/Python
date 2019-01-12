
"""
迭代器
"""
# import sys
#
# list = [1,2,3,4]
# it = iter(list)   #创建迭代器对象
#
# # for x in it:
# #     print(x, end=" ")
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

##############################################
"""
裴波拉切数列生成器
"""
# import sys
#
#
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if counter > n:
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

###############################################
"""
传不可变对象实例
"""
#
# def changeint(a):
#     a = 10
#     return
#
# b = 2
# changeint(b)
# print(b)
#
###############################################
"""
传不可变对象实例
"""


# def ChangeMe(mylist):
#     mylist.append([1,2,3,4])
#     print("函数内取值：", mylist)
#     return
#
# mylist = [10, 20, 30, 40]
# ChangeMe(mylist)
# print("函数外取值：", mylist)

###############################################
"""
关键字参数
"""

# def printme(str):
#     print(str)
#     return
#
# printme(str = "hello")   #顺序可不一致
#
#
# def printinfo(name, age):
#     print(name)
#     print(age)
#     return
#
# printinfo(age = 50, name = "hello")

###############################################
"""
默认参数
"""

# def printinfo(name = "tech", age = 35):
#     print(name)
#     print(age)
#     return
#
# printinfo(name = "hello")
# printinfo()

#############################################
"""
不定长参数
"""

# def printinfo(arg1, *vartuple):
#     print(arg1)
#     print(vartuple)
#
# printinfo(70, 60, 50)


# def printinfo(arg1, *vartuple):
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
# printinfo(10)
# printinfo(70, 60, 50)

# def printinfo(arg1, **vardict):
#     print(arg1)
#     print(vardict)
#
# printinfo(1,a = 2, b = 3)

#1
#{'a': 2, 'b': 3}

############################################
"""
匿名函数lambda
"""

# sum = lambda arg1, arg2: arg1 + arg2
#
# print(sum(10, 20))
# print(sum(20, 20))

############################################
""""""



