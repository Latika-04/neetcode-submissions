class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        count=1
        longest=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                longest = max(longest, count)
                count = 1
        longest=max(longest,count)
        return longest
        