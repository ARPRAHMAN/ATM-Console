from cardHolder import cardHolder

def print_menu():
    ##Print options to the user
    print("Press any of the following options....")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")
def deposit(cardHolder):
    try:
       deposit = float(input("How much TK would you like to deposit: "))
       cardHolder.set_balance(cardHolder.get_balance() + deposit)
       print("Thank you for your deposit. Your New Balance is: ",str(cardHolder.get_balance()))
    except:
       print("Invalid Input") 

def Withdraw(cardHolder):
    try:
        Withdraw = float(input("How much taka would you like to withdraw: "))
        ##check if user has enough money
        if(cardHolder.get_balance() < Withdraw):
            print("SORRY , Insufficient balance :(")
        else:
            cardHolder.set_balance(cardHolder.get_balance()-Withdraw)
            print(" You are good to go, THANK YOU!")
    except:
        print("Invalid Input.")
def check_balance(cardHolder):
    print("Current Balance: ",cardHolder.get_balance())

if __name__=="__main__":
    current_user = cardHolder("","","","")

    ##create a repo of cardholders
    list_of_cardHolders = []
    list_of_cardHolders.append(cardHolder("1112220",1111,"Arifur","Rahman",10000.11))
    list_of_cardHolders.append(cardHolder("1112221",2222,"Mr","Enzo",1000.01))
    list_of_cardHolders.append(cardHolder("1112222",3333,"Mr","Spoidy",6000.90))
    list_of_cardHolders.append(cardHolder("1112223",4444,"Mr","Alpha",500.99))
    list_of_cardHolders.append(cardHolder("1112224",5555,"Mr","Beluga",999.89))
    ##prompt user for debit card number
    debitCardNum =""
    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            ##check againt repo
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                    print("Card number not recongnized. Please try again.")
        except:
            print("Card number not recongnized. Please try again.")

## promt for pin
while True:
    try:
        userPin = int(input("Please enter your PIN: ").strip())
        if(current_user.get_pin() == userPin):
            break
        else:
            print("Invalid PIN. Please try again.")
            
    except:
        print("Invalid PIN. Pleaser try again")
         

