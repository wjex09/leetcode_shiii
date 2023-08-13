class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      n = len(nums)
      ans = [1]*n
      running_pre = 1
      running_suf= 1
      for i in range(0,n) :
        ans[i] *= running_pre
        running_pre *= nums[i]
      for i in range(n-1,-1,-1) :
        ans[i] *= running_suf
        running_suf *= nums[i]
      return ans
