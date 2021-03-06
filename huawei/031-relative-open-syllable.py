'''
题目描述：
相对开音节构成的结构为辅音+元音（aeiou）+辅音(r除外)+e，常见的单词有bike、cake等。
给定一个字符串，以空格为分隔符，反转每个单词中的字母，若单词中包含如数字等其他非字母时不进行反转。
反转后计算其中含有相对开音节结构的子串个数（连续的子串中部分字符可以重复）。

输入描述:
字符串，以空格分割的多个单词，字符串长度<10000，字母只考虑小写

输出描述:
含有相对开音节结构的子串个数，注：个数<10000

示例1
输入
ekam a ekac
输出
2
说明
反转后为 make a cake 其中make、cake为相对开音节子串，返回2
示例2
输入
!ekam a ekekac
输出
2
说明
反转后为!ekam a cakeke 因!ekam含非英文字符所以未反转，其中 cake、keke为相对开音节子串，返回2
'''

import re
in_str = input().split()
res = 0
for s in in_str:
    if len(s) < 4 or re.match(r'[^a-z]', s):
        continue
    else:
        new_s = s[::-1]
        for i in range(len(new_s) - 3):
            if re.match(r'([b-dhj-np-tv-z][aeiou][b-dhj-npqstv-z]e)+', new_s[i:]):
                res += 1
print(res)