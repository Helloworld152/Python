"""解压可迭代对象赋值给多个对象"""
from audioop import avg


def drop_first_last(grades):
    """去掉两端求平均值"""
    first, *middle, last = grades
    return avg(middle)

