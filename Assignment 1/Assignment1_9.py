def Display():
    count = 0 
    num = 2

    while count < 10 :
        print(num)
        num = num + 2 
        count = count + 1


def main():
    print("First 10 even numbers are : ")
    Display()


if __name__ =="__main__":
    main()