# -*- coding: utf-8 -*-
# @Author: bd
# @Date:   2024-02-29 16:47:18
# @Last Modified by:   bd
# @Last Modified time: 2024-03-01 09:42:02


'''
题目：用两种方式编写一百以内的斐波那契数列。
斐波那契数列是指这样一个数列：1，1，2，3，5，8，13，21，34，55，89……这个数列从第3项开始 ，每一项都等于前两项之和。
（可以同思路，写法不同即可）
注：如遇到疑问可咨询面试官。
代码运行：点击上方任务栏---》工具---》编译，或直接按快捷键Ctrl+B
'''

def f1(n):
    res = []
    res.append(1)
    res.append(1)
    for i in range(2,n):
        next_number = res[-1]+res[-2]
        res.append(next_number)
    return res

def f2Help(n):
    if n <= 1:
        return 1
    else:
        return f2Help(n-1)+f2Help(n-2)

def f2(n):
    res = []
    for i in range(n):
        res.append(f2Help(i))
    return res


