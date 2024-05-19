# filter - All prime numbers 
# map - multiply each number by 2 
# reduce - maximun number from that number 

from functools import reduce 

def CheckPrime(No):
    if No <= 1:
        return False
    for i in range(2, int(No**0.5) + 1):
        if No % i == 0:
            return False
    return True

def Multiply(No):
    return No * 2 

def Maximum(A,B):
    return A if A > B else B 

def main():
    Data = []

    size = (int(input("Enter the number fo elements :")))

    print("Enter the number of Elements : ")
    for i in range(0,size):
        No = int(input())
        Data.append(No)

    print("Data From input list : ",Data)  

    FData = list(filter(CheckPrime,Data))
    print("Data After filter activity is :",FData)

    MData = list(map(Multiply,FData))
    print("Data after map function is :",MData)

    RData = (reduce(Maximum,MData))
    print("Data after Reduce activity is :",RData)

if __name__ == "__main__":
    main()