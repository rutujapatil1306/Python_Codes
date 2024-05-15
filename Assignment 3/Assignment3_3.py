# write a program which accept a n number from user and store it in list . return Minimum number from list 

def Minimum(num_list):
    total = min(num_list)
    return total

def main():
    A = int(input("Enter the numberof Elements : "))
    num_list = []

    for i in range(A):
        num = int(input("Enter The number :"))
        num_list.append(num)

    Ret = Minimum(num_list)
    print("Minimum Number from the list is  :",Ret)


if __name__ == "__main__":
    main()