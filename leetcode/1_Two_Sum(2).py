

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [3, 2, 4]
target = 6
r1 = Solution()
print(r1.twoSum(nums, target))
