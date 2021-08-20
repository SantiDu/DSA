def find_second_maximum(lst):
    max1, max2 = lst[0], lst[1]
    if max1 < max2:
        max1, max2 = max2, max1
    for elem in lst[2:]:
        if max2 < elem < max1:
            max2 = elem
        elif elem > max1:
            max1, max2 = elem, max1
    return max2
