# write a program which accept one number from user & return its factorial 

def Factorial(No1):
    Fact = 1
    for i in range(No1,1,-1):
        Fact = Fact * i
    return Fact   



def main():
    A = int(input("Enter the number : "))

    Result = Factorial(A)

    print("The factorial of the number is : ",Result)

if __name__ == "__main__":
    main()