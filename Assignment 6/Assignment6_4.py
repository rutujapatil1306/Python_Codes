# create 3 threads small , capital , digits all threads accept string as parameter 
# Samll threads display number of small characters 
# capital thread display number of capital characters 
# digit thread display number of digits in characters

import threading

def small_count(string):
    print("Enter in Small Thread")
    count = 0
    for char in string:
        if char.islower():
            count = count + 1 
    print(f"Number of lowercase letters: {count}")

def capital_count(string):
    print("Enter in Capital thread ")
    count = 0
    for char in string:
        if char.isupper():
            count = count + 1
    print(f"Number of uppercase letters: {count}")

def digit_count(string):
    print("Enter in digital thread ")
    count = 0
    for char in string:
        if char.isdigit():
            count = count + 1 
    print(f"Number of digits: {count}")

def main():
    input_string = input("Enter a string: ")

    t1 = threading.Thread(target=small_count, args=(input_string,))
    t2 = threading.Thread(target=capital_count, args=(input_string,))
    t3 = threading.Thread(target=digit_count, args=(input_string,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()
