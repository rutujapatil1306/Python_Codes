# write a program which accept the number user and store it into list . Return Maximun number from from the list 


def Maximun(num_list):
    total = max(num_list)
    return total

def main():
    A = int(input("Enter the numberof Elements : "))
    num_list = []

    for i in range(A):
        num = int(input("Enter The number :"))
        num_list.append(num)

    Ret = Maximun(num_list)
    print(" Maximun number from the list is  :",Ret)


if __name__ == "__main__":
    main()
