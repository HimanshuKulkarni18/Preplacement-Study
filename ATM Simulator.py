#ATM Simulator

class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def check_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def check_balance(self):
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self):
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self):
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def menu(self):
        if not self.check_pin():
            print("Incorrect PIN. Access denied.")
            return

        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you for using ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


atm = ATM(pin="1234", balance=5000)
atm.menu()