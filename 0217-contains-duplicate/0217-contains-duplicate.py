class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        value = set(nums)
        if len(value) == len(nums) :
            return False
        return True 