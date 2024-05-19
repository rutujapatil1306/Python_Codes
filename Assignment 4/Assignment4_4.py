# filter should filter out all such numbers which are even 
# map function should calculate its square 
# Reduce will return addition of all that number 

from functools import reduce 

CheckEven = lambda No : (No % 2 == 0) 

Square = lambda No : No*No

Add = lambda A,B : A + B

def main():
    Data = []

    size = int(input("Enter the Number of Elements you Want : "))

    print("Enter the Elements in the List : ")
    for i in range(0,size):
        No = int(input())
        Data.append(No)

    print("Data from Input List : ",Data)

    FData = list(filter(CheckEven,Data))
    print("Data After filter activity is : ",FData)

    MData = list(map(Square,FData))
    print("Data After map activity is :",MData)

    RData = (reduce(Add,MData))
    print("Data After Map Activity is :",RData)
    

if __name__ == "__main__":
    main()