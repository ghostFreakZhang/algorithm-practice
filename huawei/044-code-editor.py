'''
题目描述：
某公司为了更高效的编写代码，邀请你开发一款代码编辑器程序。
程序的输入为 已有的代码文本和指令序列，程序需输出编辑后的最终文本。指针初始位置位于文本的开头。
支持的指令(X为大于等于0的整数，word为无空格的字符串)：
FORWARD X指针向前(右)移动X，如果指针移动位置超过了文本末尾，则将指针移动到文本末尾
BACKWARD X指针向后(左)移动X，如果指针移动位置超过了文本开头，则将指针移动到文本开头
SEARCH-FORWARD word 从指针当前位置向前查找word并将指针移动到word的起始位置，如果未找到则保持不变
INSERT word在指针当前位置前插入word，并将指针移动到word的结尾
REPLACE word在指针当前位置替换并插入字符(删除原有字符，并增加新的字符)
DELETE X在指针位置删除X个字符

输入描述：
输入的第一行为命令列表的长度
输入的第二行为文件中的原始文
接下来的K行，每行为一个指令

输出描述：
编辑后的最终结果
示例 1
输入
1
ello
INSERT h
输出
hello
说明
在文本开头插入

示例 2
输入
2
hllo
FORWARD 1
INSERT e
输出
hello
说明
在文本的第一个位置插入

示例 3
输入
2
hell
FORWARD 1000
INSERT o
输出
hello
说明
在文本的结尾插入

示例 4
输入
1
hello
REPLACE HELLO
输出
HELLO
说明
替换

示例 5
输入
1
hello
REPLACE HELLO_WORLD
输出
HELLO_WORLD
说明
超过文本长度替换

示例 6
输入
2
hell
FORWARD 10000
REPLACE O
输出
hellO
说明
超出文本长度替换
备注：
文本最长长度不超过256K
'''

n = int(input())
s = input()
index = 0
for _ in range(n):
    op = input().split()
    if op[0] == 'INSERT':
        s = s[:index] + op[1] + s[index:]
        index += len(op[1])
    elif op[0] == 'FORWARD':
        step = int(op[1])
        index += step if index + step < len(s) else len(s)
    elif op[0] == 'BACKWARD':
        step = int(op[1])
        index -= step if index - step >= 0 else 0
    elif op[0] == 'SEARCH-FORWARD':
        target = op[1]
        inc = s[index:].find(target)
        index += 0 if inc == -1 else inc
    elif op[0] == 'REPLACE':
        s = s[:index] + op[1]
        index += len(op[1])
    elif op[0] == 'DELETE':
        step = int(op[1])
        start = index - step if index - step >= 0 else 0
        s = s[:index - step] + s[index:]
print(s)