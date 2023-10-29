from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Quack")

    def fly(self):
        print("Fly Duck Fly")


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble")

    def fly(self):
        print("Fly Turkey Fly")


class TurkeyAdapter(Duck):
    turkey: Turkey

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        self.turkey.fly()


# duck:MallardDuck = MallardDuck()
turkey: WildTurkey = WildTurkey()

# duck.fly()
# turkey.fly()

turkeyAdapter: Duck = TurkeyAdapter(turkey)

turkeyAdapter.fly()
# # Although the client calls the Duck quack() method,
# # under the hood this is translated to the turkey's gobble() method:
turkeyAdapter.quack()