'''
题目描述：
输入待匹配的关键字，和一串固定格式的字符串中，提取符合关键字要求的寄存器地址，寄存器掩码，寄存器值。
一串固定格式的字符串由一个或者多个这样的信息组成：XXX[addr=0xYYY,mask=0xZzz,val=0xWWW]
匹配规则为：
1）左中括号前面的关键字完全匹配 
2）中括号里面匹配到"addr="后面的数字是寄存器地址，"mask="后面的数字是寄存器掩码，"val="后面的数字是寄存器值， 三个都匹配到认为满足。
满足1和2认为匹配到，逐行输出每个条目的寄存器地址，寄存器掩码，寄存器值信息。
否则匹配失败输出：FAIL 
其他约束:
1）字符串中全部为英文标点符号，不考虑中文 
2）关键字匹配时大小写不一致认为是匹配失败，输出的寄存器信息允许有大和小写，
3）输入寄存器要求必须十六进制（0x或者0X），寄存器信息允许有大和小写，如0xFF 0xa0。

输入例子：
read read[addr=0x17,mask=0xff,val=0x7],read_his[addr=0xff,mask=0xff,val=0x1],read[addr=0xf0,mask=0xff,val=0x80]

输出：
0x17 0xff 0x7
0xf0 0xff 0x80
'''

import re
target, source = input().split()
data = re.findall(r'(\w*?\[.*?\])', source)
for d in data:
    res = re.findall(r'%s\[addr=(.*?),mask=(.*?),val=(.*?)\]' % target, d)
    if len(res) > 0:
        for r in res:
            print(' '.join(r))
    else:
        print('FAIL')