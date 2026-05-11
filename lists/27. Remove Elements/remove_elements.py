class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # Iterate through the nums array
        while val in nums:
            for i, num in enumerate(nums):
                if num == val:
                    del nums[i]
                    break

        return len(nums)
