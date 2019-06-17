#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Time    : 2019-06-16 16:33
@Author  : red
@Site    : 
@File    : insertData.py
@Software: PyCharm
"""
import matplotlib.pyplot as plt

"""
@brief:   计算n阶差商 f[x0, x1, x2 ... xn]
@param:   xi   所有插值节点的横坐标集合                                                        o
@param:   fi   所有插值节点的纵坐标集合                                                      /   \
@return:  返回xi的i阶差商(i为xi长度减1)                                                     o     o
@notice:  a. 必须确保xi与fi长度相等                                                        / \   / \
          b. 由于用到了递归，所以留意不要爆栈了.                                           o   o o   o
          c. 递归减递归(每层递归包含两个递归函数), 每层递归次数呈二次幂增长，总次数是一个满二叉树的所有节点数量(所以极易栈溢出)
"""


def get_order_diff_quot(xi=[], fi=[]):
    if len(xi) > 2 and len(fi) > 2:
        return (get_order_diff_quot(xi[:len(xi) - 1], fi[:len(fi) - 1]) - get_order_diff_quot(xi[1:len(xi)],
                                                                                              fi[1:len(fi)])) / float(
            xi[0] - xi[-1])
    return (fi[0] - fi[1]) / float(xi[0] - xi[1])


"""
@brief:  获得Wi(x)函数;
         Wi的含义举例 W1 = (x - x0); W2 = (x - x0)(x - x1); W3 = (x - x0)(x - x1)(x - x2)
@param:  i  i阶(i次多项式)
@param:  xi  所有插值节点的横坐标集合
@return: 返回Wi(x)函数
"""


def get_Wi(i=0, xi=[]):
    def Wi(x):
        result = 1.0
        for each in range(i):
            result *= (x - xi[each])
        return result

    return Wi


"""
@brief: 获得牛顿插值函数
@
"""


def get_Newton_inter(xi=[], fi=[]):
    def Newton_inter(x):
        result = fi[0]
        for i in range(2, len(xi)):
            result += (get_order_diff_quot(xi[:i], fi[:i]) * get_Wi(i - 1, xi)(x))
        return result

    return Newton_inter


def calF(data):
    # 差商计算  n个数据 0-(n-1)阶个差商 n个数据
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    F = [1 for i in range(len(data))]
    FM = []
    for i in range(len(data)):
        FME = []
        if i == 0:
            FME = data_y
        else:
            for j in range(len(FM[len(FM) - 1]) - 1):
                delta = data_x[i + j] - data_x[j]
                value = 1.0 * (FM[len(FM) - 1][j + 1] - FM[len(FM) - 1][j]) / delta
                FME.append(value)
        FM.append(FME)
    F = [fme[0] for fme in FM]
    print(FM)
    return F


def NT(data, testdata, F):
    # 差商之类的计算
    predict = 0
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    if testdata in data_x:
        return data_y[data_x.index(testdata)]
    else:
        for i in range(len(data_x)):
            Eq = 1
            if i != 0:
                for j in range(i):
                    Eq = Eq * (testdata - data_x[j])
            predict += (F[i] * Eq)
        return predict


def plot(data, nums):
    data_x = [data[i][0] for i in range(len(data))]
    data_y = [data[i][1] for i in range(len(data))]
    Area = [min(data_x), max(data_x)]
    X = [Area[0] + 1.0 * i * (Area[1] - Area[0]) / nums for i in range(nums)]
    X[len(X) - 1] = Area[1]
    F = calF(data)
    Y = [NT(data, x, F) for x in X]
    plt.plot(X, Y, label='result')
    for i in range(len(data_x)):
        plt.plot(data_x[i], data_y[i], 'ro', label="point")
    # plt.savefig('Newton.jpg')
    plt.show()


if __name__ == '__main__':
    ''' 插值节点, 这里用二次函数生成插值节点，每两个节点x轴距离位10 '''
    sr_x = [i for i in range(-50, 51, 10)]
    sr_fx = [i ** 2 for i in sr_x]

    Nx = get_Newton_inter(sr_x, sr_fx)  # 获得插值函数

    tmp_x = [i for i in range(-50, 51)]  # 测试用例
    print(tmp_x)
    tmp_y = [Nx(i) for i in tmp_x]  # 根据插值函数获得测试用例的纵坐标
    print(tmp_y)

    ''' 画图 '''
    plt.figure("plt")
    ax1 = plt.subplot(111)
    plt.sca(ax1)
    plt.plot(sr_x, sr_fx, linestyle='', marker='o', color='b')
    plt.plot(tmp_x, tmp_y, linestyle='--', color='r')
    plt.show()

    # 插值
    data = [[0, 0], [1, 2], [2, 3], [3, 8], [4, 2]]
    plot(data, 100)
