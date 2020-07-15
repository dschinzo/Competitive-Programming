class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                lst = [i]
                break
        for j in range(i+1, len(nums)):
            if target - nums[lst[0]] == nums[j]:
                lst.append(j)
        return lst
