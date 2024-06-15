# write a program which contains one class named as Bookstore
# bookStore class contains two instance variable as Name,Author 
# that class contains one class variable as No of Books which is initialize as 0
# there is one instance method of class as Display which display Name ,Author and number of book 
# Initialise instance variable in init method by accepting the values from user as name as name and author 
# inside init method increment value of No of Books by one 

class BookStore:
    No_of_Books = 0 

    def __init__(self):
        self.Name = input("Enter the name of the book : ")
        self.Author = input("Enter the name of the Author : ")
        BookStore.No_of_Books  +=1

    def Display(self):
        print("Book Name : ",self.Name)
        print("Author Name : ",self.Author)
        print("Total Number of Books : ",BookStore.No_of_Books)

def main():

    Book1 = BookStore()
    Book2 = BookStore()

    print("Details of Book 1 \n")
    Book1.Display()

    print("\nDetails of Books 2 \n")
    Book2.Display()

if __name__ == "__main__":
    main()