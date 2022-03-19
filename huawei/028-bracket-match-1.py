'''
题目描述：
给定一个字符串，里边可能包含“()”、“[]”、“{}”三种括号，请编写程序检查该字符串中的括号是否成对出现，且嵌套关系正确。

输出：
true:若括号成对出现且嵌套关系正确，或该字符串中无括号字符；
false:若未正确使用括号字符。
实现时，无需考虑非法输入。

输入描述：
输入为：字符串
(1+2)/(0.5+1)

输出描述：
输出为：字符串
true
'''

import re
in_str = re.findall(r'([\(\)\[\]\{\}])', input())
stack = []
error = False
for s in in_str:
    if s == '(' or s == '{' or s == '[':
        stack.append(s)
    elif s == ')':
        if not stack or stack.pop() != '(':
            error = True
    elif s == '}':
        if not stack or stack.pop() !=  '{':
            error = True
    elif s == ']':
        if not stack or stack.pop() != '[':
            error = True
print('false') if error else print('true')