def solution(A):
    #A has N elements but has a seqeuence 1...N+1
    #Range excludes stop value, so stop must be N+2
    #set difference to get elements in A not in B, leaves only missing value
    #pop() to get element because you cannot access sets directly
    return (set(range(1,len(A)+2)) - set(A)).pop()