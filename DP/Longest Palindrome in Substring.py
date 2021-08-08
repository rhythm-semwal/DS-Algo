# code
# appraoch 1
# T.C = O(N**2)


def get_substring(word, start, end):
    result = ""
    for i in range(start, end):
        result += word[i]

    return result


def longestPalindrome(s):
    n = len(s)

    lookup_table = [[0 for _ in range(n)] for _ in range(n)]

    max_length = 1
    start = 0
    # base case for string of length 1 are palindrome so filling the diagonal values as 1
    for i in range(n):
        lookup_table[i][i] = 1

    # checking for string of length 2
    flag = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            lookup_table[i][i+1] = 1
            if not flag:
                start = i
                max_length = 2
                flag = 1

    k = 3
    while k <= n:
        i = 0
        while i < (n-k+1):
            j = i + k -1

            if s[i] == s[j] and lookup_table[i+1][j-1]:
                lookup_table[i][j] = 1

                if k > max_length:
                    start = i
                    max_length = k

            i += 1

        k += 1

    print(max_length)
    return get_substring(s, start, start+max_length)

input = "kjqlrzzfmlvyoshiktodnsjjp"
print(longestPalindrome(input))

# appraoch 2
# T.C = O(N**3)
# def is_palindrome(word, start, end):
#     while start < end:
#         if word[start] != word[end]:
#             return False
#
#         start += 1
#         end -= 1
#     return True
#
# def get_substring(word, start, end):
#     result = ""
#     for i in range(start, end):
#         result += word[i]
#
#     return result
#
# def longestPalindrome(s):
#     max_length = 1
#     start = 0
#     n = len(s)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if is_palindrome(s, i, j):
#                 if j - i + 1 > max_length:
#                     max_length = j - i + 1
#                     start = i
#
#     result = get_substring(s, start, start+max_length)
#     print(result)

# input = "forgeeksskeegfor"
# print(longestPalindrome(input))
# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         s = input()
#         print(longestPalindrome(s))