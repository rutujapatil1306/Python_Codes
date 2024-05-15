# write a program which accept number from user and return addition of digits in that number 
#  input - 5187934            Output - 37

def Sum_Digit(No1):
     num_str = str(No1)
     digit_sum = 0  

     for digit in num_str:
        digit_sum += int(digit) 

     return digit_sum
   

def main():
    A = int(input("Enter a number : "))

    Ret = Sum_Digit(A)

    print("Sum of Digits :",Ret)

if __name__ == "__main__":
    main()