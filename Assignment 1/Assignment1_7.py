# write a program which contains one function that accept one number from user & return true if number is divisible by 5 otherwise return false 

def Divisible(No):
    if(No % 5 == 0):
        print("True")
    else:
        print("False")    

def main():
    A = int(input("Enter the number : "))
    Divisible(A)

if __name__ == "__main__":
    main()
