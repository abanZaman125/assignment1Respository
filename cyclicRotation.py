# Select any five problems from the table above
# Write the pseudocode by hand for each problem.
# Write your Python solution for each problem.
# Upload your pseudocode and Python code to your GitHub repository

# PDF report (for each problem)
#   -> photo of pseudocode
#   -> python code with comments
#   -> Citations for any AI tools/resources
#   -> Link to Ai chat & github repo

#Cyc.Rot./OddOc.InArrary/FrogJmp/PrmMisingElem/TapeEq.

#REFERENCES:
#https://stackoverflow.com/questions/15768757/how-to-construct-a-set-out-of-list-items-in-python
#https://www.w3schools.com/python/python_sets_access.asp
#https://www.w3resource.com/python-exercises/sets/python-sets-exercise-1.php

#----------------------------------------------------------------------------------------------------#

#Array A made of N integers, rotated K times
#A=[3,8,9],k=2 -> [8,9,3]
#N = [0,100], K = [0,100], N_i = [-1000,1000]
##Thinking make copy of A where all elements 0
##Make a formula for A[i] -> A[i + K]
def solution1(A,K):
    #create an array with N elements - all 0
    rotated_array = [0] * len(A)

    ## 2 cases for rotations (k % len(A)) [doesnt allow for rotations of elements going over array twice]
    ### rotation doesn't rotate through array [1, 0, 0] -[shift 2]> [0, 0, 1]
    ### flip/over/rotate through: [0,0,1] -> K=1 -> [1,0,0]
    ### index 2 becomes 0 = current + (K % len(A)) - N
    #add conditional operator to avoid n % 0 (empty list)
    actual_k = K % len(A) if len(A) != 0 else 0

    #only change positions if given rotations doesn't lead original array
    if actual_k != 0:
        for i in range(0, len(A)):
            # the new index for the rotated element, not used if the element when rotated goes back to beginning
            new_index = i + actual_k
            rotated_array[new_index if (new_index < len(A)) else new_index - len(A)] = A[i]
        return rotated_array

    #returns A if k equals 0, no rotation means A stays the same
    return A