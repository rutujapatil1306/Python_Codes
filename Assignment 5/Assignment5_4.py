# write a recursive program which accept number from user and return summation of its digits 
 
def Sum_Of_Digits(No):
    if No == 0:
        return 0
    else:
        return (No % 10) + Sum_Of_Digits(No // 10)

def main():
    A = int(input("Enter the number to find the summation of its digits: "))
    result = Sum_Of_Digits(A)
    print("The summation of the digits is:", result)

if __name__ == "__main__":
    main()
