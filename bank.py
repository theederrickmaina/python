class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)

if __name__ == "__main__":
    account = BankAccount("4571230", 2400000, "26-2-2024", "Derrick Gatu")
    print("Deposited:", account.deposit(1543001))
    print("Withdrawn:", account.withdraw(500000))
    print("Withdrawn:", account.withdraw(10000000))  
    account.check_balance()
    account.customer_details()
