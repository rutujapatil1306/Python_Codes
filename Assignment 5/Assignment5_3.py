#  input - 5 
#  output - 5  4  3  2  1   

def Display(No):
     
    if  No > 0:
        print(No, end = " ")

        Display(No - 1)
        
def main():
    A = int(input("Enter the number you want to display the pattern : "))

    Display(A)
    
    print()

if __name__ == "__main__":
    main()