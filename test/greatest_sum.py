# function to find out the subset greater than length 1
def sublist(lst):
    sub = []
    for i in range(len(lst) + 1):
        for j in range(i + 1, len(lst) + 1):
            sub1 = lst[i:j]
            if len(sub1) > 1:
                sub.append(sub1)
    return sub


def greatest_sum(lst):
    sub_proper = sublist(lst)
    # list containing the  sum of all the subsets
    sum_array = (list(map(sum, sub_proper)))
    # maximum sum of the subsets
    max_sum = max(sum_array)
    return max_sum


print(greatest_sum([1, 2,-3,6]))

