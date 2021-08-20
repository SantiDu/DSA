def merge_lists1(lst1, lst2):
    index = 0
    for elem in lst2:
        while index < len(lst1) and elem > lst1[index]:
            index += 1
        lst1.insert(index, elem)
    return lst1

def merge_list2(lst1, lst2):
    pass
