class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
      cur = [0] * 1000 #Ez O^2
      for num , u , v in trips :
        for i in range(u,v):
          cur[i]+=num
          if cur[i] > capacity : return False
      return True
