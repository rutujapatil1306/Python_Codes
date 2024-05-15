# write a program which accept a number from user and return addition of its factors 

def AddFactors(No1):
    sum = 0 
    for i in range (1,No1 + 1 ):
        if (No1 % i == 0):
            sum = sum + i
    return sum        

def main():
    A = int(input("Enter a number : "))

    Result = AddFactors(A)

    print("Addition of Factors is : ",Result)

if __name__ == "__main__":
    main()