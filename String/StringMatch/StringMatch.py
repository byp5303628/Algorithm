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


def make_next(target):
    l = [0] * len(target)
    flag = 0
    for i in range(1, len(target)):
        if target[i] == target[flag]:
            flag += 1
        else:
            flag = 0
        l[i] = flag

    return l


# KMP 算法
def algorithm2(src, target):
    l = make_next(target)
    target_length = len(target)
    src_length = len(src)
    src_index = 0
    target_index = 0
    while src_index < src_length:
        while target_index < target_length:
            if src_index + target_index >= src_length:
                return -1
            if src[src_index + target_index] == target[target_index]:
                target_index += 1
            elif target_index >= 1:
                src_index += target_index - l[target_index - 1]
                target_index = l[target_index - 1]
            else:
                src_index += 1
                target_index = 0

        if target_index == target_length:
            return src_index

    return -1


if __name__ == "__main__":
    src = random_string(10000)
    print datetime.datetime.now()
    for i in range(1000):
        target = random_string(5)

        try:
            if src.find(target) != algorithm1(src, target):
                print "Test Failed"
                print src
                print target
        except:
            print "Test Failed"
            print src
            print target

    print datetime.datetime.now()
    # print algorithm2("abcaabcaabcab", "abcab")
    # print algorithm2("abcaabcaabcaa", "abcab")
