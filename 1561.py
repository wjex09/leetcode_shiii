class Solution:
    def maxCoins(self, piles: List[int]) -> int:
      piles.sort()
      ans = sum(piles[-2*i-2] for i in range(len(piles)//3))
      return ans
