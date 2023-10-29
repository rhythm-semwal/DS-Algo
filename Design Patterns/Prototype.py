import copy
from abc import ABCMeta, abstractmethod


class Courses(metaclass=ABCMeta):
    def __init__(self):
        self.id = None
        self.type = None

    @abstractmethod
    def course(self):
        pass

    def get_type(self):
        return self.type

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def clone(self):
        return copy.copy(self)


class DSA(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Data structure and algorithms"

    def course(self):
        print("inside dsa course")


class SDE(Courses):
    def __init__(self):
        super().__init__()
        self.type = "Software development"

    def course(self):
        print("Inside SDE course")


class CoursesCache:
    cache = dict()

    @staticmethod
    def get_course(id):
        course = CoursesCache.cache.get(id, None)
        return course

    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("1")
        CoursesCache.cache[sde.get_id()] = sde

        dsa = DSA()
        dsa.set_id("2")
        CoursesCache.cache[dsa.get_id()] = dsa


if __name__ == '__main__':
    CoursesCache.load()

    sde = CoursesCache.get_course("1")
    print(sde.get_type())

    dsa = CoursesCache.get_course("2")
    print(dsa.get_type())
