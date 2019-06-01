# 2019-05-31  Runtime: 72 ms

class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':

        start = 0
        max_len = 0
        let_pos = {}

        for i in range(len(s)) :
            if s[i] in let_pos and start <= let_pos[s[i]] :
                start = let_pos[s[i]] + 1
            else :
                max_len = max(max_len, i - start + 1)
            let_pos[s[i]] = i
        return max_len
