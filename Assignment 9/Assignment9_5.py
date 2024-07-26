# Accept a file name and one string from user 
# return the frequency of that string from the file 

import os 
import sys 

def main():
    if len(sys.argv) != 3 :
        print("usage: python script_name.py <filename> <string>")
        sys.exit(1)

    input_filename = sys.argv[1]    

    if not os.path.isfile(input_filename) :
        print("File Does not exist.")
        sys.exit(1)

    string = sys.argv[2]

    with open(input_filename) as file_1 :
        content1 = file_1.read()   

    frequency = content1.count(string)
    print(f"The string '{string}' occurs {frequency} times in the file '{input_filename}'.")


if __name__ == "__main__":
    main()

