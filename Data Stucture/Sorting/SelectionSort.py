class SelectionSort:
    def selection_sort(self, unsorted_array):

        for i in range(0, len(unsorted_array) - 1):
            min = i
            for j in range(i+1, len(unsorted_array)):
                if unsorted_array[j] < unsorted_array[min]:
                    min = j
                if i is not min:
                    unsorted_array[i], unsorted_array[min] = unsorted_array[min], unsorted_array[i]
        print(unsorted_array)

unsorted_array = [5,10,4,9,7,2,15,20,8,30]

print(unsorted_array)
sorted_array = SelectionSort()
sorted_array.selection_sort(unsorted_array)         
