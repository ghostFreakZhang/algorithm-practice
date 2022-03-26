'''
题目描述：
骰子是一个立方体，每个面一个数字，初始为左 1，右 2，前 3（观察者方向），
后 4，上 5，下 6，用 123456 表示这个状态，放置到平面上。
可以向左翻转（用 L表示向左翻转 1 次）
可以向右翻转（用 R 表示向右翻转 1 次）
可以向前翻转（用 F 表示向前翻转 1 次）
可以向后翻转（用 B 表示向后翻转 1 次）
可以逆时针旋转（用 A表示逆时针旋转 90 度）
可以顺时针旋转（用 C 表示顺时针旋转 90 度）
现从 123456 这个初始状态开始，根据输入的动作序列，计算得到最终的状态。
骰子的初始状态和初始状态转动后的状态如图所示。
https://blog.nowcoder.net/n/6f5332660f33473c88addc740480c861

输入描述：
输入一行，为只包含 LRFBAC 的字母序列，最大长度 50，字母可重复。

输出描述：
输出最终状态。

示例 1：
输入
LR
输出
123456
'''

ops = list(input())
arr = ['1', '2', '3', '4', '5', '6']
for op in ops:
    if op == "L":
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[4], arr[5], arr[2], arr[3], arr[1], arr[0]
    elif op == 'R':
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[5], arr[4], arr[2], arr[3], arr[0], arr[1]
    elif op == 'F':
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[0], arr[1], arr[4], arr[5], arr[3], arr[2]
    elif op == 'B':
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[0], arr[1], arr[5], arr[4], arr[2], arr[3]
    elif op == 'A':
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[3], arr[2], arr[0], arr[1], arr[4], arr[5]
    elif op == 'C':
        arr[0], arr[1], arr[2], arr[3], arr[4], arr[5] = arr[2], arr[3], arr[1], arr[0], arr[4], arr[5]
print(''.join(arr))