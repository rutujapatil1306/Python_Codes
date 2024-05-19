# write a program which contain one lambda function which accept one parameter and return power of two 

Power_of_Two = lambda B : B ** 2

def main():
    A = int(input("Enter the number : "))

    Result = Power_of_Two(A)

    print("The Power of two is :",Result)

if __name__ == "__main__":
    main()