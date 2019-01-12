# 1
# import math
# def main():
#     radius = float(input("请输入球体的半径："))
#     diameter = 2 * radius
#     perimeter = math.pi * diameter
#     area = math.pi * radius ** 2
#     print("直径：%.2f\n周长：%.2f\n面积：%.2f\n" % (diameter, perimeter, area))
#
# if __name__ == '__main__':
#     main()


# 4
import functools


def gottfried_leibniz(n):
    pai = functools.reduce(lambda x, y: x + (-1) ** (y + 1) / (2 * y - 1), range(1, n + 1))
    print(4 * pai)


gottfried_leibniz(10000)


# 3
def marble(height, num):
    List = list(map(lambda x: height * 0.6 ** x, range(0, num)))
    sum = functools.reduce(lambda x, y: x + 2 * y, List)
    sum -= List[num - 1]
    print(sum)


marble(10, 3)
