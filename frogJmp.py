from math import ceil


#given integers X, Y, D from [1-1 000 000 000]
#minimal number of steps ("size" D) from X to Y
def solution(X, Y, D):
    ##How many steps needed to go over/equal to Y-X
    ##using ceiling, if (Y-X) % D == 0, then we keep the same value
    ##if not we round up
    return ceil((Y-X)/D)