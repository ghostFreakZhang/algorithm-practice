'''
题目描述:
给定字符串 target和 source, 判断 target 是否为 source 的子序列。
你可以认为 target 和 source 中仅包含英文小写字母。字符串 source可能会很长（长度 ~= 500,000），而 target 是个短字符串（长度 <=100）。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"abc"是"aebycd"的一个子序列，而"ayb"不是）。
请找出最后一个子序列的起始位置。

输入描述:
第一行为target，短字符串（长度 <=100）
第二行为source，长字符串（长度 ~= 500,000）

输出描述:
最后一个子序列的起始位置， 即最后一个子序列首字母的下标

示例1
输入
abc
abcaybec
输出
3
说明
这里有两个abc的子序列满足，取下标较大的，故返回3
备注:
若在source中找不到target，则输出-1
'''

target = input()
source = input()
res = []
index = 0
for i, v in enumerate(source):
    if index == len(target) - 1:
        index = 0
    elif v == target[index]:
        if index == 0:
            res.append(i)
        index += 1
print(max(res))