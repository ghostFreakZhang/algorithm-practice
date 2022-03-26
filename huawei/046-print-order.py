'''
题目描述：
某个打印机根据打印队列执行打印任务。打印任务分为九个优先级，分别采用数字1~9表示，数字越大优先级越高。
打印机每次从队列头部取出第一个任务A，然后检查队列余下任务中有没有比A优先级更高的任务，
如果有比A优先级高的任务，则将任务A放到队列尾部，否则执行任务A的打印。
请编写一个程序，根据输入的打印队列，输出实际打印顺序。

输入描述：
输入一行，为每个任务的优先级，优先级之间用逗号隔开，优先级取值范围是 1~9

输出描述：
输出一行，为每个任务的打印顺序，打印顺序从0开始，用逗号隔开

示例1
输入输出示例仅供调试，后台判题数据一般不包含示例
输入
9,3,5
输出
0,2,1
说明
队列头部任务的优先级为9，最先打印，故序号为0；
接着队列头部任务优先级为3，队列中还有优先级为5的任务，优先级3任务被移到队列尾部；
接着打印优先级为5的任务，故其序号为1；
最后优先级为3的任务的序号为2
'''

from collections import deque
ori_task = input().split(',')
task = deque(ori_task)
res = [None] * len(task)
index = 0
while task:
    flag = False
    head = task[0]
    for t in task:
        if t > head:
            flag = True
    task.popleft()
    if flag:
        task.append(head)
    else:
        for i in range(len(ori_task)):
            if ori_task[i] == head and not res[i]:
                res[i] = index
                index += 1
print(','.join(list(map(str, res))))