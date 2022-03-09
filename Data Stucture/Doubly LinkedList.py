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

            NewNode = Node(data, None, current)
            current.next = NewNode

    def InsertAt(self, index, data):

        if index < 1 or  index > self.Length():
            print("Invalid Index")

        elif index == 1:
            self.InserAtTheBegining(data)

        else:
            current = self.head
            count = 1

            while current:
                if count == index-1:
                    NewNode = Node(data, current.next, current)
                    current.next = NewNode
                    current.next.previous = NewNode

                current = current.next
                count += 1

    def Length(self):
        
        current = self.head
        count = 0

        while current:
            current = current.next
            count += 1

        return count

    def Remove(self, index):

        if index < 1 or index > self.Length():
            print("Invalid Index")

        elif index == 1:
            self.head = self.head.next
            return

        else:
            current = self.head
            count = 1

            while current:
                if count == self.Length():
                    current.previous.next = current.next
                    break
                elif count == index:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    break

                current = current.next
                count += 1

    def Clear(self):
        self.head = None
        return

    def Display(self):
        if self.head == None:
            print("LinkedList is Empty")
            return

        linked_lists = ''

        current = self.head

        while current:
            linked_lists += str(current.data) + '-->'
            current = current.next

        print(linked_lists)


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.InserAtTheBegining(10) 
    linkedList.InserAtTheBegining(20) 
    linkedList.InserAtTheBegining(30)
    linkedList.InserAtTheEnd(40)
    linkedList.InserAtTheEnd(50)
    linkedList.InsertAt(1, 100)
    linkedList.Remove(3)
    print(linkedList.Length())
    linkedList.Clear()
    linkedList.Display() 
