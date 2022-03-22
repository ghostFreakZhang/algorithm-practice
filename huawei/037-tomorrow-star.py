'''
题目描述：
某项目组组织举办“明日之星”评选活动，投票采用无记名方式，投票后整理出投票清单，最后根据投票和评选规则选出一名“明日之星”。
要求：
1、票数最多者当选
2、票数相同的，根据员工姓名排序，字母序号越小排前面，a>b>c,A>B>C;
清单必须由英文字母和英文逗号组成，否则作废，返回error.0001;
名字必须为大写字母开头，剩下为小写字母，否则返回error.0001;

输入描述：
投票姓名之间用英文逗号隔开，中间不带空格。
例如：
Tom,Lily,Tom,Lucy,Lucy,Jack
输出：Lucy
'''

import re
voter_list = input()
error = False
if re.match(r'[^A-Za-z,]+', voter_list):
    error = True
dic = dict()
for voter in voter_list.split(','):
    if not voter.istitle() or re.findall(r'[^A-Za-z]+', voter):
        error = True
        break
    else:
        dic[voter] = dic.setdefault(voter, 0) + 1
res = list(sorted(dic, key = lambda x: (-dic[x], x)))
print(res[0]) if not error else print('error.0001')