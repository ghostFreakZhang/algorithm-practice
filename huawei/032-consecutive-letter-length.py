'''
题目描述：
给定一个字符串，只包含大写字母，求在包含同一字母的子串中，长度第 k 长的子串的长度，相同字母只取最长的那个子串。

输入描述:
第一行有一个子串(1<长度<=100)，只包含大写字母。
第二行为 k的值

输出描述:
输出连续出现次数第k多的字母的次数。

示例1
输入
AAAAHHHBBCDHHHH
3
输出
2
说明
同一字母连续出现的最多的是A和H，四次；第二多的是H，3次，但是H已经存在4个连续的，故不考虑；下个最长子串是BB，所以最终答案应该输出2。
示例2
输入
AABAAA
2
输出
1
说明
同一字母连续出现的最多的是A，三次；第二多的还是A，两次，但A已经存在最大连续次数三次，故不考虑；下个最长子串是B，所以输出1
示例3
输入
ABC
4
输出
-1
说明
只含有3个包含同一字母的子串，小于k，输出-1
示例4
输入
ABC
2
输出
1
说明
三个子串长度均为1，所以此时k = 1，k=2，k=3这三种情况均输出1。特此说明，避免歧义。
备注:
若子串中只包含同一字母的子串数小于k，则输出-1
'''

import re
in_str = input()
k = int(input())
res = []
for s in set(in_str):
    str_list = sorted(re.findall(r'('+ s +'+)', in_str), key = lambda x : len(x), reverse = True)
    res.append(str_list[0].count(s))
print(sorted(res, reverse = True)[k - 1]) if len(res) >= k else print(-1)