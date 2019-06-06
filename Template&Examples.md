# Template
### Codirectional double pointer template
##### Key: The outer loop traverses every position from 0 to n-1, the inner loop "does not look back", j++ until the optimal position
##### Time Complexity:  O(n)
##### Algorithm:
    j = 0
    // Loop the starting position of each subarray
 
    for i in range(n):
      while j < n and current subarray does not satisfy the condition：
        j += 1
        Broaden the current subarray
      
      if current subarray does satisfy the condition：
        Compare and judge whether the current solution is the optimal solution

      Remove nums[i] from the current subarray
    
| \# | Problems | Difficulty | Solution |
|----|----------|-----------|------|
| 003  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Medium | [Java](./Code/3_ Longest_Substring_Without_Repeating_Characters.py)
| 076  | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) |Hard| [Java]
| 209  | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/) | Medium | [Java]
----------------------------------
###  template
| \# | Problems | Difficulty | Solution |
|----|----------|-----------|------|
| 001  | [Two_Sum](https://leetcode.com/problems/two-sum/)  | Easy | [Java]
| 002  | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) |Medium| [Java] 
