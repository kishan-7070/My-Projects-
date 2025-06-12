#ATM Project
class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
    def menu(self):
        user_input=input("""
        Hi How can i help you?
        1.press 1 to create pin
        2.press 2 to change pin
        3.press 3 to check balance
        4.press 4 to withdrawl
        5. Anything else to exit : """)
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
        elif user_input=='3':
            self.check_balance()
        elif user_input=='4':
            self.withdraw()
        else:
            exit()
    def create_pin(self):
        user_pin=int(input("Enter pin: "))
        self.pin=user_pin
        user_balance=int(input("Enter balance: "))
        self.balance=user_balance
        print('pin created successfully')
        self.menu()
    def change_pin(self):
        old_pin=int(input("Enter old pin: "))
        if old_pin == self.pin:
            new_pin=int(input("Enter new pin: "))
            self.pin=new_pin
            print("Pin changed Successfully !")
        else:
            print("Wrong password")
            self.menu()
    def check_balance(self):
        user_pin=int(input("Enter your pin: "))
        if user_pin==self.pin:
            print("your balance is: ",self.balance)
    def withdraw(self):
        user_pin=int(input("Enter your pin: "))
        if user_pin==self.pin:
            amount=int(input('Enter amount to withdraw: '))
            if amount<=self.balance:
                self.balance -= amount
                print("left amount is: ",self.balance)
                print("Get your money : ")
                print("Thanks")
                self.menu()
            else:
                print('insufficient balance ')
                self.menu()
        else:
            print('chor')
obj=Atm()