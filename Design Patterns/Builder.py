from abc import ABC, abstractmethod


class Course(ABC):

    @abstractmethod
    def fee(self):
        pass

    @abstractmethod
    def available_seats(self):
        pass

    def __repr__(self):
        return 'Fee : {0.fee} | Batches Available : {0.batches}'.format(self)

    # def __str__(self):
    #     return "{0} object created".format(self)


class DSA(Course):
    def fee(self):
        self.fee = 8000

    def available_seats(self):
        self.batches = 5

    def batch_name(self):
        print("Scaler EliteX")


class SDE(Course):
    def fee(self):
        self.fee = 10000

    def available_seats(self):
        self.batches = 10


class ComplexCourse:
    def __repr__(self):
        return 'Fee : {0.fee} | available_batches: {0.batches}'.format(self)


class ComplexCourse(ComplexCourse):
    def fee(self):
        self.fee = 1700

    def available_seats(self):
        self.batches = 2


# @classmethod
def construct_course(cls):
    course = cls()
    course.fee()
    course.available_seats()
    # course.batch_name()

    return course


if __name__ == "__main__":
    dsa = DSA()  # object for DSA course
    sde = SDE()  # object for SDE course

    complex_course = construct_course(SDE)
    print(complex_course)

