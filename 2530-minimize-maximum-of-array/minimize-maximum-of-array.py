class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        n = len(nums)
        arr = nums

        total = ans = 0

        for i in range(n):
            total += arr[i]
            ans = max(ans, math.ceil(total / (i + 1)))

        return ans