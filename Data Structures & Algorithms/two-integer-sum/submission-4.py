class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        copyNums = {}
        for i in range(len(nums)):
            copyNums[nums[i]] = i

        for i in range(len(nums)):
            difference = target - nums[i] 
            if difference in copyNums and i != copyNums[difference]:
                return [i,copyNums[difference]]
                            
        return  []