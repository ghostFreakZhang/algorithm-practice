
## 题目内容

[最长回文子串题目链接](https://leetcode-cn.com/problems/longest-palindromic-substring/)

给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：

输入：s = "babad"

输出："bab"

解释："aba" 同样是符合题意的答案。

示例 2：

输入：s = "cbbd"


输出："bb"

## 题解

- 直接暴力解法

执行超时，通过大概1/3用例。

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                if s[i:j] == ''.join(list(s[i:j])[::-1]) and len(s[i:j]) > len(res):
                    res = s[i:j]
        return res
```

- 双指针解法

中间向两端的双指针扩散判断回文串

找回文串的关键技巧是传入两个指针 l 和 r 向两边扩散，因为这样实现可以同时处理回文串长度为奇数和偶数的情况

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(s: str, l: int, r: int) -> str:
            '''
            计算以 s[l] 和 s[r] 为中心的最长回文子串
            '''
            # 注意循环条件，防止越界
            while l >= 0 and r < len(s) and s[l] == s[r]:
                # 向两边展开
                l -= 1
                r += 1
            # l 这里最小到 -1
            return s[l + 1:r]

        res = ''
        for i in range(len(s)):
            # 以 s[i] 为中心的最长回文子串
            s1 = helper(s, i, i)
            # 以 s[i] 和 s[i + 1] 为中心的最长回文子串
            s2 = helper(s, i, i + 1)
            res = sorted([res, s1, s2], key = lambda x: len(x))[-1]
        return res
```