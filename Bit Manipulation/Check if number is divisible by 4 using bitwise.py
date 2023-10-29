def Div_by_4(n):
    return ((n >> 2) << 2) == n


print(Div_by_4(16))
