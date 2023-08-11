class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
      inn , out  = defaultdict(int),defaultdict(int)
      for u ,v in matches :
        out[v]+=1
        inn[u]+=1
      clean,one_loss = [], []
      for u , _ in inn.items() :
         if u not in out: clean.append(u)
      for u , v in out.items() :
        if v == 1 : one_loss.append(u)
      clean.sort()
      one_loss.sort()
      return [clean,one_loss]
