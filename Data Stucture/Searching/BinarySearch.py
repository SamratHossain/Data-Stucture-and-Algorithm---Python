list_of_numbers = [2,4,5,8,9,15,20,35,50,55]

def BinarySearch(list_of_numbers, value):
    left = 0
    right = len(list_of_numbers) - 1

    while left <= right:
        mid = (left + right) // 2
        if list_of_numbers[mid] == value:
            return print(f"{list_of_numbers[mid]} Found in Index {mid}")
        elif value < list_of_numbers[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print("Data is Not Found")

BinarySearch(list_of_numbers,55)
