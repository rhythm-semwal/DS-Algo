from abc import ABC, abstractmethod
from enum import Enum
"""
constants
"""

# read this from configuration or database. This can be configured
class VehicleType(Enum):
    CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5


class ParkingSpotType(Enum):
    HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class AccountStatus(Enum):
    ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
    ACTIVE, PAID, LOST = 1, 2, 3


class Address:
    def __init__(self, street, city, state, zip_code,country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country


class Person:
    def __init__(self, name, email, address, phone):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__phone = phone


"""
Defining persons who interact with the system
"""


class Employee:
    def __init__(self, user_name, password, person):
        self.__username = user_name
        self.__password = password
        self.__person = person

    def reset_password(self):
        pass


class Admin(Employee):
    def __init__(self, user_name, password, person):
        super().__init__(user_name, password, person)

    def add_parking_floor(self, floor):
        pass

    def add_parking_spot(self, spot, floor):
        pass

    def add_entrance(self, entrance):
        pass

    def add_exit(self, exit):
        pass

    def add_parking_display_board(self, floor_name, display_board):
        pass

    def add_customer_info_panel(self, floor_name, info_panel):
        pass


class ParkingAttendant(Employee):
    def __init__(self, user_name, password, person):
        super().__init__(user_name, password, person)

    def process_ticket(self, ticket_number):
        pass


"""
Definition of parking spots and its subclasses
"""

class Terminal(ABC):
    id, name
    pass


class EntryTerminal(Terminal):
    pass


class ExitTerminal(Terminal):
    pass

class IsSecured:
    pass


class SecuredTerminal(Terminal):
    pass


class ParkingSlot(ABC):
    def __init__(self, number, parking_spot_type):
        self.__number = number
        self.__parking_spot_type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    def is_free(self):
        pass

    def assign_vehicle(self, vehicle):
        self.__vehicle = vehicle
        free = False

    def remove_vehicle(self):
        self.__vehicle = None
        free = True


class HandicappedSpot(ParkingSlot):
    def __init__(self, number):
        super(HandicappedSpot, self).__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSlot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSlot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSlot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSlot):
    def __init__(self, number):
        super().__init__(number, ParkingSpotType.ELECTRIC)


# different parking slot allotment strategy. In case of VVIP or normal parking. This will return slots based on the
# spot type
"""
ParkingFloor: This class encapsulates a parking floor:
"""


