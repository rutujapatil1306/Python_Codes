# write a program which accept the number from user & print that number of "*" on screen 

def Display(num):
    print("*" * num)

def main():
    num = int(input("Enter a number: "))
    Display(num)

if __name__ == "__main__":
    main()
