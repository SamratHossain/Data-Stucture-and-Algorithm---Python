class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._bubble_down(0)
        return max_val

    def _bubble_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._bubble_up(parent)


    def _bubble_down(self, index):
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._bubble_down(largest)

heap = MaxHeap()
heap.push(50)
heap.push(100)
heap.push(150)
heap.push(200)
heap.push(70)
heap.push(300)
print(heap.heap)
print(heap.pop())
# print(heap.heap)
# print(heap.pop())
# print(heap.pop())

