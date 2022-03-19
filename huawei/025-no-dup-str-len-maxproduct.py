'''
题目描述：
给定一个元素类型为小写字符串的数组，请计算两个没有相同字符的元素长度乘积的最大值。
如果没有符合条件的两个元素返回0。

输入描述：
输入为一个半角逗号分割的小写字符串数组
2<= 数组长度 <=100
0< 字符串长度 <=50

输出描述：
两个没有相同字符的元素长度乘积的最大值

示例一
输入
iwdvpbn,hk,iuop,iikd,kadgpf
输出
14
说明
数组中有5个元组，第一个和第二个元素没有相同字符满足条件，输出7*2=14。
说明：
数组中有5个元素。
iwdvpbn与hk无相同的字符，满足条件，iwdvpbn的长度为7，hk的长度为2，乘积为14（7*2）。
iwdvpbn与iuop、iikd、kadgpf均有相同的字符，不满足条件。
iuop与iikd、kadgpf均有相同的字符，不满足条件。
'''

s = input().split(',')
res = 0
for i in range(len(s)):
    for j in range(i, len(s)):
        s1 = s[i]
        s2 = s[j]
        if len(set(s1) & set(s2)) == 0:
            res = max(res, len(s1) * len(s2))
print(res)