# write a program which accept one number and display the below pattern 
# 5
#  1
#  1   2 
#  1   2   3
#  1   2   3    4
#  1   2   3    4   5

def Display(No1):
   for i in range(1, No1 + 1):
        print(' ' , end='')  
        for j in range(1, i + 1):
            print(j, end=' ')
        print()    

def main():
    A = int(input("Enter the  number"))

    Display(A)

if __name__ == "__main__":
    main()
