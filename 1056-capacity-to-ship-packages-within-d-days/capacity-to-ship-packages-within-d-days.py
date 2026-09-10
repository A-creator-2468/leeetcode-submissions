def CanShip(weights,days_have,capacity):
    #finds the days needed to ship all the weights under choosen capacity
    days_needed=1
    cweightsum=0
    for w in weights:
        if cweightsum+w<=capacity:
            cweightsum+=w
        else:
            days_needed+=1
            cweightsum=w
    return days_needed<=days_have                
# compare days_needed <=days_have (capacity is a valid choice)
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if CanShip(weights,days,mid):
                high=mid
            else:
                low=mid+1
        return low            
        