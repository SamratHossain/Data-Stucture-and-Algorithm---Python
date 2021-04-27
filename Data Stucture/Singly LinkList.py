class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self):
        self.head = None

    def InserAtTheBegining(self, data):
        if self.head is None:
            NewNode = Node(data)
            self.head = NewNode
        else:
            NewNode = Node(data, self.head)
            self.head = NewNode


    def InserAtTheEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def InsertValues(self, data_list):
        self.head = None
        for data in data_list:
            self.InserAtTheEnd(data)

    def InserAt(self, index, data):
        if index < 0 or index >= self.Length():
            raise Exception("Invalid Index")

        if index == 0:
            self.InserAtTheBegining(data)

        itr = self.head
        count = 0
        while itr:
            if count == index:
                NewNode = Node(data, itr.next)
                itr.next = NewNode
                break

            itr = itr.next
            count += 1

    def Length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def Remove(self, index):
        if index < 0 or index >= self.Length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def Clear(self):
        self.head = None
        return

    def Display(self):
        if self.head is None:
            print("LinkList is Empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)



if __name__ == '__main__':
    mylist = LinkList()
    mylist.InserAtTheBegining(10)
    mylist.InserAtTheBegining(20)
    mylist.InserAtTheEnd(30)
    mylist.InserAtTheEnd(40)
    mylist.InserAt(1, 25)
    mylist.Remove(2)
    print(mylist.Length())
    mylist.Display()
    mylist.Clear()
    mylist.Display()