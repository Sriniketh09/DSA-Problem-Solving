class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return True
        l = len(flowerbed)
        res = False
        for i in range(l):
            if i==0 and 1 not in flowerbed[:2] :
                #print("cond1")
                flowerbed[i] = 1 if n>0 else 0
                n = n-1 if n>0 else n-0
            elif i<= l-2 and flowerbed[i]==0:
                #print("cond2")
                cond = True if flowerbed[i-1] == 0 and flowerbed[i+1]==0 else False
                flowerbed[i] = 1 if cond else 0
                n -= 1 if cond and n>0 else 0
            elif i==l-1 and 1 not in flowerbed[l-2:]:
                #print("cond3")
                flowerbed[i] = 1 if n>0 else 0
                n = n-1 if n>0 else n-0
            if n==0:
                res = True
                break
            #print(flowerbed)
        return res
                        
