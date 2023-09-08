class Solution:
    def sumOfFlooredPairs(elf, nums: List[int]) -> int:
      n,mx = len(nums)+1,0
      mx = max(nums) + 1
      cnt = Counter(nums)
      pre = [0]*mx
      pre[0] = cnt[0]
      for i in range(1,mx):
        pre[i]=pre[i-1]+cnt[i]
      ret = 0
      seen = [False]*mx
      for i in nums:
        if seen[i]: continue
        seen[i] = True
        for j in range(i,mx,i):
          ret +=(pre[-1]-pre[j-1])*cnt[i]
          #print(f"i:{i} , j:{j} , pre[R]:{pre[-1]} , pre[L-1]:{pre[j-1]} contrib: {(pre[-1] - pre[j-1])*cnt[i]}")
      return ret%1000000007
