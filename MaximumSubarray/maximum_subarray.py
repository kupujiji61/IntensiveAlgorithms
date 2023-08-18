class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        current_maximum = 0
        if max(nums) <= 0:
            return max(nums)
        for i in range(len(nums)):
            if nums[i] >= 0:
                current_sum += nums[i]
            elif current_sum + nums[i] > 0:
                if current_sum > current_maximum:
                    current_maximum = current_sum
                current_sum += nums[i]
            else:
                if current_sum > current_maximum:
                    current_maximum = current_sum
                current_sum = 0
        return max(current_sum, current_maximum)
