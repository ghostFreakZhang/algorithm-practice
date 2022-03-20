'''
题目描述：
给你一串未加密的字符串str，通过对字符串的每一个字母进行改变来实现加密，加密方式是在每一个字母str[i]偏移特定数组元素a[i]的量，
数组a前三位已经赋值：a[0]=1,a[1]=2,a[2]=4。
当i>=3时，数组元素a[i]=a[i-1]+a[i-2]+a[i-3]，
例如：原文 abcde 加密后 bdgkr，其中偏移量分别是1,2,4,7,13。

输入描述:
第一行为一个整数n（1<=n<=1000），表示有n组测试数据，每组数据包含一行，原文str（只含有小写字母，0<长度<=50）。

输出描述:
每组测试数据输出一行，表示字符串的密文

示例1
输入
1
xy
输出
ya
说明
第一个字符x偏移量是1，即为y，第二个字符y偏移量是2，即为a
示例2
输入
2
xy
abcde
输出
ya
bdgkr
说明
第二行输出字符偏移量分别为1、2、4、7、13
'''

n = int(input())
for _ in range(n):
    s = input()
    a = [1, 2, 4]
    res = ''
    for i in range(len(s)):
        if i > 2:
            a.append(a[i - 1] + a[i - 2] + a[i - 3])
        code = ord(s[i]) + a[i]
        code = code if code < 123 else 123 - code + 97
        res += chr(code)
    print(res)