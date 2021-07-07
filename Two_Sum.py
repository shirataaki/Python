class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    def twoSum(self, nums, target):
        for i, num1 in enumerate(nums):
            for j in range(i+1,len(nums)):
                if(nums[j] == target - nums[i]):
                    return [i,j]
        return []

Sol = Solution() # Solに関数一つをカプセル化したオブジェクトを代入
target = 11
nums = [2,7,11,15,4]
l = Sol.twoSum(nums, target)
print(l)