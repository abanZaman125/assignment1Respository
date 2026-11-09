def solution(A):
    #permutation is an array of length N and elements range(1,N+1)
    #make it a set to remove distinct values
    #check if the max value of A equals its length to know A is the sequence 1...N

    return 1 if max(A) == len(A) and len(set(A)) == len(A) else 0