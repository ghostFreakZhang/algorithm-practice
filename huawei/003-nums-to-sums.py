'''
题目描述：
一个整数可以由连续的自然数之和来表示。给定一个整数，计算该整数有几种连续自然数之和的表达式，且打印出每种表达式。

输入描述:
一个目标整数T (1 <=T<= 1000)

输出描述:
该整数的所有表达式和表达式的个数。如果有多种表达式，输出要求为：
1.自然数个数最少的表达式优先输出
2.每个表达式中按自然数递增的顺序输出，具体的格式参见样例。在每个测试数据结束时，输出一行”Result:X”，其中X是最终的表达式个数。

示例1
输入
9
输出
9=9
9=4+5
9=2+3+4
Result:3
说明
整数 9 有三种表示方法，第1个表达式只有1个自然数，最先输出，第2个表达式有2个自然数，第2次序输出，第3个表达式有3个自然数，最后输出。每个表达式中的自然数都是按递增次序输出的。
数字与符号之间无空格
'''

num = int(input())
nums_list = list(range(1, num + 1))
res = []
for i in range(num):
    for j in range(1, num + 1):
        if sum(nums_list[i:j]) == num:
            res.append('+'.join(map(str, nums_list[i:j])))
res.sort(key=lambda x: len(x))
for r in res:
    print(f'{num}={r}')
print(f'Result:{len(res)}')