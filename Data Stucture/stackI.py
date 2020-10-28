class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self):
        item = input("Enter the value: ")
        self.stack.append(item)
        return print(f"Pushed: {item}")

    def pop(self):
        pop = self.stack.pop()
        return print(f"Removed: {pop}")

    def peek(self):
        top = self.stack[len(self.stack)-1]
        return print(f"Top value is: {top}")

    def size(self):
        return print(len(self.stack))

    def value(self):
        print(f"Items are: {self.stack}")


stack = Stack()

print("1.Push")
print("2.Pop")
print("3.Peek")
print("4.Size")
print("5.isEmpty")
print("6.Stack")

while True:
    number = int(input("Enter your choice: "))
    if number == 1:
        stack.push()
    elif number == 2:
        stack.pop()
    elif number == 3:
        stack.peek()
    elif number == 4:
        stack.size()
    elif number == 5:
        if stack.isEmpty():
            print("Stack is Empty")
        else:
            print("Stack is not Empty")
    elif number == 6:
        stack.value()

