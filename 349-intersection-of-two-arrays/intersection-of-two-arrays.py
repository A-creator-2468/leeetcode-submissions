class Solution(object):
    def intersection(self, nums1, nums2):
        result=[]
        nums1=set(sorted(nums1))
        nums2=set(sorted(nums2))
        for i in nums1:
            for j in nums2:
                if i==j:
                    result.append(i)
        return result            

        