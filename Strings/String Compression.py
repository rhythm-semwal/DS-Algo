def encode(arr):
    # Code here
    result_string = []
    count = 1
    n = len(arr)
    result_string += arr[0]
    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            # if count > 1:
            result_string.append("% s" % count)

            result_string.append(arr[i + 1])
            count = 1

    # if count > 1:
    result_string.append("% s" % count)

    return "".join(result_string)


str = "aaaabbbccc"
print(encode(str))
