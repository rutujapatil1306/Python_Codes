# write a recursive program which accept number from user and returns its factorial 

def Factorial(No):
    if No == 0 or No == 1:
        return 1
    else:
        return No * Factorial(No - 1)

def main():
    A = int(input("Enter the number to find its factorial: "))
    result = Factorial(A)
    print(f"The factorial of given number is: ",result)

if __name__ == "__main__":
    main()
