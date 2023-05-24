class InsertionSort:
    def insertion_sort(self, unsorted_array):
        for i in range(1, len(unsorted_array)):
            temp = unsorted_array[i]
            j = i - 1
            while j >= 0 and unsorted_array[j] > temp:
                unsorted_array[j+1] = unsorted_array[j]
                j -= 1
            unsorted_array[j+1] = temp
        
        print(unsorted_array)
            

unsorted_array = [5,10,4,9,30,7,2,15,20,8]

print(unsorted_array)
sorted_array = InsertionSort()
sorted_array.insertion_sort(unsorted_array)
