class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      digits = ''.join([str(digit)for digit in digits])   #to string
      digits = str(int(digits)+1)
      return [int(digit) for digit in list(digits)]
