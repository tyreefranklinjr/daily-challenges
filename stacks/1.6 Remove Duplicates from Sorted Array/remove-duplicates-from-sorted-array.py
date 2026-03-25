class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        unsorted = True

        while unsorted: 
            prev = None
            index = 0

            unsorted = False

            for number in nums:
                if number == prev and index > 0:
                    del nums[index]
                    unsorted = True
                
                prev = number
                index += 1
    
            print(nums)
