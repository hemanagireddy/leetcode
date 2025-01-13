class Solution(object):
    def reverse(self, p):
        """
        :type p: int
        :rtype: int
        """
        if p < 0:
            return -self.reverse(-p)

        result = 0
        while p:
            result = result * 10 + p % 10
            p //= 10
        return result if result <= 0x7fffffff else 0 
    
