from enum import  Enum
from abc import ABC, abstractmethod


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country


class Customer:
    """
    “Customer” encapsulates the ATM user, “Card” the ATM card, and “Account” can be of two types: checking and savings:
    """
    def __init__(self, name, address, contact_number, email):
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.email = email
        self.__card = Card()
        self.__account = Account

    def make_transaction(self):
        pass


class Card:
    def __init__(self, number, customer_name, expiry_date, pin):
        self.__card_number = number
        self.__customer_name = customer_name
        self.__expiry_date = expiry_date
        self.__pin = pin


class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__available_balance = 0.0
        self.__total_balance = 0.0

    def get_available_balance(self):
        return self.__available_balance


class SavingAccount(Account):
    pass


class CheckingAccount(Account):
    pass


# ****************************************************************************************************************

class Bank:
    def __init__(self, name, bank_code):
        self.__bank_name = name
        self.__bank_code = bank_code

    def get_bank_code(self):
        return self.__bank_code

    def add_atm(self):
        pass


class ATM:
    def __init__(self, id, location):
        self.__id = id
        self.__location = location
        self.__bank = Bank()
        self.__cash_dispenser = CashDispenser()
        self.__keypad = Keypad()
        self.__screen = Screen()
        self.__printer = Printer()
        # self.__cash_deposit = CashDeposit()
        # self.__check_deposit = CheckDeposit()

    def authenticate_user(self):
        pass


class CashDispenser:
    def __init__(self):
        self.__hundred_rs_notes = 0
        self.__five_hundred_rs_notes = 0
        self.two_thousand_rs_notes = 0

    def dispense_cash(self):
        pass


class Screen:
    def show_message(self):
        pass

    def get_input(self):
        pass


class Keypad:
    def get_input(self):
        pass


class Printer:
    def print_receipt(self, transaction):
        pass


# class CashDeposit:
#     pass
#
#
# class CheckDeposit:
#     pass


class DepositSlot(ABC):
    def __init__(self):
        self.__total_amount = 0.0

    def get_total_amount(self):
        return self.__total_amount


class CashDepositSlot(DepositSlot):
    def amount_deposit(self):
        pass


class CheckDepositSlot(DepositSlot):
    def check_deposit(self):
        pass


"""
Transaction and types of transactions
"""


class Transactions(ABC):
    def __init__(self, id, time, status):
        self.__transaction_id = id
        self.__transaction_time = time
        self.__transaction_status = status

    def make_transaction(self):
        pass


class BalanceEnquiry(Transactions):
    def __init__(self, account_number):
        super().__init__()
        self.__account_number = account_number

    def get_account_number(self):
        return self.__account_number


class Withdraw(Transactions):
    def __init__(self, amount):
        super().__init__()
        self.__withdraw_amount = amount

    def get_withdraw_amount(self):
        return self.__withdraw_amount


class Deposit(Transactions):
    def __init__(self, amount):
        super().__init__()
        self.__amount = amount

    def get_deposit_amount(self):
        return self.__amount


class CashDeposit(Deposit):
    def __init__(self, deposit_amount):
        super().__init__()
        self.__deposit_amount = deposit_amount


class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        super().__init__()
        self.__check_number = check_number
        self.__bank_code = bank_code

    def get_check_number(self):
        return self.__check_number


class TransferFund(Transactions):
    def __init__(self, destination_account_number, amount):
        super().__init__()
        self.__destination_account_number = destination_account_number
        self.__amount = amount