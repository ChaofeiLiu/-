from collections import deque
class Queue():
    def __init__(self):
        self.items =deque()
    def append(self,val):
        return self.items.append(val)
    def pop(self):
        return self.items.popleft()
    def empty(self):
        return len(self.items) == 0
def test_queue():
    q = Queue()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())
test_queue()