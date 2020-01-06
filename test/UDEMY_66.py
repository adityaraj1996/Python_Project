class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance



    def deposit(self, dep_amt):
        self.balance += dep_amt
        print("Hey {}, the deposit is successful, the updated balance is {} ".format(self.owner, self.balance))

    def withdraw(self, with_amt):
        if with_amt > self.balance:
            print("sorry {}, insufficient balance".format(self.owner))
        else:
            self.balance -= with_amt
            print("Hey {}, withdrawal is successful, the updated balance is {} ".format(self.owner, self.balance))


    def __str__(self):
         return ("owner: {} \nbalance : {} ".format(self.owner,self.balance))


New_Account1 = Account('Jose', 10000)
New_Account2 = Account('Pit', 20000)

New_Account1.deposit(1000)
New_Account2.withdraw(2000)
print(New_Account1)