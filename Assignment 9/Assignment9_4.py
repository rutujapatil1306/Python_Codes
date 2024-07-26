# write a program which accept 2 file names from user 
# compare the content of both the files 
# if both the files contains same content then Display sucess otherwise dipaly failure 
# Accept names of both the files from commomd line 

import os 
import sys
from difflib import Differ 

def main():

    if len(sys.argv) != 3 :
        print("Usage : python script.py <filename> <filename>")
        sys.exit(1)

    input_filename1 = sys.argv[1]

    input_filename2 = sys.argv[2]

    if not os.path.isfile(input_filename1) or not os.path.isfile(input_filename2):
        print("One or both the file does not exist. ")
        sys.argv(1)

    with open(input_filename1,'r') as file_1, open (input_filename2,'r') as file_2 :
        content1 = file_1.read ()
        content2 = file_2.read () 

    if content1 == content2 :
        print("Sucess: Both files have same content.")   
    else :
        print("Failure : The files have different content")    

if __name__ == "__main__":
    main()