class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n=len(nums)
        a=nums
        b=sorted(a)
        start=n
        end=0
        for i in range(n):
            if a[i]!=b[i]:
                start=min(start,i)
                end=max(end,i)
        if end==0:
            return 0
        else:
            return (end-start+1)
                