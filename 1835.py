class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
      a , b, = 0 , 0
      for i in arr1 :
        a^=i
      for i in arr2 :
        b^=i
      return a&b
