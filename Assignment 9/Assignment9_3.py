# write a program whcih accept file name from user and create new file named as dedmo.txt 
# copy all the content from existing file into new file 
# Accept the file name through commond line argument 

import os 
import sys

def main():

# check if the user has provided the file name as a command line argument 
    if len(sys.argv) != 2 :
        print("Usage : python script.py <filename>")
        sys.exit(1)

# Get the file name from the command line arguments 
    input_filename = sys.argv[1]

# check if the input file exists 
    if not os.path.isfile(input_filename):
        print("File Does not exist",input_filename)
        sys.exit(1)

# Define the new file name        
    output_filename = "Demo.txt"

# open the output file and the new file 
    with open(input_filename,'r') as infile , open(output_filename,"w") as outfile:

# copy the content from the input file to new file 
        for line in infile:
            outfile.write(line)

    #  print(f"Content of {input_filename} is copied into {output_filename} : ) 

    print(f"Content of {input_filename} is copied into {output_filename}:")
                     

if __name__ == "__main__":
    main()