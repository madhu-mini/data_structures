import numpy as np


class TwoStacks:

    def __init__(self, size):
        self.size = size
        self.arr = np.zeros([size], dtype=int)
        self.top1 = -1
        self.top2 = self.size

    def push1(self, value):
        if (self.top1 + 1) != self.top2:
            self.top1 += 1
            self.arr[self.top1] = value

    def push2(self, value):
        if self.top1 != (self.top2 - 1):
            self.top2 -= 1
            self.arr[self.top2] = value

    def pop1(self):
        if self.top1 == -1:
            return None
        value = self.arr[self.top1]
        self.top1 -= 1
        return value

    def pop2(self):
        if self.top2 == self.size:
            return None
        value = self.arr[self.top2]
        self.top2 += 1
        return value
