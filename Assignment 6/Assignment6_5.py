# create 2 threads named as thread1 and thread2 
# thread1 display 1 to 50 on screen
# thread2 display 50 to 1 on screen in reverse order on screen 
# after execution thread1 gets completed then schedule thread2 

import threading

def print_numbers1():
    print("Enter in thread 1 ")
    for i in range(1, 51):
        print(i)

def print_numbers2():
    print("Enter in thread 2")
    for i in range(50, 0, -1):
        print(i)

def main():
    t1 = threading.Thread(target=print_numbers1)
    t2 = threading.Thread(target=print_numbers2)

    t1.start()
    t1.join() 
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
