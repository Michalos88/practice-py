"""MinHeap and MaxHeap using built-in heapq"""

import heapq


class MinHeap:
    def __init__(self):
        self.data = list()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, num):
        self.size += 1
        heapq.heappush(self.data, num)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return heapq.heappop(self.data)

    def peek(self):
        return self.data[0]


class MaxHeap:
    def __init__(self):
        self.data = list()
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, num):
        self.size += 1
        heapq.heappush(self.data, -num)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return -heapq.heappop(self.data)

    def peek(self):
        return -self.data[0]
