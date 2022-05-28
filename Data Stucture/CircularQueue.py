class Queue:

    def __init__(self, MaxSize):
        self.queue = []
        self.MaxSize = MaxSize
        self.front = -1
        self.rear = -1

    def EnQueue(self, data):
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue.insert(self.rear, data)
        elif (self.rear+1) % self.MaxSize ==  self.front:
            print("Queue is Full")
        else:
            self.rear = (self.rear + 1) % self.MaxSize
            self.queue.insert(self.rear, data)

    def DeQueue(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Empty")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.MaxSize

    def Display(self):
        if self.front == -1 and self.rear == -1:
            print("Queue is Empty")
        else:
            # Display using While Loop
            i = self.front
            while i != self.rear:
                print(self.queue[i])
                i = (i + 1) % self.MaxSize
            print(self.queue[self.rear])

            # Display using for loop
            # if self.front < self.rear:
            #     for i in range(self.front, self.rear+1):
            #         print(self.queue[i], end=" ")
            # elif self.front > self.rear:
            #     for i in range(self.front, self.MaxSize+1):
            #         print(self.queue[i], end=" ")
            #     for i in range(0, self.rear+1):
            #         print(self.queue[i], end="")

            
            print(f'Front: {self.front} Rear: {self.rear}')

q = Queue(5)
q.EnQueue(1)
q.EnQueue(2)
q.EnQueue(3)
q.Display()
q.DeQueue()
q.Display()
q.EnQueue(4)
q.EnQueue(5)
q.Display()
q.DeQueue()
q.Display()
q.EnQueue(6)
q.Display()


# for i in range(1, 10):
#     print(i)