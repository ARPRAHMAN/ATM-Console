class CardHolder:
    def __init__(self, card_num: str, pin: int, first_name: str, last_name: str, balance: float):
        self._card_num = card_num
        self._pin = pin
        self._first_name = first_name
        self._last_name = last_name
        self._balance = balance


    @property
    def card_num(self) -> str:
        return self._card_num


    @property
    def pin(self) -> int:
        return self._pin


    @property
    def first_name(self) -> str:
        return self._first_name


    @property
    def last_name(self) -> str:
        return self._last_name


    @property
    def balance(self) -> float:
        return self._balance


    def print_out(self) -> None:
        print("Card :", self.card_num)
        print("Pin :", self.pin)
        print("First Name :", self.first_name)
        print("Last Name :", self.last_name)
        print("Balance :", self.balance)


def print_menu() -> None:
    print("Press any of the following options....")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Create Account")
    print("5. Admin View")
    print("6. Exit")


def deposit(card_holder: CardHolder) -> None:
    try:
        deposit_amount = float(input("How much TK would you like to deposit: "))
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        card_holder._balance += deposit_amount
        print("Thank you for your deposit. Your New Balance is: ", str(card_holder.balance))
    except ValueError as e:
        print(e)


def withdraw(card_holder: CardHolder) -> None:
    try:
        withdraw_amount = float(input("How much taka would you like to withdraw: "))
        if withdraw_amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if card_holder.balance < withdraw_amount:
            raise ValueError("Insufficient balance.")
        card_holder._balance -= withdraw_amount
        print(" You are good to go, THANK YOU!")
    except ValueError as e:
        print(e)


def check_balance(card_holder: CardHolder) -> None:
    print("Current Balance: ", str(card_holder.balance))


def create_account(cardholders: list) -> None:
    card_num = input("Please enter your desired card number: ")
    if any(card._card_num == card_num for card in cardholders):
        print("Card number already exists. Please choose a different card number.")
        return
    pin = int(input("Please enter your desired pin: "))
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    balance = 0.0
    new_cardholder = CardHolder(card_num, pin, first_name, last_name, balance)
    cardholders.append(new_cardholder)
    print("Account created successfully!")


def admin_view(cardholders: list) -> None:
    for cardholder in cardholders:
        cardholder.print_out()
        print()


cardholders = [
    CardHolder("1112220", 1111, "Arifur", "Rahman", 10000.11),
    CardHolder("1112221", 2222, "Enzo", "Boss", 1000.01),
    CardHolder("1112222", 3333, "Spoidy", "Player", 6000.90),
    CardHolder("1112223", 4444, "Mark", "President", 500.99),
    CardHolder("1112224", 5555, "Jhon", "President", 999.89),
    CardHolder("1", 1, "Admin", "Admin", 0)
]

def main() -> None:
    while True:
        print("Welcome to the ATM!")
        print("1. Enter debit card")
        print("2. Create account")
        print("3. Admin access")
        try:
            option = int(input("Please choose an option: "))
            if option == 1:
                debit_card_num = input("Please insert your debit card: ")
                debit_pin = int(input("Please enter your PIN: "))
                debit_match = [card for card in cardholders if card.card_num == debit_card_num and card.pin == debit_pin]
                if len(debit_match) > 0:
                    current_user = debit_match[0]
                    break
                else:
                    print("Card number or PIN not recognized. Please try again.")
            elif option == 2:
                create_account(cardholders)
            elif option == 3:
                admin_card_num = input("Please enter your admin card number: ")
                admin_pin = int(input("Please enter your admin PIN: "))
                admin_match = [card for card in cardholders if card.card_num == admin_card_num and card.pin == admin_pin and card.first_name == "Admin"]
                if len(admin_match) > 0:
                    current_user = admin_match[0]
                    break
                else:
                    print("Admin card number or PIN not recognized. Please try again.")
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    while True:
        print_menu()
        try:
            option = int(input("Please choose an option: "))
            if option == 1:
                deposit(current_user)
            elif option == 2:
                withdraw(current_user)
            elif option == 3:
                check_balance(current_user)
            elif option == 4:
                create_account(cardholders)
            elif option == 5:
                if current_user.first_name == "Admin":
                    admin_view(cardholders)
                else:
                    print("Access denied. Please enter your admin credentials.")
            elif option == 6:
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

    print("Thank you. Have a nice day!")


if __name__ == "__main__":
    main()