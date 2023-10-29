def build(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    build(arr, tree, left_child, start, mid)
    build(arr, tree, right_child, mid + 1, end)

    tree[node] = tree[left_child] ^ tree[right_child]
    return tree


def query(tree, node, start, end, left, right):
    if right < start or left > end:
        return 0
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    left_child = 2 * node + 1
    right_child = 2 * node + 2

    return query(tree, left_child, start, mid, left, right) ^ query(tree, right_child, mid + 1, end, left, right)


def getXor(arr, n, li, ri):
    '''
    arr: given array
    n:   len of given array
    li: left index of range
    ri: right index of range
    '''
    from math import ceil, log2
    height = int(ceil(log2(n)))
    max_size = 2 * (int(2 ** height))
    tree = [0] * max_size
    build(arr, tree, 0, 0, n - 1)

    result = query(tree, 0, 0, n - 1, li, ri)
    return result
