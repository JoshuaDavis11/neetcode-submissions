class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copyNums = {}
        ans = []
        for i in range(len(nums)):
            copyNums[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i] 
            if copyNums.get(difference):
                if i != copyNums.get(difference):
                    ans.append(i)
                    ans.append(copyNums.get(difference))
                    break
                    
                   
        return  ans