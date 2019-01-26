"""此程序需要安装numpy库"""
import numpy as np
import math as M

# 创建医疗包类
class Bag:

    def __init__(self, i, l, w, h, we):
        self.id = i
        self.length = l
        self.width = w
        self.height = h
        self.weight = we
        self.volume = self.length * self.width * self.height

# 创建货舱类
class Box:

    def __init__(self, i, l, w, h, we=0):
        self.id = i
        self.length = l
        self.width = w
        self.height = h
        self.weight = we
        self.volume = self.length * self.width * self.height

# 创建模型
class Model:

    def __init__(self):

        self.bags = []
        self.bags.append(Bag(1, 14, 7, 5, 2))
        self.bags.append(Bag(2, 5, 8, 5, 2))
        self.bags.append(Bag(3, 12, 7, 4, 3))

        self.box = Box(2, 24, 20, 20)

    # 计算V(i),此函数不完整，需完善
    def computeV_i_(self, i):

        Tuple = [0.0, 0.0, 0.0]
        if i == 0:
            Tuple = [self.box.length,
                     self.box.width,
                     self.box.height]
        return Tuple

    # 计算第i步第j种医疗包的判别矩阵
    def createMatrice(self, i, j):

        A = self.computeV_i_(i-1)[0]
        B = self.computeV_i_(i-1)[1]
        C = self.computeV_i_(i-1)[2]

        a = self.bags[j-1]
        b = self.bags[j-1]
        c = self.bags[j-1]

        matrice = np.mat(np.array([[M.modf(A/a), M.modf(A/b), M.modf(A/c)],
                                   [M.modf(B/a), M.modf(B/b), M.modf(B/c)],
                                   [M.modf(C/a), M.modf(C/b), M.modf(C/c)]]))

        return matrice

    # 第i步选择医疗包
    def chooseBag(self, i):

        matriceList = []
        for j in range(0, 3):
            matriceList.append(self.createMatrice(i, j))

        min_column = 0
        min_row = 0

        for matrix in matriceList:
