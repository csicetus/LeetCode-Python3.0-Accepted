# 2019-06-08  Runtime: 32 ms  Algorithm: Recursive

class Solution:    
    def letterCombinations(self, digits: str) -> List[str]:
        if (not digits):
            return []
        res = []
        self.combination("", digits, 0, res)
        return res
        
    def combination(self, prefix: str, digits: str, offset: int, res: List[str]):
        if (offset == len(digits)):
            res.append(prefix)
            return
        KEYS = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        letters = KEYS[int(digits[offset])]
        for i in range(0, len(letters)):
            self.combination(prefix + letters[i], digits, offset + 1, res)
        
