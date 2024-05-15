# write a program which accept n number from user and store it into list . Accept one number from user and return frequency of that number from list 

def Frequency(No,num_list):
    Count = 0 
    for num in (num_list):
        if (num == No) :
            Count = Count + 1 

    return Count    


    return(Count)    
        
def main():
    A = int(input("Enter the number of Elements  : "))

    num_list = []

    for i in range(A):
        num = int(input("Enter the number : "))
        num_list.append(num)

    B = int(input("Enter one number from the list to Count the Frequency :"))
    
    Ret = Frequency(B,num_list)

    print("The Frequency of given number is : ",Ret )



if __name__ == "__main__":
    main()