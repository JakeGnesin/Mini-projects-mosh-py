# balance = 0


# def display_menu():
#     print('Welcome to the ATM')

#     OPTIONS = [
#         '1. Check Balance',
#         '2. Deposit',
#         '3. Withdraw',
#         '4. Exit'
#     ]

#     for option in OPTIONS:
#         print(option)


# def check_balance(selection):
#     if selection == 1:
#         print(f'You have: ${balance}')


# def new_deposit(selection):
#     while True:
#         if selection == 2:
#             deposit = float(input('Enter a deposit amount: '))
#             if deposit <= 0 or not float:
#                 print('Invalid deposit amount')
#                 continue
#             else:
#                 balance += deposit
#                 print(f'Succsseful deposit of ${deposit} added to balance')
#                 break


# def new_withdraw(selection):
#     while True:
#         if selection == 3:
#             withdrawal = float(input('Enter an amount to withdraw: $ '))
#             if withdrawal <= 0 or withdrawal > balance:
#                 print('Invalid withdrawal amount')
#                 continue
#             else:
#                 balance - + withdrawal
#                 print(
#                     f'Succsseful withrawal of ${withdrawal} taken from your balance')
#                 break


# def exit_atm(selection):
#     while True:
#         if selection == 4:
#             print('Goodbye!')
#             break


# def main(OPTIONS):
#     display_menu(OPTIONS)

#     while True:
#         selection = int(input('Select a menu option'))
#         if selection not in OPTIONS:
#             print('Invalid option')
#             continue
#         else:
#             break

#     while True:
#         check_balance(balance, selection)
#         new_deposit(balance, selection)
#         new_withdraw(balance, selection)
#         exit_atm(balance, selection)


# if __name__ == '__main__':
#     main()
# ---------------------------------------


# proper code without using class ------

# balance = 0

# def display_menu():
#     print('Welcome to the ATM')
#     print('1. Check Balance')
#     print('2. Deposit')
#     print('3. Withdraw')
#     print('4. Exit')

# def check_balance():
#     print(f'You have: ${balance:.2f}')

# def deposit():
#     global balance
#     while True:
#         try:
#             amount = float(input('Enter a deposit amount: $'))
#             if amount <= 0:
#                 print('Invalid deposit amount. Please enter a positive number.')
#                 continue
#             balance += amount
#             print(f'Successful deposit of ${amount:.2f} added to balance')
#             return
#         except ValueError:
#             print('Please enter a valid number')

# def withdraw():
#     global balance
#     while True:
#         try:
#             amount = float(input('Enter an amount to withdraw: $'))
#             if amount <= 0:
#                 print('Invalid withdrawal amount. Please enter a positive number.')
#                 continue
#             if amount > balance:
#                 print('Insufficient funds')
#                 continue
#             balance -= amount
#             print(f'Successful withdrawal of ${amount:.2f}. New balance: ${balance:.2f}')
#             return
#         except ValueError:
#             print('Please enter a valid number')

# def main():
#     while True:
#         display_menu()
#         try:
#             selection = int(input('Select a menu option (1-4): '))
#             if selection == 1:
#                 check_balance()
#             elif selection == 2:
#                 deposit()
#             elif selection == 3:
#                 withdraw()
#             elif selection == 4:
#                 print('Goodbye!')
#                 break
#             else:
#                 print('Invalid option. Please select 1-4.')
#         except ValueError:
#             print('Please enter a valid number')

# if __name__ == '__main__':
#     main()
# ---------------------------


# proper code using class....NO REFACTORING USED
# class ATM:
#     def __init__(self):
#         self.balance = 1000  # Initial balance
#         self.pin = "1234"    # Default PIN

#     def _verify_pin(self, entered_pin):
#         return self.pin == entered_pin

#     def _execute_if_valid(self, entered_pin, action, *args):
#         if self._verify_pin(entered_pin):
#             return action(*args)
#         print("Incorrect PIN")
#         return False

#     def check_balance(self, entered_pin):
#         def show_balance():
#             print(f"Your current balance is: ${self.balance}")
#         self._execute_if_valid(entered_pin, show_balance)

