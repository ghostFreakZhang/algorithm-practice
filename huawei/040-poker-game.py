'''
题目描述：
有一种游戏，每个人手上有一些不同颜色和数字的卡牌。
上一个人发完牌后，下一个人可以出同样的颜色或数字的卡牌。
下面第一行输入数字，第二行输入颜色，请输出最优策略可以打出牌的数量。
输入
1 4 3 4 5
r y b b r
输出 
3
'''
nums = input().split()
colors = input().split()
poker_list = list(map(lambda x, y: x + y, nums, colors))
n = len(nums)
matrix = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if poker_list[i][0] == poker_list[j][0] or poker_list[i][1] == poker_list[j][1]:
            matrix[i][j] = 1
visited = [False] * len(poker_list)
max_ = 0
temp = 0
for index in range(n):
    if visited[index]:
        continue
    else:
        q = [index]
        visited[index] = True
    while q:
        i = q.pop()
        temp += 1
        for j in range(n):
            if matrix[i][j] == 1 and not visited[j] and i != j:
                q.append(j)
                visited[j] = True
    max_ = max(max_, temp)
    temp = 0
print(max_)