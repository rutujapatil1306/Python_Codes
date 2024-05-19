# write a program which contain one lambda function which accept two  parameter and return its multiplication 

Multiplication  = lambda A,B : A*B

def main():
    A = int(input("Enter first number : "))
    B = int(input("Enter Second number : "))

    Result = Multiplication(A,B)

    print("The Multiplication of two number is :",Result)

if __name__ == "__main__":
    main()