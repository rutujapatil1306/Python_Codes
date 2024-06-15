# Write a program  which contains one class named as number 
# Arithmatic class contains one instance Variable as value
# Inside init method initialise that instance variable to the value which is accepted from the user 
# chePrime() method will return true if number is prime other wise return false
# chkPerfect() method wii return true if number is perfect otherwise return false
# Factors() method will display all factors of instance variable
# SumFactor() method will return addition of all factors . user this method in any onother method as helper method if required 
# after designing the above class class call all instance methods by creating multiple objects 

class Number:
    def __init__(self):
        self.value = int(input("Enter a number: "))

    def chkPrime(self):
        if self.value <= 1:
            return False
        for i in range(2, int(self.value ** 0.5) + 1):
            if self.value % i == 0:
                return False
        return True

    def chkPerfect(self):
        return self.value == self.SumFactors()

    def Factors(self):
        factors = [i for i in range(1, self.value) if self.value % i == 0]
        return factors

    def SumFactors(self):
        return sum(self.Factors())

def main():
    number1 = Number()
    print(f"\nNumber: {number1.value}")
    print(f"Is Prime: {number1.chkPrime()}")
    print(f"Is Perfect: {number1.chkPerfect()}")
    print(f"Factors: {number1.Factors()}")
    print(f"Sum of Factors: {number1.SumFactors()}")

    print("------------------------------------------------")

    number2 = Number()
    print(f"\nNumber: {number2.value}")
    print(f"Is Prime: {number2.chkPrime()}")
    print(f"Is Perfect: {number2.chkPerfect()}")
    print(f"Factors: {number2.Factors()}")
    print(f"Sum of Factors: {number2.SumFactors()}")

if __name__ == "__main__":
    main()
