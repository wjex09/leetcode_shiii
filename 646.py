class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
      pairs.sort()
      ans = 0
      next = -200000
      for u ,v in pairs :
        if u > next :
          ans+=1
          next = v
        else : next = min(next , v)
      return ans
