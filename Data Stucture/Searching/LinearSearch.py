List = [2,4,5,8,9,15,20,35,50,55]

def LinearSearch(List, Value):
    for i in range(len(List)):
        if List[i] == Value:
            return print(f"{List[i]} Found in index {i}")
            
    print("Data Not Found!")

LinearSearch(List, 60)