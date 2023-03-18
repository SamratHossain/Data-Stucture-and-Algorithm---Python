class MergeSort:
    
    def merge_sort(self, arr, low, high):
        new_arr = [None] * (high+1)
        if low < high:
            mid = (low+high) // 2
            self.merge_sort(unsorted_array, low, mid)
            self.merge_sort(unsorted_array, mid+1, high)
            self.merge(unsorted_array, new_arr, low, mid, high)
        return unsorted_array

    def merge(self, unsorted_array, new_arr, low, mid, high):
        i = low
        j = mid + 1
        k = low
        
        while i <= mid and j <= high:
            if unsorted_array[i] < unsorted_array[j]:
                new_arr[k] = unsorted_array[i]
                i += 1
            else:
                new_arr[k] = unsorted_array[j]
                j += 1
            k += 1
        
        if i > mid:
            while j <= high:
                new_arr[k] = unsorted_array[j]
                j += 1
                k += 1
        else:
            while i <= mid:
                new_arr[k] = unsorted_array[i]
                i += 1
                k += 1
        
        for i in range(low, high + 1):
            unsorted_array[i] = new_arr[i]
        

unsorted_array = [5,10,4,9,7,2,15,20,8,30]

low = 0
high = len(unsorted_array) - 1

ms = MergeSort()
print(unsorted_array)
sorted_array = ms.merge_sort(unsorted_array, low, high)
print(sorted_array)