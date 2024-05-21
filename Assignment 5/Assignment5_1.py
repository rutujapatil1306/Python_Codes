# write a recursive Program which display below pattern 
# 5
# *  *  *  *  *

def Display(No):
    if No > 0 :
        print("*",end= " ")
        Display(No-1)

def main():
    print("Enter thr number you want to display the pattern : ")

    A = int(input())

    Display(A)

    print()


if __name__ == "__main__":
    main()