#     def deposit(self, amount, entered_pin):
#         def do_deposit(amt):
#             if amt > 0:
#                 self.balance += amt
#                 print(f"Successfully deposited ${amt}")
#                 print(f"New balance: ${self.balance}")
#                 return True
#             print("Deposit amount must be positive")
#             return False
#         self._execute_if_valid(entered_pin, do_deposit, amount)

#     def withdraw(self, amount, entered_pin):
#         def do_withdraw(amt):
#             if amt > 0:
#                 if amt <= self.balance:
#                     self.balance -= amt
#                     print(f"Successfully withdrew ${amt}")
#                     print(f"New balance: ${self.balance}")
#                     return True
#                 print("Insufficient funds")
#                 return False
#             print("Withdrawal amount must be positive")
#             return False
#         self._execute_if_valid(entered_pin, do_withdraw, amount)

#     def change_pin(self, old_pin, new_pin):
#         def update_pin(new_p):
#             self.pin = new_p
#             print("PIN successfully changed")
#             return True
#         self._execute_if_valid(old_pin, update_pin, new_pin)


# def main():
#     atm = ATM()
#     menu = {
#         "1": ("Check Balance", atm.check_balance),
#         "2": ("Deposit", lambda p: atm.deposit(float(input("Enter amount: ")), p)),
#         "3": ("Withdraw", lambda p: atm.withdraw(float(input("Enter amount: ")), p)),
#         "4": ("Change PIN", lambda p: atm.change_pin(p, input("Enter new PIN: "))),
#     }

#     while True:
#         print("\n=== ATM Menu ===")
#         for k, (desc, _) in menu.items():
#             print(f"{k}. {desc}")
#         print("5. Exit")

#         choice = input("Enter your choice (1-5): ")
#         if choice == "5":
#             print("Thank you for using our ATM. Goodbye!")
#             break

#         if choice in menu:
#             pin = input("Enter your PIN: ")
#             menu[choice][1](pin)
#         else:
#             print("Invalid choice")


# if __name__ == "__main__":
#     main()


# ///-----------------------///


# new program with refactoring and OOP:

class ATM:
    def __init__(self):
        self._balance = 1000  # Initial balance
        self._pin = "1234"    # Default PIN

    def _verify_pin(self, entered_pin):
        if self._pin != entered_pin:
            raise ValueError("Incorrect PIN")

    def get_balance(self, pin):
        self._verify_pin(pin)
        return self._balance

    def deposit(self, amount, pin):
        self._verify_pin(pin)
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount, pin):
        self._verify_pin(pin)
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    def change_pin(self, old_pin, new_pin):
        self._verify_pin(old_pin)
        self._pin = new_pin
        return True

    @staticmethod
    def get_number(prompt):
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            raise ValueError("Please enter a valid number")


class ATMController:
    def __init__(self):
        self.atm = ATM()
        self.menu = {
            "1": ("Check Balance", self._check_balance),
            "2": ("Deposit", self._deposit),
            "3": ("Withdraw", self._withdraw),
            "4": ("Change PIN", self._change_pin),
        }

    def _display_menu(self):
        print("\n=== ATM Menu ===")
        for key, (desc, _) in self.menu.items():
            print(f"{key}. {desc}")
        print("5. Exit")

    def _get_pin(self):
        return input("Enter your PIN: ")

    def _check_balance(self, pin):
        balance = self.atm.get_balance(pin)
        print(f"Your current balance is: ${balance}")

    def _deposit(self, pin):
        amount = self.atm.get_number("Enter amount to deposit: ")
        new_balance = self.atm.deposit(amount, pin)
        print(f"Deposited ${amount}. New balance: ${new_balance}")

    def _withdraw(self, pin):
        amount = self.atm.get_number("Enter amount to withdraw: ")
        new_balance = self.atm.withdraw(amount, pin)
        print(f"Withdrew ${amount}. New balance: ${new_balance}")

    def _change_pin(self, pin):
        new_pin = input("Enter new PIN: ")
        self.atm.change_pin(pin, new_pin)
        print("PIN successfully changed")

    def run(self):
        while True:
            self._display_menu()
            choice = input("Enter your choice (1-5): ")

            if choice == "5":
                print("Thank you for using our ATM. Goodbye!")
                break

            if choice in self.menu:
                try:
                    pin = self._get_pin()
                    self.menu[choice][1](pin)
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid choice")


if __name__ == "__main__":
    controller = ATMController()
    controller.run()
