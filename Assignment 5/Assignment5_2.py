#  input - 5 
#  output - 1  2  3  4  5  

def Display(No,current = 1):
     
    if current <= No:
        print(current , end = " ")

        Display(No,current + 1)
        
def main():
    A = int(input("Enter the number you want to display the pattern : "))

    Display(A)
    
    print()

if __name__ == "__main__":
    main()