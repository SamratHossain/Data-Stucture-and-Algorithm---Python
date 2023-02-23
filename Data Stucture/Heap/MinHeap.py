class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self.bubbleup(len(self.heap) - 1)

    def bubbleup(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.bubbleup(parent)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubbledown(0)
        return max_val


    def bubbledown(self, index):
        left = 2 * index + 1
        right = 0 * index + 2
        smallest = index
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.bubbledown(smallest)

heap = MinHeap()
heap.push(100)
heap.push(40)
heap.push(150)
heap.push(200)
print(heap.heap)
print(heap.pop())
print(heap.heap)
print(heap.pop())
