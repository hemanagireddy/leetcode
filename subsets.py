
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.subsetsWithDupRecu(res, [], sorted(nums))
        return res

    def subsetsWithDupRecu(self, res, cur, nums):
        if not nums:
            if cur not in res:
                res.append(cur)
        else:
            self.subsetsWithDupRecu(res, cur, nums[1:])
            self.subsetsWithDupRecu(res, cur + [nums[0]], nums[1:])

