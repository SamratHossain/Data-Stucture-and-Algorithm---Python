class Queue:
    def __init__(self, limit=5):
        self.limit = limit
        self.queue = []

    def Size(self):
        return len(self.queue)

    def isEmpty(self):
        if self.Size() == 0:
            return True
        else:
            return False

    def EnQueue(self, value):
        if self.Size() >= self.limit:
            print("Queue Overflow")
        else:
            self.queue.append(value)

    def DeQueue(self):
        if self.isEmpty():
            print("Queue is UnderFlow")
        else:
            self.queue.pop(0)

    def Top(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            size = self.Size()
            print(self.queue[size-1])

    

    def Display(self):
        print(self.queue)


if __name__ == '__main__':

    queue = Queue()
    # queue.EnQueue(5)
    # queue.EnQueue(10)
    # queue.EnQueue(15)
    # queue.EnQueue(20)
    queue.DeQueue()
    # queue.isEmpty()
    queue.Display()
    # print(queue.Size())
    # queue.Top()
    