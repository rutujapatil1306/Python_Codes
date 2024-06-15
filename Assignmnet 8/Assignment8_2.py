# write a program which contains one class named as Bank Account 
# Bank Account Class two instance variable as Name And Amount
# that class contains one class variable as ROI which is initialise to 10.5
# inside init methid initialise all names and amount variables by accepting the values from user 
# there are four instance method inside class as Display(), Deposit(), Withdraw(), CalculateInterst()
# Deposit () method will accept the amount fro user and add that value in class instance variable Amount 
# withdraw() method will accept the amount to withdraw from the user and substract that amount from class instance variable Amount 
# CalculateIntrest() method calculate the intrest based on Amount by Considering rate of intrest which is class variable as ROI
# Display() method will display value  of all the instance variable as Name and Amount 

class Bank_Account:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter the Name of the customer: ")
        self.Amount = float(input("Enter the Total Amount that the customer has: "))

    def Deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.Amount += amount
        print("Amount Deposited Successfully.")
        print("New Balance: ", self.Amount)

    def Withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.Amount:
            print("Insufficient Amount")
        else:
            self.Amount -= amount
            print("Amount Withdrawn Successfully.")
            print("New Balance: ", self.Amount)

    def CalculateInterest(self):
        interest = (self.Amount * Bank_Account.ROI) / 100
        print("Interest on the current Amount is: ", interest)

    def Display(self):
        print("Customer Name: ", self.Name)
        print("Customer Amount: ", self.Amount)
        print("----------------------------------------------")

def main():
    Account = Bank_Account()
    while True:
        print("\n1. Display Account Information")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Calculate Interest")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            Account.Display()
        elif choice == 2:
            Account.Deposit()
        elif choice == 3:
            Account.Withdraw()
        elif choice == 4:
            Account.CalculateInterest()
        elif choice == 5:
            print("Exiting the Program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
