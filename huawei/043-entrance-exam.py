'''
题目描述：
升学考试包括三门基础学科，基础学科分别为语文、数学、英语。10名学生参加考试，录取条件：
（1）每门基础学科考试总分100分，及格成绩为60分。
（2）没有不及格科目
（3）录取排名前三的考生。
约束限制：
（1）优先考察基础学科总分排名
（2）基础学科总分相同时，排名再依次分别查看单科语文、数学、英语三门单科成绩。
（3）如果考生成绩完全相同时，排名也相同。同一个排名的可能存在多位考生。最终录取人数可能多于或者少于3人。
（4）按照总分从大到小排名
（5）排名相同时，按姓名（汉语拼音，最多10个字母）的ASCII码从小到大排序
（6）排序后，分别输出考试合格考生的名单和被录取名单。
（7）分数输入范围为0-100，包括0和100，不需要考虑异常
（8）学生数量为10名，不需要考虑其他数量
（9）名字长度超过10不需要考虑
（10）名字不需要考虑重名

输入描述：
每一行依次输入姓名、语文、数学、英语三门学科分数，中间为单个空格隔开
每一个考生的成绩只在同一行，同一行只有一位考生成绩

输出描述：
（1）输出考试合格考生名单，先打印[First round name list]
（2）输出被录取考生名单，先打印[Final name list]
按顺序打印出姓名、语文、数学、英语三门学科分数，之间用单个空格分离
每打印一名考生成绩换行
合格考生名单和被录取考生之间用一个空行隔开

输入
goudan2 60 80 80
zhaowu 60 80 80
zhangsan 60 80 80
yatou 90 80 80
goudan1 60 80 80
gousheng 80 100 60
lilei 80 100 60
hanmingmei 80 90 60
liutao 80 100 60
SimonYin 80 100 60
输出
[First round name list]
yatou 90 80 80
SimonYin 80 100 60
gousheng 80 100 60
lilei 80 100 60
liutao 80 100 60
hanmingmei 80 90 60
goudan1 60 80 80
goudan2 60 80 80
zhangsan 60 80 80
zhaowu 60 80 80
 
[Final name list]
yatou 90 80 80
SimonYin 80 100 60
gousheng 80 100 60
lilei 80 100 60
liutao 80 100 60
hanmingmei 80 90 60
'''

record = []
for _ in range(10):
    s1 = input().split()
    s2 = list(map(int, s1[1:]))
    record.append(s1[:1] + s2)
record = list(filter(lambda x: x[1] >= 60 and x[2] >= 60 and x[3] >= 60, record))
record = sorted(record, key = lambda x: (-(x[1] + x[2] + x[3]), -x[1], -x[2], -x[3], x[0]))
print('[First round name list]')
for r in record:
    print(f'{r[0]} {str(r[1])} {str(r[2])} {str(r[3])}')
limit = 3
i = 0
while i < len(record):
    start = i
    r = record[i]
    while i + 1 < len(record) and i < limit - 1 and record[i][1] == record[i + 1][1] and record[i][2] == record[i + 1][2] and record[i][3] == record[i + 1][3]:
        limit += 1
        i += 1
    i += 1
print('[Final name list]')
for r in record[:limit]:
    print(f'{r[0]} {str(r[1])} {str(r[2])} {str(r[3])}')