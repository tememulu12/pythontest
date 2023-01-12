# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import (
#     Column, Integer, String, Float, ForeignKey, create_engine)
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm import sessionmaker
#
# from sqlalchemy.orm import relationship
#
# engine = create_engine('sqlite:///bankomat.db')
# Base = declarative_base()
#
#
# class Bankomat(Base):
#     __tablename__ = 'bankomat'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     account_num = Column(Integer)
#     balance = Column(Float)
class Bankomat:
    def __init__(self, name, account_num: int, balance: float):
        self.name= name
        self.account_num= account_num
        self.balance =balance

    def deposit(self, amount):
        self.amount = amount

        if self.balance:
            return f"{self.name} deposit {self.balance + self.amount}zl"
        else:
            return self.amount

    def withdraw(self, amount):
        self._amount = amount
        if self.balance:
            return f"{self.name} withdraw {self.balance - self.amount}zl"
        else:
            return 0

    def available_balance(self):
        return f"Available balance in this account number {self.account_num}: {self.balance}zl"

    def transaction(self):
        while True:
            menu = int(input("Enter 1 for deposit,2 for withdraw=, 3 for check your available balance="))
            if menu in [1, 2, 3]:
                if menu == 1:
                    print("Deposit!")
                    amount = float(input("Amount of deposit: "))
                    print(self.deposit(amount=amount))
                elif menu == 2:
                    print("Withdraw!")
                    amount = float(input("Amount of withdraw: "))
                    print(self.withdraw(amount=amount))
                elif menu == 3:
                    print("Available balance!")
                    print(self.available_balance())
                stop_transactions = input("Do you want stop transaction? write 'q'= ")
                if stop_transactions == 'q':
                    break
            else:
                print("invalid input")


bankomat = Bankomat('Mulu', 239450, 2000.0)
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()
# bankomat1 = Bankomat(name='Mulu', account_num=239450, balance=2000.0)
# bankomat2 = Bankomat(name='Pawel', account_num=2393350, balance=40000.0)
# bankomat3 = Bankomat(name='Faxi', account_num=239330, balance=200033.0)
# bankomat4 = Bankomat(name='Jan', account_num=239453, balance=2333.0)
# bankomat5 = Bankomat(name='Adam', account_num=239430, balance=20333.0)
# session.add_all([bankomat1, bankomat2, bankomat3, bankomat4, bankomat5])
# session.commit()

bankomat.transaction()
