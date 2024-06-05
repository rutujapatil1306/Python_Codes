# write a program which contains one class named as demo 
# Demo Class contains 2 instance variable as no1 , no2 
# that class contains one class variable as value 
# there are 2 instance method of class as fun and gun which display value of instance variables 
# initialise instance variable in init method by accepting the values from the user
# after creating the class create two objects of demo class as 
# obj1 = demo(11,21)
# obj2 = demo(51,101)
# now call the instance method as 
# obj1.Fun()
# obj1.Gun()

class Demo:
    value = 100

    def __init__(self,no1,no2):
        self.no1 = no1
        self.no2 = no2

    def Fun(self):
        print("Value of No1 : ",self.no1)
        print("Value of No2 : ",self.no2)

    def Gun(self):
        print("Value of No1 is : ",self.no1)
        print("value of No2 is : ",self.no2)     

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()

    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()