'''
题目描述:
公司用一个字符串来表示员工的出勤信息：
absent：缺勤
late：迟到
leaveearly：早退
present：正常上班
现需根据员工出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下：
缺勤不超过一次；没有连续的迟到/早退；任意连续7次考勤，缺勤/迟到/早退不超过3次

输入描述:
用户的考勤数据字符串，记录条数 >= 1；输入字符串长度<10000；不存在非法输入

输出描述:
根据考勤数据字符串，如果能得到考勤奖，输出"true"；否则输出"false"，对于输入示例的结果应为：

示例1：
输入
2
present
present present
输出
true true

示例2：
输入
2
present
present absent present present leaveearly present absent
输出
true false
'''

num = int(input())
res = []
for _ in range(num):
    info = input().split()
    flag = True
    if info.count('absent') > 1:
        res.append('false')
        continue
    for i in range(len(info) - 1):
        if info[i] == 'late' or info[i] == 'leaveearly':
            if info[i + 1] == 'late' or info[i + 1] == 'leaveearly':
                flag = False
                break
    if len(info) >= 7:
        for i in range(len(info) - 6):
            info_list = info[i:i + 7]
            if info_list.count('absent') + info_list.count('late') + info_list.count('leaveearly') > 3:
                flag = False
    res.append('true') if flag else res.append('false')
print(' '.join(res))