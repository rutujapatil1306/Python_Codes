# write a program which accept number from user and return number of digits in that number 
# input - 5187934        Output - 7 

def Digit_Count(No1):
    num_str = str(No1)
    return len(num_str)

def main():
    A = int(input("Enter a number : "))

    Ret = Digit_Count(A)

    print("Number of Digits : ",Ret)
    

if __name__ == "__main__":
    main()