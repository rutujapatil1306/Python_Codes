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