# write a program which contains one class named as Arithmatic 
# Arithmatic class contains three instace variable as value1,value2
# inside init method initialise all instance variable to 0 
# there are instance methid inside class as Accept(),Addition(),Sunstrection(),Multiplication(),Division()
# after designing the above class call all the instance method by creating multiple objects 

class Arithmatic:

    def __init__(self):
        self.Value1 = 0.0
        self.Value2 = 0.0
        self.Result = 0.0 

    def Accept(self):
        self.Value1 = float(input("Enter First Number : "))
        self.Value2 = float(input("Enter Second Number : "))

    def Addition(self):
        self.Result = self.Value1 + self.Value2 
        print("Addition of Two Numbers is : ",self.Result)

    def Substraction(self):
        if self.Value1 < self.Value2 :
            self.Result = self.Value2 - self.Value1 
            print("Substraction of Two Numbers is : ",self.Result)
        else:
            self.Result = self.Value1 - self.Value2 
            print("Substraction of Two Numbers is : ",self.Result)

    def Multiplication(self):
        self.Result = self.Value1 * self.Value2 
        print("Multiplication of Two Numbers is : ",self.Result)

    def Division(self):
        self.Result = self.Value1 / self.Value2 
        print("Division of Two Numbers is : ",self.Result)
                                    

def main():
    obj1 = Arithmatic()
    obj2 = Arithmatic()

    print("Operations for the first set of numbers:")
    obj1.Accept()
    obj1.Addition()
    obj1.Substraction()
    obj1.Multiplication()
    obj1.Division()
    print("------------------------------------------------\n")

    print("Operations for the Second set of numbers:")
    obj2.Accept()
    obj2.Addition()
    obj2.Substraction()
    obj2.Multiplication()
    obj2.Division()
    print("------------------------------------------------\n")
    

if __name__ == "__main__":
    main()