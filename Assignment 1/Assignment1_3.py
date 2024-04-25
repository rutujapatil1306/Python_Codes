# write a program to do addition of two numbers 

def Add(No1, No2):
    Ans = No1 + No2
    return Ans 

def main():
    print("Enter first number")
    A = int(input())

    print("Enter Second Number")
    B = int(input())

    Result = Add(A, B)

    print("Addition of Two is", Result)

if __name__ =="__main__":
    main()

    

