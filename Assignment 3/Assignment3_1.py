# write a program in python which accept n from user store it in list and return additon of all the number in the list

def Addition(num_list):
    total = sum(num_list)
    return total

def main():
    A = int(input("Enter the numberof Elements : "))
    num_list = []

    for i in range(A):
        num = int(input("Enter The number :"))
        num_list.append(num)

    Ret = Addition(num_list)
    print("Sum of All number :",Ret)


if __name__ == "__main__":
    main()