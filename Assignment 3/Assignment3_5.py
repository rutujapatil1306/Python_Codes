# wriet a program which accept n number from user and store it into list 
# Return addition of all Prime numbers in that list 
# main python file accept n  number from user and pass each number to chlPrime() which is part of our user define module names as MarvellousNum.
# Name of the function from main python file should be listPrime()

from Marvellous import CheckPrime

def ListPrime(num_List):
    Sum = 0 
    for num in num_List :
        if CheckPrime(num):
            Sum = Sum + num
    return Sum        


def main():
    A = int(input("Enter the number of Elements :"))
    num_List = []

    for i in range(A):
        num = int(input("Enter the Elements : "))
        num_List.append(num)

    Ret = ListPrime(num_List)  
    print("The Sum of All prime number in the list is : ",Ret)  

if __name__ == "__main__":
    main()