# 问题
# 怎样实现一个按优先级排序的队列？ 并且在这个队列上面每次 pop 操作总是返回优先级最高的那个元素
import heapq

class PriorityQueue():
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # -priority表示用优先级从大到小排列
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item("Zahir"), 1)
q.push(Item("Zahi"), 2)
q.push(Item("Zah"), 3)
q.push(Item("ZA"), 1)

for i in range(4):
    print(q.pop())



