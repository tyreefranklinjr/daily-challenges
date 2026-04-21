class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # Declare the essential variables
        res = []
        min_i = 1

        # Read through the prices list
        for i in prices:
            res.append(i)
            
            # Find smaller prices
            for j in prices[min_i:]:
                if i >= j:
                    res[-1] = i - j
                    break
            
            min_i += 1

        return res
