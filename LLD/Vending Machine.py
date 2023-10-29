from decimal import Decimal


class DollarAmount(Decimal):
    """
    Represents a dollar amount.
    Extends the decimal.Decimal class.
    """
    def __repr__(self):
        return f"DollarAmount('{self}')"

    def __str__(self):
        return f'${self:,.2f}'


class Coin:
    """Base class representing coins."""
    value = DollarAmount('0')

    def __radd__(self, other):
        return self.value + other

    def __eq__(self, other):
        return self.value == other.value


class FiveCent(Coin):
    """5 cent coin."""
    value = DollarAmount('0.05')


class TenCent(Coin):
    """10 cent coin."""
    value = DollarAmount('0.10')


class Quarter(Coin):
    """25 cent coin."""
    value = DollarAmount('0.25')


class Loonie(Coin):
    """$1 coin."""
    value = DollarAmount('1')


class Toonie(Coin):
    """$2 coin."""
    value = DollarAmount('2')

COIN_CLASSES = [
    money.FiveCent,
    money.TenCent,
    money.Quarter,
    money.Loonie,
    money.Toonie
]


class VendingMachine:
    """
    A virtual vending machine.
    """
    def __init__(self):
        self.inserted_coins = []

    def insert_coin(self, coin):
        """
        Accepts a Coin instance and inserts it into the vending machine.
        """
        if not isinstance(coin, money.Coin):
            raise ValueError()

        self.inserted_coins.append(coin)

    def get_balance(self):
        """
        Returns the balance remaining.
        """
        return sum(self.inserted_coins)

    def get_change(self):
        """
        Returns change representing positive balance. The largest
        denominations are always used first.
        """
        coins = []
        balance = self.get_balance()
        balance -= balance * 100 % 5

        while balance > 0:
            for coin_class in reversed(COIN_CLASSES):
                if balance - coin_class.value >= 0:
                    coin = coin_class()  # Create a coin instance
                    coins.append(coin)
                    balance -= coin_class.value
                    break

        return coins