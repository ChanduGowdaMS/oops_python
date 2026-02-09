class BankAccount:
    account_holder_name="unknown"
    _account_type="Savings"


    def __init__(self,pin):
        self.__balance=0
        self.__pin=pin

    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("Pin setted")
   
    def get_pin(self):
        return self.__pin


    def verify_pin(self,new_pin):
        return new_pin==self.__pin


    def get_balance(self,pin):
        if self.verify_pin(pin):
            return self.__balance
        else:
            return "incorrect pin."
   
    def set_balance(self,pin,amount):
        if self.verify_pin(pin):
            self.__balance+=amount
            print("The updated balance: ",self.__balance)
        else:
            print("Enter valid PIN")




BA=BankAccount(1234)
BA.account_holder_name="Raj"
print("The account holder name is: ",BA.account_holder_name)
print("The account pin is:",BA.get_pin())
BA.set_pin(5678)
print("The account new pin is:",BA.get_pin())
print("The old balance is: ",BA.get_balance(5678))
BA.set_balance(1234,1000)
BA.set_balance(5678,1000)
