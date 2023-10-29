from enum import Enum
from abc import ABC
from datetime import datetime
"""
Constants
"""


class BookingStatus(Enum):
    REQUESTED, PENDING, CONFIRMED, CHECKED_IN, CANCELED, ABANDONED = 1, 2, 3, 4, 5, 6


class SeatType(Enum):
    REGULAR, PREMIUM, ACCESSIBLE, SHIPPED, EMERGENCY_EXIT, OTHER = 1, 2, 3, 4, 5, 6


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class PaymentStatus(Enum):
    UNPAID, PENDING, COMPLETED, FILLED, DECLINED, CANCELLED, ABANDONED, SETTLING, SETTLED, REFUNDED = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street_address = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


"""
Account, Customer, Admin, FrontDeskOfficer, and Guest: 
These classes represent the different people that interact with our system:
"""


class Account:
    def __init__(self, username, password, status=AccountStatus.ACTIVE):
        self.__username = username
        self.__password = password
        self.__status = status

    def reset_password(self):
        pass


class Person(ABC):
    def __init__(self, name, address, phone, email):
        self.__name = name
        self.__address= address
        self.__phone = phone
        self.__email = email


class Customer(Person):
    def __init__(self, name, address, phone, email):
        super(Customer, self).__init__(name,address, phone, email )

    def make_booking(self):
        pass

    def get_bookings(self):
        pass


class Admin(Person):
    def add_new_movies(self, movie):
        pass

    def add_show(self, movie, show):
        pass

    def block_customer(self, customer):
        pass


class FrontDeskOfficer(Person):
    def create_booking(self, booking):
        pass


class Guest:
    def register_account(self):
        pass


"""
Show and Movie: A movie will have many shows:
"""


class Show:
    def __init__(self, id, played_at, movie, start_time, end_time):
        self.__show_id = id
        self.__created_on = datetime.date.today()
        self.__start_time = start_time
        self.__end_time = end_time
        self.__played_at = played_at
        self.__movie = movie


class Movie:
    def __init__(self, title, description, duration_in_mins, language, release_date, country, genre, added_by):
        self.__title = title
        self.__description = description
        self.__duration_in_mins = duration_in_mins
        self.__language = language
        self.__release_date = release_date
        self.__country = country
        self.__genre = genre
        self.__movie_added_by = added_by

        self.__shows = []

    def get_shows(self):
        None


"""

"""


class City:
    def __init__(self, name, state, zip_code):
        self.__name = name
        self.__state = state
        self.__zip_code = zip_code


class Cinema:
    def __init__(self, name, total_cinema_halls, address, halls):
        self.__name = name
        self.__total_cinema_halls = total_cinema_halls
        self.__location = address

        self.__halls = halls


class CinemaHall:
    def __init__(self, name, total_seats, seat_types, shows):
        self.__name = name
        self.__total_seats = total_seats

        self.__seat_types = seat_types
        self.__shows = shows


class CinemaHallSeat:
    def __init__(self, id, seat_type):
        self.__hall_seat_id = id
        self.__seat_type = seat_type


"""
Booking, ShowSeat, and Payment: Customers will reserve seats with a booking and make a payment:
"""


class Booking:
    def __init__(self, booking_number, number_of_seats, status, show, show_seats, payment):
        self.__booking_number = booking_number
        self.__number_of_seats = number_of_seats
        self.__created_on = datetime.date.today()
        self.__status = status
        self.__show = show
        self.__seats = show_seats
        self.__payment = payment

    def make_payment(self):
        pass

    def make_new_booking(self):
        pass

    def cancel_booking(self):
        pass

    def select_seats(self):
        pass

    def send_notification(self):
        pass


class ShowSeats(CinemaHallSeat):
    def __init__(self, id, is_reserved, price):
        self.__show_seat_id = id
        self.__is_reserved = is_reserved
        self.__price = price


class Payment(ABC):
    def __init__(self, amount, transaction_id, payment_status):
        self.__amount = amount
        self.__created_on = datetime.date.today()
        self.__transaction_id = transaction_id
        self.__status = payment_status


class CreditCardPayment(Payment):
    pass


class CashPayment(Payment):
    pass


"""
Search interface and Catalog: Catalog will implement Search to facilitate searching of products.
"""


class Search(ABC):
    def search_by_title(self, title):
        pass

    def search_by_language(self, language):
        pass

    def search_by_genre(self, genre):
        pass

    def search_by_release_date(self, rel_date):
        pass

    def search_by_city(self, city_name):
        pass


class Catalog(Search):
    def __init__(self):
        self.__movie_titles = {}
        self.__movie_languages = {}
        self.__movie_genres = {}
        self.__movie_release_dates = {}
        self.__movie_cities = {}

    def search_by_title(self, title):
        return self.__movie_titles.get(title)

    def search_by_language(self, language):
        return self.__movie_languages.get(language)

    def search_by_city(self, city_name):
        return self.__movie_cities.get(city_name)


"""
How to handle concurrency; such that no two users are able to book the same seat?

We can use transactions in SQL databases to avoid any clashes. For example, 
if we are using SQL server we can utilize Transaction Isolation Levels to lock the rows before we update them. 
Note: within a transaction, if we read rows we get a write-lock on them so that they can’t be updated by anyone else. 
Here is the sample code:

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
 
BEGIN TRANSACTION;
 
    -- Suppose we intend to reserve three seats (IDs: 54, 55, 56) for ShowID=99 
    Select * From ShowSeat where ShowID=99 && ShowSeatID in (54, 55, 56) && isReserved=0 
 
    -- if the number of rows returned by the above statement is NOT three, we can return failure to the user.
    update ShowSeat table...
    update Booking table ...
 
COMMIT TRANSACTION;
"""