class ParkingFloor:
    def __init__(self, name):
        self.__name = name
        self.__handicapped_spots = {}
        self.__compact_spots = {}
        self.__large_spots = {}
        self.__motorbike_spots = {}
        self.__electric_spots = {}
        self.__info_portals = {}
        self.__free_handicapped_spot_count = {'free_spot': 0}
        self.__free_compact_spot_count = {'free_spot': 0}
        self.__free_large_spot_count = {'free_spot': 0}
        self.__free_motorbike_spot_count = {'free_spot': 0}
        self.__free_electric_spot_count = {'free_spot': 0}
        self.__display_board = ParkingDisplayBoard()

    def add_floor(self, floor):
        pass

    def assign_ticket(self, vehicle_type):
        pass

    def scan_and_pay(self, ticket):
        pass

    def add_parking_spot(self, spot):
        switcher = {
            ParkingSpotType.HANDICAPPED: self.__handicapped_spots.put(spot.get_number(), spot),
            ParkingSpotType.COMPACT: self.__compact_spots.put(spot.get_number(), spot),
            ParkingSpotType.LARGE: self.__large_spots.put(spot.get_number(), spot),
            ParkingSpotType.MOTORBIKE: self.__motorbike_spots.put(spot.get_number(), spot),
            ParkingSpotType.ELECTRIC: self.__electric_spots.put(spot.get_number(), spot),
        }
        switcher.get(spot.get_type(), 'Wrong parking spot type')

    def assign_vehicle_to_spot(self, vehicle, spot):
        spot.assign_vehicle(vehicle)
        switcher = {
            ParkingSpotType.HANDICAPPED: self.update_display_board_for_handicapped(spot),
            ParkingSpotType.COMPACT: self.update_display_board_for_compact(spot),
            ParkingSpotType.LARGE: self.update_display_board_for_large(spot),
            ParkingSpotType.MOTORBIKE: self.update_display_board_for_motorbike(spot),
            ParkingSpotType.ELECTRIC: self.update_display_board_for_electric(spot),
        }
        switcher(spot.get_type(), 'Wrong parking spot type!')

    def update_display_board_for_handicapped(self, spot):
        if self.__display_board.get_handicapped_free_spot().get_number() == spot.get_number():
            # find another free handicapped parking and assign to display_board
            for key in self.__handicapped_spots:
                if self.__handicapped_spots.get(key).is_free():
                    self.__display_board.set_handicapped_free_spot(self.__handicapped_spots.get(key))

            self.__display_board.show_empty_spot_number()

    def update_display_board_for_compact(self, spot):
        if self.__display_board.get_compact_free_spot().get_number() == spot.get_number():
            # find another free compact parking and assign to display_board
            for key in self.__compact_spots:
                if self.__compact_spots.get(key).is_free():
                    self.__display_board.set_compact_free_spot(self.__compact_spots.get(key))

            self.__display_board.show_empty_spot_number()

    def free_spot(self, spot):
        spot.remove_vehicle()
        switcher = {
            ParkingSpotType.HANDICAPPED: self.__free_handicapped_spot_count.update(
                free_spot=self.__free_handicapped_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.COMPACT: self.__free_compact_spot_count.update(
                free_spot=self.__free_compact_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.LARGE: self.__free_large_spot_count.update(
                free_spot=self.__free_large_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.MOTORBIKE: self.__free_motorbike_spot_count.update(
                free_spot=self.__free_motorbike_spot_count["free_spot"] + 1
            ),
            ParkingSpotType.ELECTRIC: self.__free_electric_spot_count.update(
                free_spot=self.__free_electric_spot_count["free_spot"] + 1
            ),
        }

        switcher(spot.get_type(), 'Wrong parking spot type!')


"""
ParkingDisplayBoard: This class encapsulates a parking display board:
"""


class ParkingDisplayBoard:
    def __init__(self, id):
        self.__id = id
        self.__handicapped_free_spot = None
        self.__compact_free_spot = None
        self.__large_free_spot = None
        self.__motorbike_free_spot = None
        self.__electric_free_spot = None

    def show_empty_slot(self):
        message = ""
        if self.__handicapped_free_spot.is_free():
            message += "Free Handicapped: " + self.__handicapped_free_spot.get_number()
        else:
            message += "Handicapped is full"
        message += "\n"

        if self.__compact_free_spot.is_free():
            message += "Free Compact: " + self.__compact_free_spot.get_number()
        else:
            message += "Compact is full"
        message += "\n"

        if self.__large_free_spot.is_free():
            message += "Free Large: " + self.__large_free_spot.get_number()
        else:
            message += "Large is full"
        message += "\n"

        if self.__motorbike_free_spot.is_free():
            message += "Free Motorbike: " + self.__motorbike_free_spot.get_number()
        else:
            message += "Motorbike is full"
        message += "\n"

        if self.__electric_free_spot.is_free():
            message += "Free Electric: " + self.__electric_free_spot.get_number()
        else:
            message += "Electric is full"

        print(message)


class ParkingRate:
    def __init__(self):
        pass
        # self.__hours = hours


class ParkingTicket:
    def __init__(self):
        pass


"""
ParkingLot: Our system will have only one object of this class. 
This can be enforced by using the Singleton pattern. In software engineering, 
the singleton pattern is a software design pattern that restricts the instantiation of a class to only one object.
"""

import threading


class ParkingLot:
    instance = None

    class __OnlyOne:
        def __init__(self, name, address):
            # 1. initialize variables: read name, address and parking_rate from database
            # 2. initialize parking floors: read the parking floor map from database,
            #    this map should tell how many parking spots are there on each floor. This
            #    should also initialize max spot counts too.
            # 3. initialize parking spot counts by reading all active tickets from database
            # 4. initialize entrance and exit panels: read from database

            self.__name = name
            self.__address = address
            self.__parking_rate = ParkingRate()

            self.__compact_spot_count = 0
            self.__large_spot_count = 0
            self.__motorbike_spot_count = 0
            self.__electric_spot_count = 0
            self.__max_compact_count = 0
            self.__max_large_count = 0
            self.__max_motorbike_count = 0
            self.__max_electric_count = 0

            self.__entrance_panels = {}
            self.__exit_panels = {}
            self.__parking_floors = {}

            # all active parking tickets, identified by their ticket_number
            self.__active_tickets = {}

            self.__lock = threading.Lock()

    def __init__(self, name, address):
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
        else:
            ParkingLot.instance.__name = name
            ParkingLot.instance.__address = address

    def get_new_parking_ticket(self, vehicle):
        if self.is_full(vehicle.get_type()):
            raise Exception('Parking full!')
        # synchronizing to allow multiple entrances panels to issue a new
        # parking ticket without interfering with each other
        self.__lock.acquire()
        ticket = ParkingTicket()
        vehicle.assign_ticket(ticket)
        ticket.save_in_DB()
        # if the ticket is successfully saved in the database, we can increment the parking spot count
        self.__increment_spot_count(vehicle.get_type())
        self.__active_tickets.put(ticket.get_ticket_number(), ticket)
        self.__lock.release()
        return ticket

    def is_full(self, type):
        # trucks and vans can only be parked in LargeSpot
        if type == VehicleType.Truck or type == VehicleType.Van:
            return self.__large_spot_count >= self.__max_large_count

        # motorbikes can only be parked at motorbike spots
        if type == VehicleType.Motorbike:
            return self.__motorbike_spot_count >= self.__max_motorbike_count

        # cars can be parked at compact or large spots
        if type == VehicleType.Car:
            return (self.__compact_spot_count + self.__large_spot_count) >= (
                        self.__max_compact_count + self.__max_large_count)

        # electric car can be parked at compact, large or electric spots
        return (self.__compact_spot_count + self.__large_spot_count + self.__electric_spot_count) >= (
                    self.__max_compact_count + self.__max_large_count
                    + self.__max_electric_count)

    def increment_spot_count(self, type):
        large_spot_count = 0
        motorbike_spot_count = 0
        compact_spot_count = 0
        electric_spot_count = 0
        if type == VehicleType.Truck or type == VehicleType.Van:
            large_spot_count += 1
        elif type == VehicleType.Motorbike:
            motorbike_spot_count += 1
        elif type == VehicleType.Car:
            if self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1
        else:  # electric car
            if self.__electric_spot_count < self.__max_electric_count:
                electric_spot_count += 1
            elif self.__compact_spot_count < self.__max_compact_count:
                compact_spot_count += 1
            else:
                large_spot_count += 1

    def add_parking_floor(self):
        # add in db
        pass

    def add_entrance_panel(self):
        # add in db
        pass

    def add_exit_panel(self):
        # add in db
        pass

    def is_full(self):
        for key in self.__parking_floors:
            if not self.__parking_floors.get(key).is_full():
                return False

        return True

