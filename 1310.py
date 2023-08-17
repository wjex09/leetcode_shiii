class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
      pre = [0] * len(arr)
      pre[0] = arr[0]
      for i in range(1,len(arr)) :
        pre[i] = pre[i-1] ^ arr[i]
      ret = []
      for l ,r in queries:
        if not l : ret.append(pre[r])
        else : ret.append(pre[r] ^ pre[l-1])
      return ret
