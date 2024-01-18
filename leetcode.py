class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            if nums[i] + nums[i + 1] == target:
                return (nums.index(nums[i]),
                        nums.index(nums[i + 1]))

nums = [3, 3]
target = 6
serch_two_summ = Solution()
print(serch_two_summ.twoSum(nums, target))