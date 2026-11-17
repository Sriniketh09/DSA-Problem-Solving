class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        m = max(candies)
        for c in candies:
            res.append(True if c+extraCandies>= m else False)
        return res
