class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        nums.sort()

        end = 0
        for i in range(0, len(nums)):
            start = 0
            if i > 0 and nums[i] == nums[i - 1]: start = end + 1
            end = len(subsets) - 1
            for j in range(start, end + 1):
                currSubset = list(subsets[j])
                currSubset.insert(j, nums[i])
                subsets.append(currSubset)

        return subsets
