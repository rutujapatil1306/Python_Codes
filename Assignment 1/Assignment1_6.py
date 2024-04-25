def check(No):
    if(No > 0 ):
        print("The number is Positive")
    else:
        print("The number is negative")    
    
def main():
    A = int(input("Enter number"))
    check(A)

if __name__ =="__main__":
    main()