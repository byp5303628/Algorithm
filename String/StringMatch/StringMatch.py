# -*- coding: utf-8 -*-
import random
import datetime

s = "abcdefghijklmnopqrstuvwxyz"


def random_string(size):
    l = []
    for i in range(size):
        l.append(s[random.randint(0, len(s) - 1)])

    return "".join(l)


# 朴素算法
def algorithm1(src, target):
    for i in range(len(src)):
        flag = True
        for j in range(len(target)):
            if i + j >= len(src):
                return -1

            if src[i + j] != target[j]:
                flag = False
                break

        if flag:
            return i

    return -1


# KMP 算法
def algorithm2(src, target):
    pass


if __name__ == "__main__":

    src = random_string(10000)
    print datetime.datetime.now()
    for i in range(10000):
        target = random_string(20)

        try:
            if src.find(target) != -1:
                print src
                print target
            if src.find(target) != algorithm1(src, target):
                print "Test Failed"
                print src
                print target
        except:
            print "Test Failed"
            print src
            print target

    print datetime.datetime.now()
