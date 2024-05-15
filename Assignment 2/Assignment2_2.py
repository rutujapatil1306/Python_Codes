# write a program which accept one number & display below pattern 

def Display(size):
    for  i  in range(size):  # Loop for rows
        for j in range(size):  # Loop for columns
            print("*", end=" ") 
        print()  # Move to the next line after each row

def main():
    size = int(input("Enter the number to display the pattern : "))
    Display(size)

if __name__ == "__main__":
    main()
