class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        output = list()
        
        for x in candies:
            if x + extraCandies < max_candies:
                output.append(False)
            else:
                output.append(True)
                
        return output