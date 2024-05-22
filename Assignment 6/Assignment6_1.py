# Design python application which creates two thread named as even and odd 
# Even thread will display first 10 even numbers 
# Odd thread will display first 10 odd numbers 

import multiprocessing 

def EvenDisplay(No):
    print("List of Even numbers : ")
    x = 2 
    for i in range (No):
        print(x)
        x = x + 2

def OddDisplay(No):
    print("List of Odd numbers : ")
    x = 1 
    for i in range(No):
        print(x)
        x = x + 2        

def main():
    A = 10

    p1 = multiprocessing.Process(target = EvenDisplay, args = (A,))
    p2 = multiprocessing.Process(target = OddDisplay, args = (A,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main Function ")

if __name__ == "__main__":
    main()