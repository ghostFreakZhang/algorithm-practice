'''
题目描述：
请一个在字符串中找出连续最长的数字串，并返回这个字符串；如果存在长度相同的连续数字串，返回最后一个连续数字串；
注意：
数字串是由数字和“.”组成的（长度包括“.”在内），“.”两边必须是数字，比如： 数字串“1234”的长度就小于数字串“00055”，数字串“1234.56789”的长度大于数字串“123456789”

输入描述：
字符串输入为 ASCLL 编码，长度不定，可能含有空格，请读取完整一行数据作为输入

输出描述：
如果没有符合条件的数字串，返回空字符串“”

示例 1
输入：
abcd123.4567.890.123
abcd12345ed125ss123058789
abcd12345ss54761
输出
4567.890
123058789
54761
'''

import re
nums = re.findall(r'([\d\.]+)', input())
max_len = 0
res = ''
for index in range(len(nums)):
    if '.' in nums[index]:
        dot_count = nums[index].count('.')
        num = list(filter(None, nums[index].split('.')))
        for j in range(len(num) - 1):
            tmp = f'{num[j]}.{num[j + 1]}'
            if len(tmp) >= max_len:
                res = tmp
                max_len = len(tmp)
    else:
        if len(nums[index]) >= max_len:
            res = nums[index]
            max_len = len(nums[index])
print(res)