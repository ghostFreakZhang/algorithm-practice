'''
题目描述：
小组中每位都有一张卡片，卡片上是6位内的正整数，将卡片连起来可以组成多种数字，计算组成的最大数字。

输入描述:
","号分割的多个正整数字符串，不需要考虑非数字异常情况，小组最多25个人

输出描述:
最大的数字字符串

示例1
输入
22,221
输出
22221
示例2
输入
4589,101,41425,9999
输出
9999458941425101
'''

nums = input().split(',')
max_len = len(sorted(nums, key = lambda x: len(x), reverse = True)[0])
d = dict()
dup_num = []
for num in nums:
    new_num = num.ljust(max_len, '0')
    if new_num in d:
        dup_num.append(new_num)
    padding = max_len - len(num)
    d[new_num] = padding
order_nums = sorted(list(d.keys()) + dup_num, reverse = True)
res = ''
for n in order_nums:
    res += n[:len(n) - d[n]]
print(res)