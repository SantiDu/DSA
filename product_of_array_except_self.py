def find_product(lst):
    zero_count = 0
    product = 1
    for i in lst:
        if i != 0:
            product *= i
        else:
            zero_count += 1
    l = []
    for i in lst:
        if zero_count > 1:
            l.append(0)
        elif zero_count == 1:
            if i == 0:
                l.append(product)
            else:
                l.append(0)
        else:
            l.append(product / i)
    return l
