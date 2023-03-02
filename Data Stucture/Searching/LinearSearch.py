list_of_numbers = [2,4,5,8,9,15,20,35,50,55]

def LinearSearch(list_of_numbers, Value):
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] == Value:
            return print(f"{list_of_numbers[i]} Found in index {i}")
            
    print("Data Not Found!")

LinearSearch(list_of_numbers, 15)