# write a program which accept a file name from user and open that file 
#  display the contents of that file on screen 

import os

def main():
    print("Enter the name of the file which you want to display the content : ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,'r')
        print("File is opened sucessfully for reading ")
        print(fobj.read())

    else :
        print("Unable to open the file because it is not present in the current directory ")

if __name__ == "__main__":
    main()