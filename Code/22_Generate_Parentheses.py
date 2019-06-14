# 2019-06-13  Runtime: 44 ms

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        st = ""
        self.backtrack(res, st, 0, 0, n)
        return res
    
    def backtrack(self, res: List[str], cur: str, l: int, r: int, n: int):
        if len(cur) == 2 * n:
            res.append(cur)
            return
        if l < n:
            self.backtrack(res, cur + '(', l + 1, r, n)
        if r < l:
            self.backtrack(res, cur +')', l, r + 1, n)
        
        
