class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        arr = nums
        result=[]

        for i in range(1 << n):
            subset = []
            for j in range(n):
                if i & (1 << j):
                    subset.append(arr[j])
            result.append(subset)
        return(result)
        