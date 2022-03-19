'''
题目描述：
现有一字符串仅由 '('， ')'， '{'， '}'， '['， ']'六种括号组成。 若字符串满足以下条件之一，则为无效字符串：
1、任一类型的左右括号数量不相等；
2、存在未按正确顺序（先左后右）闭合的括号。
输出括号的最大嵌套深度，若字符串无效则输出 0。 0≤字符串长度≤100000

输入描述:
一个只包括 '('， ')'， '{'， '}'， '['， ']'的字符串

输出描述:
一个整数，最大的括号深度

示例1
输入
[]
输出
1
说明
有效字符串，最大嵌套深度为1
示例2
输入
([]{()})
输出
3
说明
有效字符串，最大嵌套深度为3
示例3
输入
(]
输出
0
说明
无效字符串，有两种类型的左右括号数量不相等
示例4
输入
([)]
输出
0
说明
无效字符串，存在未按正确顺序闭合的括号
示例5
输入
)(
输出
0
说明
无效字符串，存在未按正确顺序闭合的括号
'''

in_str = input()
stack = []
depth = 0
error = False
for s in in_str:
    if s == '(' or s == '{' or s == '[':
        stack.append(s)
        depth = len(stack)
    elif s == ')':
        if not stack or stack.pop() != '(':
            error = True
    elif s == '}':
        if not stack or stack.pop() !=  '{':
            error = True
    elif s == ']':
        if not stack or stack.pop() != '[':
            error = True
print(0) if error else print(depth)