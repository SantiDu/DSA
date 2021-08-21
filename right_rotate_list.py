def right_rotate(lst, k):
    try:
        k %= len(lst)
    except ZeroDivisionError:
        return []
    return lst[len(lst) - k:] + lst[:len(lst) - k]