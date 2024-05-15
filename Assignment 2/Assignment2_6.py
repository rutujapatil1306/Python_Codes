# Decreasing triangle 

def Display(No):
    for i in range(No, 0, -1):  
        for j in range(i): 
            print('*', end=' ')
        print()   

def main():
    A = int(input("Enter the number :"))
    Display(A)

if __name__ == "__main__":
    main()


   