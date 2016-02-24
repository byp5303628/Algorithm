# -*- coding: utf-8 -*-

# Input: 有一个长n米的木头，和一个price table如下：
# 长度i  1 2 3 4 5  6
# 价格Pi 1 5 8 9 10 17
# Output：找一个cut的方法，使最后赚的最多

dic = {
    1: 1,
    2: 5,
    3: 8,
    4: 9,
    5: 10,
    6: 17
}

count = 0


def cut(table, l):
    global count
    count += 1
    q = 0
    if l <= 0:
        return 0
    for i in table.keys():
        q = max(q, table[i] + cut(table, l - i))

    return q


print cut(dic, 15)
print count
