# Create 2 threads EvenList and OddList ,both the threads accepts list of integers as parameters 
# EvenList thread add all even elements from input list and display the addition 
# OddList thread add all  odd elements from  input list and display the addition 

import threading

def Even_List(numbers):
    print("Even Elements from the input list")
    even_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
    print("Sum of all even elements in the list is:", even_sum)

def Odd_List(numbers):
    print("Odd Elements from the input list")
    odd_sum = 0
    for num in numbers:
        if num % 2 != 0:
            odd_sum += num
    print("Sum of all odd elements in the list is:", odd_sum)

def main():
    data = []

    size = int(input("Enter the number of elements you want in your list: "))

    for i in range(size):
        element = int(input("Enter the element: "))
        data.append(element)
    
    print("Elements from the list are:", data)

    t1 = threading.Thread(target=Even_List, args=(data,))
    t2 = threading.Thread(target=Odd_List, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main function")

if __name__ == "__main__":
    main()
