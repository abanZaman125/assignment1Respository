#A is NON EMPTY and ODD # OF ELEMENTS [N]
#all but one of the values in A occur an even number of times
## and one unique value occurs an odd # times
def solution(A):
    if len(A) == 1:
        return A[0]

    #initiate list
    search_through_list = []

    ###For an element occurs an even amount of times, if added, it will be removed at some point (add, remove, [x2(n)])
    ###If an element occurs an odd amount of times, once discovered/added
    ###it gets removed, but must be added again (add, remove, add x2[n])
    for number in A:
        if number not in search_through_list:
            search_through_list.append(number)
        else:
            search_through_list.remove(number)

    return search_through_list[0]