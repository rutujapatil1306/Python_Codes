# Write a program  which contain filter() map() Reduce()in it .
# Python application which contains one list of number List contains the number which are aceepted from user .
# Filter out all such number which greater than or equal to 70 and less than or equal to 90 
# Map Function will increase each number by 10 .
# Reduce will return product of all that number 

from FMR_Moduel import * 
Greater = lambda No : ( 70 <= No <= 90)

Increase = lambda No : No + 1 

Product = lambda No,No1 : No * No1

def main():
    Data = []

    print("Enter the number of elements you want : ")
    size = int(input())

    print("Enter the elements :")
    iCnt = 0
    for iCnt in range(0,size):
        No = int(input())
        Data.append(No)  

    print("Data from input List : ",Data) 

    FData = list(filterX(Greater,Data))
    print("Data after filter activity :",FData)

    MData = list(mapX(Increase,FData))
    print("Data after  map activity :",MData)

    RData = reduceX(Product,MData)
    print("Data after map activity :",RData)     

if __name__ == "__main__":
    main()
