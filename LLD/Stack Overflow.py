from enum import Enum
from abc import ABC
from datetime import datetime

class QuestionStatus(Enum):
    OPEN, CLOSED, ON_HOLD, DELETED = 1, 2, 3, 4


class QuestionClosingRemark(Enum):
    DUPLICATE, OFF_TOPIC, TOO_BROAD, NOT_CONSTRUCTIVE, NOT_A_REAL_QUESTION, PRIMARILY_OPINION_BASED = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, BLOCKED = 1, 2, 3, 4, 5


"""
Account, Member, Admin, and Moderator: These classes represent the different people that interact with our system:
"""


class Account:
    def __init__(self, id, password, name, address, email, phone, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone =  phone
        self.__status = status
        self.__reputation = 0

    def get_reputation(self):
        return self.__reputation

    def reset_password(self):
        pass


class Guest:
    def create_account(self):
        pass


class Member:
    def __init__(self, account):
        self.__account = account
        self.badges = []

    def get_reputation(self):
        return self.__account.get_reputation()

    def create_question(self, question):
        pass

    def create_tag(self, tag):
        pass


class Admin(Member):
    def block_member(self, member):
        pass

    def unblock_member(self, member):
        pass


"""
Question, Comment and Answer: Members can ask questions, as well as add an answer to any question. 
All members can add comments to all open questions or answers:
"""


class Search(ABC):
    def search(self, query):
        pass


class Question(Search):
    def __init__(self, title, description, bounty, asking_member):
        self.__title = title
        self.__description = description
        self.__view_count = 0
        self.__vote_count = 0
        self.__creation_time = datetime.now()
        self.__update_time = datetime.now()
        self.__status = QuestionStatus.OPEN
        self.__closing_remark = QuestionClosingRemark.DUPLICATE
        self.__bounty = bounty
        self.__asking_member = asking_member
        self.__photos = []
        self.__comments = []
        self.__answers = []

    def add_comment(self, comment):
        pass

    def add_answer(self, answer):
        pass

    def close(self):
        pass

    def search(self, query):
        pass


class Comment:
    def __init__(self, text, member):
        self.__comment = text
        self.__creation_time = datetime.now()
        self.__flag_count = 0
        self.__vote_count = 0
        self.__asking_member = member

    def increment_vote_count(self):
        pass


class Answer:
    def __init__(self, text, member):
        self.__answer = text
        self.__answered_by = member
        self.__answer_date = datetime.now()
        self.__vote_count = 0
        self.__flag_count = 0

    def increment_vote_count(self):
        pass


"""
Badge, Tag, and Notification: Members have badges, questions have tags and notifications:
"""


class Badge:
    def __init__(self, name, description):
        self.__name = name
        self.__description = description


class Tag:
    def __init__(self, name, description):
        self.__tag_name = name
        self.__description = description


class Notification:
    def __init__(self, send_to, content):
        self.__receiver = send_to
        self.__content = content
        self.__date = datetime.now()

    def send_notification(self):
        pass


"""
Photo and Bounty: Members can put bounties on questions. Answers and Questions can have multiple photos:
"""


class Bounty:
    def __init__(self, reputation, expiry):
        self.__reputation = reputation
        self.__expiry = expiry

    def modify_reputation(self):
        pass
