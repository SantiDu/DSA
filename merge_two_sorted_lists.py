def merge_lists1(lst1, lst2):
    index = 0
    for elem in lst2:
        while index < len(lst1) and elem > lst1[index]:
            index += 1
        lst1.insert(index, elem)
    return lst1

def merge_lists2(lst1, lst2):
    l = []
    for elem2 in lst2:
        while lst1 and elem2 > lst1[0]:
            l.append(lst1.pop(0))
        l.append(elem2)
    return l + lst1
