class QuickSort:

    def quick_sort(self, low, high):
        if low < high:
            j = self.Partition(low, high)
    
            self.quick_sort(low, j)
            self.quick_sort(j+1, high)

    def Partition(self, low, high):
        pivot = arr[low]
        i = low
        j = high
        while i < j:
            while arr[i] <= pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        if i > j:
            arr[low], arr[j] = arr[j], arr[low]
            return j



arr = [5,10,4,9,7,2,15,20,8,30]

low = 0
high = len(arr) - 1

q = QuickSort()

print(arr) #print unsorted array
q.quick_sort(low, high)
print(arr) #print sorted array
