'''
题目描述：
字符串中没有数字，全是小写字母，对该二进制文件进行压缩。
规则1：连续相同的字母，使用数字来表示重复出现的个数，bbbccc压缩成b3c3，但是如果只有两个连续的字母，压缩之后没有收益，不压缩，如bb就不再压缩:
规则2：对于重复出现的连续子串，压缩为大写子串加重复数字，例如abcabcabc压缩成ABC3;
规则3：重复字母和重复子串同时出现，优先进行重复子串的压缩，例如aaaabcabc,压缩成a3ABC2;
规则4：有多个重复子串时，优先压缩最长的重复子串，例如aaaabcabcaaaabcabc,压缩成AAAABCABC2;

输入：
aaaabcaabcaabcaabc

输出：
aaAABC4
'''

'''
目前只想到如此暴力的解法, 效率极低, 后面再填坑吧...
'''

import re
string = input()
str_list = list(string)
str_len = len(str_list)
res = []
for i in range(str_len):
    for j in range(str_len, i, -1):
        str_ori = ''.join(str_list)
        sub_str = ''.join(str_list[i:j])
        mid = len(sub_str) // 2
        while len(set(sub_str)) > 2 and sub_str[:mid] and sub_str[:mid] == sub_str[mid:]:
            sub_str = sub_str.replace(sub_str, sub_str[:mid])
            mid = len(sub_str) // 2
        count = str_ori.count(sub_str)
        if len(set(sub_str)) > 2 and count >= 2:
            sub_start = [substr.start() for substr in re.finditer(sub_str, str_ori)]
            for start in sub_start:
                for index in range(len(sub_str)):
                    str_list[start + index] = ''
            res.append((i, sub_str, count))
index = 0
while index <= len(str_list) - 1:
    start = index
    if not str_list[index]:
        index += 1
        continue
    while index + 1 < len(str_list) and str_list[index] == str_list[index + 1]:
        index += 1
    res.append((start, str_list[index], index - start + 1))
    index += 1
out = ''
for r in sorted(res, key = lambda x: x[0]):
    if len(r[1]) == 1 and r[2] > 2:
        out += r[1] + str(r[2])
    elif len(r[1]) == 1 and r[2] <= 2:
        out += r[1] * r[2]
    else:
        out += r[1].upper() + str(r[2])
print(out)