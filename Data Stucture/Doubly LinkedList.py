class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None

    def InserAtTheBegining(self, data):
        if self.head is None:
            NewNode = Node(data, None, None)
            self.head = NewNode
        else:
            NewNode = Node(data, self.head, None)
            self.head.previous = NewNode
            self.head = NewNode

    def InserAtTheEnd(self, data):
        if self.head is None:
            NewNode = Node(data, None, None)
            self.head = NewNode
        else:
            current = self.head
            while current.next != None:
                current = current.next

            current.next = Node(data, None, current)


if __name__ == '__main__':
    linkedList = LinkedList() 
