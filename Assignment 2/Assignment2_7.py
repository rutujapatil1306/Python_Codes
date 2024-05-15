# write a program which accept a number from user and display below pattern 
#  1   2   3   4   5 
#  1   2   3   4   5 
#  1   2   3   4   5 
#  1   2   3   4   5 
#  1   2   3   4   5 

def Display(No):
    for i in range(1,No+1):
        for j in range(1,No + 1):
            print(j,end = '\t')
        print()    
       
def main():
    A = int(input("Enter a number :"))
    Display(A)


if __name__ == "__main__":
    main()

   