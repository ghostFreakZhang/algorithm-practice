'''
题目描述：
将一段压缩后的字符串解压缩，并且排序输出。

解压规则：
每个字符串后面跟随一个数字，表示这个字符串的重复次数。
例如，“a5”解压缩的结果为“aaaaa”；“abc3”解压缩后的结果为“abcabcabc”。

排序规则：
根据每个字符串的重复次数升序排序，然后输出结果。例如，“a3b2”，输出的结果为“bbaaa”。
如果字符重复次数一样，则根据 ASCII 编码顺序做升序排序，然后输出结果。例如，“b2a2”，输出的结果为“aabb”

输入描述：
输入的原始字符串仅包含字母和数字

输出描述：
输出的结果字符串仅包含字母

示例 1
输入：
a11b2bac3bad3abcd2
输出：
bbabcdabcdbacbacbacbadbadbadaaaaaaaaaaa
注：原题给的示例输出结果有问题，abcd和b数量虽然都为2，但abcd的ASCII码小于b，所以先输出abcd。
'''

import re
s = input()
nums = list(map(int, re.findall(r'(\d+)', s)))
item = re.findall(r'([a-z]+)', s)
d = dict(zip(item, nums))
sort_key = sorted(d, key = lambda x: (d[x], x))
res = ''
for k in sort_key:
    res += k * d[k]
print(res)