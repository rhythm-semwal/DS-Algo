"""
Entities:
 - user
 - group
 - expense
"""
"""
Relationships:
1) User m ----participates in -----n  expense
2) User m ----member of -----n  group
3) expense * ----- 0/1 group - because it is not mandatory for a expense to belong to a group
4) User 1----admin of ----* group
"""

from abc import ABC
from typing import TypeVar, Generic


class UserNameException(Exception):
    def UserNameException(self, message):
        super().__init__(message)


class Auditable(ABC):
    def __init__(self, id):
        self.__id = id
        self.__created_date = None
        self.__modified_date = None


class User(Auditable):
    def __init__(self):
        self.__name = ""
        self.__email = ""
        self.__phone_number = None
        self.__password = ""

        self.__expenses = []  # particular user all expenses
        self.__groups = []  # list of all the groups the user is part of

    def get_username(self):
        return self.__name

    def set_username(self, name):
        self.__name = name

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_user_id(self):
        return self.__id

    def get_user_email(self):
        return self.__email

    def get_user_phone_number(self):
        return self.__phone_number

    def get_total_amount_owed(self):
        pass


class Group(Auditable):
    def __init__(self, group_name):
        self.__group_name = group_name
        self.__admin = ""  # user object will be the admin
        self.__members = []  # user will be the members
        self.__expenses = []  # list of all the expenses


class Expense(Auditable):
    def __init__(self, description, total_amount):
        self.__description = description
        self.__participants = []  # list of user
        self.__total_amount = total_amount
        self.__paid_amount = {}  # {user: amount}
        self.__owed_amount = {}  # {user: amount}
        self.__is_settled = False


"""
User Repository.This will contain the operations related to a user
"""

T = TypeVar('T')
class CommonRepositpory(Generic[T]):
    def find_user_by_id(self, T):
        pass

    def create_new_user(self, T):
        pass

    def update_user(self, T):
        pass

    def save(self, T):
        pass

    def delete(self, T):
        pass


class UserRepository(CommonRepositpory):
    def find_user_by_username(self, user):
        pass


class ExpenseRepository(CommonRepositpory):
    pass


class GroupRepository(CommonRepositpory):
     pass


"""
User DTO(Data Transfer Object)
"""


class UserDTO:
    # when a new user puts in the detail it will be stored in this object
    def __init__(self):
        self.name = ""
        self.email = ""
        self.phone_number = None
        self.password = ""

"""
authentication_context
"""


class AuthenticationContext:
    def currently_logged_in_user(self):
        pass


"""
Payment strategy
"""


class PaymentStrategy(ABC):
    def calculate_paid_amounts(self, expense):
        pass


class ExactAmountPaymentStrategy(PaymentStrategy):
    def calculate_paid_amounts(self, expense):
        pass

class IPaidPaymentStrategy(PaymentStrategy):
    def calculate_paid_amounts(self, expense):
        pass


"""
Split Strategy
"""

class SplitStrategy(ABC):
    def calculate_owed_amounts(self, expense):
        pass


class EqualSplitStrategy(SplitStrategy):
    def calculate_owed_amounts(self, expense):
        pass

class PercentageSplitStrategy(SplitStrategy):
    def calculate_owed_amounts(self, expense):
        pass

"""
User controller
"""


class UserController:
    def __init__(self):
        self.user_repository = UserRepository()

    def register(self,  user_dto):
        # user_dto object will contain all the details like name, password
        new_user = User()
        # add details and create new user. user id will be assigned here

        # adding validation, if username already exist or not
        if self.user_repository.find_user_by_username(user_dto.name):
            raise UserNameException("user name already exist")
        new_user.set_username(user_dto.name)

        # check for password length and then hash the password

    def update_profile(self, authentication_context, user_dto):
        pass

    def change_password(self, authentication_context, old_password, new_password):
        # the current logged in user should only be able to change its own password
        logged_in_user = authentication_context.get_current_user_details()
        # check if the old password is correct and if correct change the passowrd else raise exception

    def get_my_total_owed(self, authentication_context):
        # calculate and return total amount owed by the user
        # get user and call the user class to calculate the amount
        pass

    def get_expense_history(self, authentication_context):
        pass

    def get_my_groups(self, authentication_context):
        pass


class ExpenseController:
    def create_new_expense_in_group(self, authentication_context):
        # get the user from authentication_context


    def create_new_expense_with_users(self, authentication_context, participant_id,
                                      payment_strategy, split_strategy, description, created_date):
        # get the user from authentication_context
        # get the list of participants in the expense
        # add participants in a list
        # call the split strategy based on the input
        # call the payment strategy based on the input
        # at last create a new expense

        pass
