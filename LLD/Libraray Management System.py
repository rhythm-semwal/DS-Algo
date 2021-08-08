"""
Constants
"""
from enum import Enum
from abc import ABC
import datetime


class BookFormat(Enum):
    HARDCOVER, PAPERBACK, AUDIO_BOOK, EBOOK, NEWSPAPER, MAGAZINE, JOURNAL = 1, 2, 3, 4, 5, 6, 7


class BookStatus(Enum):
    AVAILABLE, RESERVED, LOANED, LOST = 1, 2, 3, 4


class ReservationStatus(Enum):
    WAITING, PENDING, COMPLETED,  CANCELED, NONE = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELED, BLACKLISTED, NONE = 1, 2, 3, 4, 5


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country


class Person(ABC):
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone


class Constants:
    def __init__(self):
        self.MAX_BOOKS_ISSUED_TO_A_USER = 5
        self.MAX_LENDING_DAYS = 10


"""
Account, Member, and Librarian: These classes represent various people that interact with our system:
"""


class Account(ABC):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        self.__id = id
        self.__password = password
        self.__person = Person(person)
        self.__status = status

    def reset_password(self):
        pass


class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super(Librarian, self).__init__(id, password, person, status)

    def add_book(self, book):
        pass

    def remove_book(self, book):
        pass

    def add_new_member(self, member):
        pass

    def block_member(self, member):
        pass

    def unblock_member(self, member):
        pass


class Member(Account):

    def __init__(self, id, password, person, status=AccountStatus.ACTIVE):
        super(Member, self).__init__(id, password, person, status)
        self.__date_of_membership = datetime.datetime.date.today()
        self.__total_books_checked_out = 0

    def get_member_id(self):
        return self.__id

    def get_total_books_checked_out(self):
        return self.__total_books_checked_out

    def increment_total_checked_out_books(self):
        self.__total_books_checked_out += 1

    def reserve_book(self, book):
        pass

    def renew_book_item(self, book):
        pass

    def checkout_new_book(self, book):
        if self.get_total_books_checked_out() >= Constants().MAX_BOOKS_ISSUED_TO_A_USER:
            print("User has already checked out the max limit of books")
            return False
        book_reservation = BookReservation().fetch_reservation_details(book.get_barcode())

        if book_reservation.get_memebr_id() != self.id:
            print("book is reserved by another user")
            return False

        else:
            book_reservation.update_status(ReservationStatus.COMPLETED)

        self.increment_total_checked_out_books()
        return True

    def check_for_fine(self, book_item_barcode):
        book_lending = BookLending.fetch_lending_details(book_item_barcode)
        due_date = book_lending.get_due_date()

        today = datetime.datetime.today()
        if today > due_date:
            diff = today - due_date
            diff_days = diff.days
            Fine.collect_fine(self.get_member_id(), diff_days)

    def return_book_item(self, book_item):
        # check for fine
        # collect fine if any
        # check for book reservation, if any reserve it else make book available and send notification
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())

        if book_reservation.status == BookStatus.RESERVED:
            book_item.update_status(BookStatus.RESERVED)
        else:
            book_item.update_status(BookStatus.AVAILABLE)
            book_reservation.send_notification()

    def renew_book_item(self, book_item):
        self.check_for_fine(book_item)
        book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())

        if book_reservation == BookStatus.RESERVED and book_reservation.get_member_id() != self.get_member_id():
            print("Cannot renew book already reserved")
            book_reservation.update_status(ReservationStatus.COMPLETED)
            book_reservation.send_notification()

        else:
            book_reservation.update_status(ReservationStatus.COMPLETED)
            BookLending.lend_book(book_item.get_barcode(), self.get_member_id())
            book_item.update_due_date(datetime.datetime.now().AddDays(Constants().MAX_LENDING_DAYS))

        return True


"""
BookReservation, BookLending, and Fine: These classes represent a book reservation, 
lending, and fine collection, respectively.
"""


class BookReservation:
    def __init__(self, date, status, book_item_barcode, member_id):
        self.__date = date
        self.__status = status
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def fetch_reservation_details(self, barcode):
        pass

    def send_notification(self):
        pass

    def get_member_id(self):
        return self.__member_id


class BookLending:
    def __init__(self, creation_date, due_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__due_date = due_date
        self.__return_date = None
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def get_due_date(self):
        return self.__due_date

    def lend_book(self, barcode, member_id):
        pass

    def fetch_lending_details(self, barcode):
        return


class Fine:
    def __init__(self, creation_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def collect_fine(self):
        pass


"""
BookItem: Encapsulating a book item, this class will be responsible for processing the reservation, 
return, and renewal of a book item.
"""


class Book(ABC):
    def __init__(self, ISBN, title, subject, publisher, language, number_of_pages):
        self.__ISBN = ISBN
        self.__title = title
        self.__subject = subject
        self.__publisher = publisher
        self.__language = language
        self.__number_of_pages = number_of_pages
        self.__authors = []


class BookItem(Book):
    def __init__(self, barcode, is_reference_only, borrowed, due_date, price, book_format, status,
                 date_of_purchase, publication_date, placed_at):
        self.__barcode = barcode
        self.__is_reference_only = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__price = price
        self.__format = book_format
        self.__status = status
        self.__date_of_purchase = date_of_purchase
        self.__publication_date = publication_date
        self.__placed_at = placed_at

    def checkout(self, member_id):
        if self.__is_reference_only:
            print("Cannot loan")

        if BookLending.lend_book(self.__barcode, member_id):
            self.update_book_status(BookStatus.LOANED)

    def update_book_status(self, status):
        self.__status = status


class Rack:
    def __init__(self, number, location_identifier):
        self.__number = number
        self.__location_identifier = location_identifier


"""
Search interface and Catalog: The Catalog class will implement the Search interface to facilitate searching of books.
"""


class Search(ABC):
    def search_by_title(self, title):
        pass

    def search_by_author(self, author):
        pass

    def search_by_subject(self, subject):
        pass

    def search_by_publisher(self, publisher):
        pass


class Catalog(Search):
    def __init__(self):
        self.__book_titles = {}
        self.__book_authors = {}
        self.__book_subjects = {}
        self.__book_publishers = {}

    def search_by_title(self, title):
        return self.__book_titles.get(title,"Book Not present")

    def search_by_subject(self, subject):
        return self.__book_subjects.get(subject, "Book Not present")