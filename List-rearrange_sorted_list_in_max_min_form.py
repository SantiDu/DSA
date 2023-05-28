# educative

def max_min(lst):
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
