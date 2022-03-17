'''
题目描述：

给定多组原本的航班预订信息（航班号，座位号，乘客姓名），以及多组要改签的航班信息（原本航班号，原本座位号，新航班号，新座位号）
输出最后的航班预订信息，要是有重复的内容，以最新改签的为标准

输入内容如下：

3 表示原本的航班信息数，2表示要改签的航班数
3
CZ7132,A1,ZHANGSAN
CZ7132,A2,ZHAOSI
CZ7156,A2,WANGWU
2
CZ7132,A1,CZ7156,A2
CZ7156,A2,CZ7156,A3

输出内容如下：
CZ7132,A2,ZHAOSI
CZ7156,A2,ZHANGSA
CZ7156,A3,WANGW
按照航班号、座位号排序
'''
ori_n = int(input())
ori_list = []
for _ in range(ori_n):
    ori_list.append(input().split(','))
adjust_n = int(input)
adjust_list = []
for _ in range(adjust_n):
    adjust_list.append(input().split(','))

for o in ori_list:
    flag = False
    for a in adjust_list:
        if o[0] == a[0] and o[1] == a[1]:
            o0 == a[2]
            o1 == a[3]
            flag = True
    if flag:
        o[0] == o0
        o[1] == o1
order_ori_list = sorted(ori_list, key = lambda x: (x[0], x[1]))
for v in order_ori_list:
    print(','.join(v))