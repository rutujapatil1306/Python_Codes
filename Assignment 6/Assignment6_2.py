# create two threads as EvenFactors and OddFactors both thread accept one parameter as integer 
# EvenFactor will display addition of even factors of given numbers 
# OddFactors will display  addition of odd factors of given numbers 

import multiprocessing

def EvenFactors(No):
    Sum_Even = 0 
    print("Calculating Even Factors of given numbers ")
    for i in range(1, No+1 ):
        if No % i == 0 and i % 2 == 0 :
            Sum_Even = Sum_Even + i
    print("Sum of even factors is : ",Sum_Even)   

def OddFactors(No):
    Sum_Odd = 0 
    print("Calculating Odd Factors of given numbers ")
    for i in range (1,No+1 ):
        if No % i == 0 and i % 2 != 0 :
             Sum_Odd = Sum_Odd + i 
        print("Sum of odd factors is :",Sum_Odd)

def main():
    A = int(input("Enter the number : "))

    p1 = multiprocessing.Process(target = EvenFactors , args = (A,))
    p2 = multiprocessing.Process(target = OddFactors , args = (A,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()
