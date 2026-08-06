class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left=0
        currentsum=0
        avg=0.0
      
        count=0
        for i in range(len(arr)):
            currentsum+=arr[i]
            if i>=k-1:
                avg=currentsum/k
                currentsum-=arr[left]
                left+=1
                if avg>=threshold:
                    count+=1 
        return count           
                

        