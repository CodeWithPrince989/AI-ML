class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ₹{self.balance}")


def main():
    accounts = {}

    while True:
        print("\n--- Banking System ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")

            if account_number in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[account_number].deposit(amount)
            else:
                print("Account not found.")

        elif choice == "2":
            account_number = input("Enter account number: ")

            if account_number in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")

            if account_number in accounts:
                accounts[account_number].check_balance()
            else:
                print("Account not found.")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()