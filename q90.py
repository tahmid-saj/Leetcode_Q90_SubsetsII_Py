class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(pos, ansArr):
            if len(nums) == pos:
                res.append(ansArr.copy())
                return

            ansArr.append(nums[pos])
            backtrack(pos + 1, ansArr)
            ansArr.pop()

            while pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
                pos += 1
            backtrack(pos + 1, ansArr)

        backtrack(0, [])
        return res
        
