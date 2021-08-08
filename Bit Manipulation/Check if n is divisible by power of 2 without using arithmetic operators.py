def isDivBy2PowerM(n, m):
    # if expression results to 0, then
    # n is divisible by pow(2, m)
    if (n & ((1 << m) - 1)) == 0:
        return True

    # n is not divisible
    return False
