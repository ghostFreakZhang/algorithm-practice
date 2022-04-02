'''
题目描述：
近些年来，我国防沙治沙取得显著成果。
某沙漠新种植N棵胡杨(编号1-N) 排成一排。一个月后，有M棵胡杨未能成活。
现可补种胡杨K棵，请问如何补种（只能补种，不能新种） ，可以得到最多的连续胡杨树?

输入描述：
N 总种植数量
M 未成活胡杨教量
M 个空格分隔的数，按编号从小到大排列
K 最多可以补种的数量
其中：
1<= N <=100000
1<= M <=N
0<= K <=M

输出描述：
最多的连续胡杨棵树

示例1：
输入
5
2
2 4
1
输出
3
说明：补种到2和4结果一样，最多的连续胡杨棵树都是3
示例2：
输入
10
3
2 4 7
1
输出
6
说明：补种第7棵树，最多的连续胡杨棵树为6（5、6、7、8、9、10）
'''

n = int(input())
m = int(input())
dead = [0]
dead.extend(list(map(int, input().split())))
dead.append(n + 1)
k = int(input())
res = 0
index = 1
while index + k - 1 <= m:
    print(dead[index+k], dead[index-1])
    res = max(res, dead[index + k] - dead[index - 1]) - 1
    index += 1
print(res)