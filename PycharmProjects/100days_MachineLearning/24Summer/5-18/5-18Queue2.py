'''
单向链表实现队列
'''

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

class MyQueue(object):
    def __init__(self):

