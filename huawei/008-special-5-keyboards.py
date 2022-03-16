'''
题目描述：
有一个特殊的五键键盘，上面有A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A A键在屏幕上输出一个字母A，Ctrl-C将当前所选的字母复制到剪贴板，Ctrl-X将当前选择的字母复制到剪贴板并清空所选择的字母，Ctrl-V将当前剪贴板的字母输出到屏幕，Ctrl-A选择当前屏幕中所有字母

条件如下：
剪贴板初始为空
新的内容复制到剪贴板会覆盖原有内容
当屏幕中没有字母时,Ctrl-A无效
当没有选择字母时Ctrl-C、Ctrl-X无效
当有字母被选择时A和Ctrl-V这两个输出功能的键，会先清空所选的字母再进行输出
给定一系列键盘输入，输出最终屏幕上字母的数量

输入描述：
输入为一行，为简化解析用数字12345分别代替A、Ctrl-C、Ctrl-X、Ctrl-V、Ctrl-A的输入，数字用空格分割

输出描述：
输出一个数字为屏幕上字母的总数量

示例1：
输入
1 1 1
输出
3
说明
连续键入3个a，故屏幕上字母的长度为3

示例2：
输入
1 1 5 1 5 2 4 4
输出
2
说明
输入两个a后ctrl-a选择这两个a，再输入a时选择的两个a先被清空，所以此时屏幕只有一个a，后续的ctrl-a，ctrl-c选择并复制了这一个a，最后两个ctrl-v在屏幕上输出两个a，故屏幕上字母的长度为2（第一个ctrl-v清空了屏幕上的那个a）
'''

op = input().split()
res = ''
clipboard = ''
choose = ''
for o in op:
    if o == '1':
        if choose:
            res = 'a'
        else:
            res += 'a'
    elif o == '2':
        clipboard = choose
    elif o == '3':
        clipboard = choose
        res = ''
    elif o == '4':
        if choose:
            res = clipboard
            choose = ''
        else:
            res += clipboard
    elif o == '5':
        choose = res
print(len(res))
    