# write a program whcih contains one class named as circle
# circle class contains three instance variable as radius area circumference 
# That class contains one class variable as PI which is initialise to 3.14
# inside init method initialise all instance variable to 0.0
# there are three instance method inside class as Accept(),CalculateArea(),CalculateCircunference(),Display()
# Accept method will accept value of Radius fron user
# calculateAre() method will calculate are of circle and stor it into instance variable Area
# calculateCirfumferemve() will calculate circumference of circle and store it into instancevariable cirfumference
# Display() method will  display value of all instancevariable as radius , area,circumference
# after designing the above class call all instance methods by creating multiple objects 

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0 
        self.Circumference = 0.0 

    def Accept(self):
         self.Radius= float(input("Enter the Value of Radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * (self.Radius ** 2)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius 

    def Display(self):
        print("Radius of Circle is : ",self.Radius)
        print("Area of circle is : ",self.Area)
        print("Circunference of circle is : ",self.Circumference)    

def main():
    circle1 = Circle()
    circle2 = Circle()

    circle1.Accept()
    circle1.CalculateArea()
    circle1.CalculateCircumference()
    print("Detailes of Circle 1 ")
    circle1.Display()
    print("------------------------------------------------\n")

    circle2.Accept()
    circle2.CalculateArea()
    circle2.CalculateCircumference()
    print("Detailes of Circle 2 ")
    circle1.Display()
    print("------------------------------------------------\n")

if __name__ == "__main__":
    main()