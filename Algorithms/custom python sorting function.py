# ascending order
def letter_cmp(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1

# descending order
def letter_cmp(a, b):
    if a[1] > b[1]:
        return -1
    elif a[1] == b[1]:
        if a[0] > b[0]:
            return 1
        else:
            return -1
    else:
        return 1


from functools import cmp_to_key
letter_cmp_key = cmp_to_key(letter_cmp)
[].sort(key=letter_cmp_key)