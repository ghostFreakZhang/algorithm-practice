'''
数字反转
题目描述：
如果数字多行排列，第一行1个数，第二行2个，第三行3个，#即第n行有n个数字，并且奇数行正序排列，偶数行逆序排列，数字依次累加。规则总结如下：
a、每个数字占据4个位置，不足四位用*补位，如1打印为1***。
b、数字之间相邻4空格。
c、数字的打印顺序按照正序逆序交替打印，奇数行正序，偶数行逆序。
d、最后一行数字顶格，第n-1行相对第n行缩进四个空格

输入描述：
第一行输入为N，表示打印多少行；1<=N<=30
输入：2

输出描述：
XXXX1***
3***XXXX2***
备注：
符号*表示，数字不满4位时的补位，符号X表示数字之间的空格。注意实际编码时不需要打印X，直接打印空格即可。此处为说明题意，故此加上X

示例1：
输入
2
输出
    1***
3***    2***
'''
n = int(input())
end = 1
for i in range(1, n + 1):
    flag = True if i % 2 == 0 else False
    tab = '    ' * (n - i)
    nums = sorted(list(range(end, end + i)), reverse = flag)
    end = nums[-1] + 1 if not flag else nums[0] + 1
    str_nums = list(map(lambda x: str(x).ljust(4, '*') if len(str(x)) < 4 else x, nums))
    print(tab + '    '.join(str_nums))