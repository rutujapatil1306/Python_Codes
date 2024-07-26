
import os

def main():

    print("Enter the file name  you want to write ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname,'a')
        print("File is sucessfully opend in write mode")

        print("Enter Data that you want to write in file ")
        Data = input()

        fobj.write(Data)

    else :
        print("Unable to open the file because the file is not present in current directory ")
if __name__ == "__main__":
    main()
