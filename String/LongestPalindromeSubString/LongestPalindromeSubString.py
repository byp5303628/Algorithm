# -*- coding: utf-8 -*-


def is_palindrome(s):
    str_length = len(s)

    for i in range(str_length / 2):
        if s[i] != s[str_length - 1 - i]:
            return False

    return True


def change(s):
    l = []
    for c in s:
        l.append(c)

    return "@#%s#" % "#".join(l)


# 暴力求解法
def algorithm1(s):
    length = len(s)

    for i in range(length):
        for j in range(i + 1):
            if is_palindrome(s[j: length - i + j]):
                return len(s[j: length - i + j])

    return 1


# 动态规划法
def algorithm2(s):
    pass


# 中心求解法
def algorithm3(s):
    s = change(s)
    flag = 0
    for i in range(2, len(s) - 2):
        temp = 1
        while s[i - temp] == s[i + temp]:
            temp += 1

        if temp > flag:
            flag = temp

    return flag - 1


# Manacher算法
def algorithm4(s):
    s = change(s)
    p = [0] * len(s)
    index = 0
    for i in range(2, len(s) - 2):
        if p[index] + index > i:
            p[i] = min(p[2 * index - i], p[index] + index - i)
        else:
            p[i] = 1

        while s[i - p[i]] == s[i + p[i]]:
            p[i] += 1

        if index + p[index] < i + p[i]:
            index = i

    return max(p) - 1


if __name__ == "__main__":
    s1 = "abbac"
    print s1
    print algorithm4(s1)
    print algorithm3(s1)
    print algorithm1(s1)
