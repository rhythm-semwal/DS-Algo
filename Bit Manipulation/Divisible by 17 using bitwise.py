def isDivisibleby17(n):
    # if n=0 or n=17 then yes
    if n == 0 or n == 17:
        return True

    # if n is less then 17, not
    # divisible by 17
    if n < 17:
        return False

    # reducing the number by floor(n/16)
    # - n%16
    return isDivisibleby17(int(n >> 4) - int(n & 15))

print(isDivisibleby17(51))