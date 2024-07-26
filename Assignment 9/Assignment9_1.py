# write a program which accept file name from user and check whether
#  that file exists in current directory or not 

import os 

def main():
    print("Enter the name of the file that you want to search  : ")
    Fname = input()

    if os.path.exists(Fname):
        print("File exists in current directory.")

    else :
        print("The file does not exists in current directory.")

if __name__ == "__main__":
    main()
