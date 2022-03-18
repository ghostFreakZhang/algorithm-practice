'''
题目描述：
输入一个字符串仅包含大小写字母和数字，求字符串中包含的最长的非严格递增连续数字序列的长度（比如12234属于非严格递增连续数字序列）。

输入描述:
输入一个字符串仅包含大小写字母和数字，输入的字符串最大不超过255个字符。

输出描述:
最长的非严格递增连续数字序列的长度

示例1：
输入
abc2234019A334bc
输出
4
说明
2234为最长的非严格递增连续数字序列，所以长度为4。
'''

import re
nums_list = re.findall(r'(\d+)', input())
max_ = 1 if len(nums_list) > 0 else 0
for nums in nums_list:
    num_len = 1
    for i in range(1, len(nums)):
        if int(nums[i]) >= int(nums[i-1]):
            num_len += 1
        else:
            num_len = 1
        if num_len > max_:
            max_ = num_len
print(max_)