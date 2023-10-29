def calc_gcd(self, a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a < b:
        a, b = b, a

    while b > 0:
        a = a % b
        a, b = b, a

    return a