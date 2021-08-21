def rearrange1(lst):
    negatives = []
    positives = []
    for i in lst:
        if i >= 0:
            positives.append(i)
        else:
            negatives.append(i)
    return negatives + positives

def rearrange2(lst):
    index_last_neg = 0
    for i, elem in enumerate(lst):
        if elem < 0 and i != index_last_neg:
            lst[i], lst[index_last_neg] = lst[index_last_neg], lst[i]
            index_last_neg += 1
    return lst

