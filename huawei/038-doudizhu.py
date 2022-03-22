'''
题目描述：
在斗地主扑克牌游戏中， 扑克牌由小到大的顺序为：3,4,5,6,7,8,9,10,J,Q,K,A,2，
玩家可以出的扑克牌阵型有：单张、对子、顺子、飞机、炸弹等。
其中顺子的出牌规则为：由 至少 5 张由小到大连续递增 的扑克牌组成，且 不能包含 2 。
例如：{3,4,5,6,7}、{3,4,5,6,7,8,9,10,J,Q,K,A}都是有效的顺子；
而{J,Q,K,A,2}、 {2,3,4,5,6}、{3,4,5,6}、{3,4,5,6,8}等都不是顺子。
给定一个包含13张牌的数组，如果有满足出牌规则的顺子，请输出顺子。
如果存在多个顺子，请每行输出一个顺子，且需要按顺子的 第一张牌的大小（必须从小到大） 依次输出。
如果没有满足出牌规则的顺子，请 输出 No 。

输入描述:
13张任意顺序的扑克牌，每张扑克牌数字用空格隔开，每张扑克牌的数字都是合法的，并且不包括大小王：
2 9 J 2 3 4 K A 7 9 A 5 6
不需要考虑输入为异常字符的情况

输出描述:
组成的顺子，每张扑克牌数字用空格隔开：
3 4 5 6 7
示例1：
输入
2 9 J 2 3 4 K A 7 9 A 5 6
输出
3 4 5 6 7
说明
13张牌中，可以组成的顺子只有1组：3 4 5 6 7
示例2：
输入
2 9 J 10 3 4 K A 7 Q A 5 6
输出
3 4 5 6 7
9 10 J Q K A
说明
13张牌中，可以组成2组顺子，从小到大分别为：3 4 5 6 7 和 9 10 J Q K A
示例3：
输入
2 9 9 9 3 4 K A 10 Q A 5 6
输出
No
说明
13张牌中，无法组成顺子
'''

d = {'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
poker_list = sorted(list(map(int, 
                input().replace('J', d['J'])
                .replace('Q', d['Q'])
                .replace('K', d['K'])
                .replace('A', d['A']).split())))
res = []
index = 0
while index < len(poker_list):
    start = index
    while index + 1 < len(poker_list) and poker_list[index + 1] == poker_list[index] + 1:
        if poker_list[index] == 2:
            break
        index += 1
    if len(poker_list[start:index + 1]) >= 5: res.append(poker_list[start:index + 1])
    index += 1
for r in res:
    r = list(map(str, r))
    for i in range(len(r)):
        d2 = dict(zip(d.values(), d.keys()))
        if r[i] in d2:
            r[i] = d2[r[i]]
    print(' '.join(r))
if not res: print('No')