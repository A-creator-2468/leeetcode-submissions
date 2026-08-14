class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        csum=0 #this is our prefixsum
        subcnt=0
        seen={0:1} #hash map to store prefix sums found so far
        for i in nums:
            csum+=i#compute prefix sum
            #chech if req in prefixes so far
            req=csum-k
            if req in seen:
                subcnt+=seen[req]
                # add the number of times we seen that prefix 
                #push the current prefix in the hash map
            seen[csum]=seen.get(csum,0)+1
        return subcnt        
       