class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minimum, ans = nums[0], 0
        for num in nums[1:]:
            ans = max(ans, num - minimum)
            minimum = min(minimum, num)
        return ans if ans else -1