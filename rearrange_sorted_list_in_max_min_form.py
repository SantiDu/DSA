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

# def max_min3(lst):
