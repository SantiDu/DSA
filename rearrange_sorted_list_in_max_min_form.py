def max_min1(lst):
    l = []
    while lst:
        l.append(lst.pop())
        try:
            l.append(lst.pop(0))
        except IndexError:
            break
    return l

def max_min2(lst):
    l = []
    quotient, remainder = divmod(len(lst), 2)
    for small, large in zip(lst, lst.__reversed__()):
        if not quotient:
            if remainder == 1:
                l.append(small)
                break
        else:
            l.append(large)
            l.append(small)
            quotient -= 1
    return l

def max_min3(lst):
    def two_numbers_in_one():
        n_to_hold = lst[index] % n_max_pp
        return n + n_to_hold * n_max_pp
    n_max_pp = lst[-1] + 1
    for i, n in enumerate(lst):
        if i % 2 == 0:
            index = len(lst) - (i // 2 + 1)
            lst[i] = two_numbers_in_one()
        else:
            index = (i - 1) // 2
            lst[i] = two_numbers_in_one()
    for i, n in enumerate(lst):
        lst[i] //= n_max_pp
    return lst
