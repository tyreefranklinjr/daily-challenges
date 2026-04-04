class Solution(object):
    def lengthOfLongestSubstring(self, s):

        from collections import Counter
        
        """
        :type s: str
        :rtype: int
        """

        from collections import deque

        longest_count = 0
        
        dummy_list = []

        dup_list = deque(s)

        for i in range(len(dup_list)):

            dummy_list = []
            temp_count = 0

            for temp in dup_list:
                if temp in dummy_list:
                    break

                else:
                    dummy_list.append(temp)
                    temp_count += 1

            if temp_count > longest_count:
                longest_count = temp_count

            dup_list.popleft()

        return longest_count
