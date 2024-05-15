import Arithmatic as Ar

def main():
    A = int(input("Enter first number : "))

    B = int(input("Enter second number : "))

    Result = Ar.Addition(A,B)
    print("Addition of two numbers is :",Result)
    print("-----------------------------------------------------")

    Result = Ar.Substraction(A,B)
    print("Substraction of two number is : ",Result)
    print("-----------------------------------------------------")

    Result = Ar.Multiplication(A,B)
    print("Multiplication of two numbere is : ",Result)
    print("-----------------------------------------------------")

    Result = Ar.Division(A,B)
    print("Division of two  number is : ",Result)
    print("-----------------------------------------------------")
    
if __name__ =="__main__":
    main()

