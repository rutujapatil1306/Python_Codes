# wrute a program which accept one numnber from and check whether the number is prime or not 

def CheckPrime(No1):
    for i in range(2,No1,):
        if ( No1 % i == 0):
            print("The number is not prime")
            break
    else :
            print("The number is prime")    
          
def main():

    A = int(input("Enter the number :"))

    CheckPrime(A)

if __name__ == "__main__":
    main()