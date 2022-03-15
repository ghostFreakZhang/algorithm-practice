'''
题目描述：
有一个N个整数的数组，和一个长度为M的窗口，窗口从数组内的第一个数开始滑动直到窗口不能滑动为止，每次窗口滑动产生一个窗口和（窗口内所有数的和），求窗口滑动产生的所有窗口和的最大值。

输入描述:
第一行输入一个正整数N，表示整数个数。(0<N<100000)
第二行输入N个整数，整数的取值范围为[-100,100]。
第三行输入一个正整数M，M代表窗口大小，M<=100000，且M<=N。

输出描述:
窗口滑动产生的所有窗口和的最大值。

示例1：
输入
6
10 20 30 15 23 12
3
输出
68
说明
窗口长度为3，窗口滑动产生的窗口和分别为10+20+30=60，20+30+15=65，30+15+23=68，15+23+12=50，所以窗口滑动产生的所有窗口和的最大值为68。
'''

nums = int(input())
nums_list = list(map(int, input().split()))
windows = int(input())
max_ = sum(nums_list[:windows])
for i in range(nums - windows):
    sum_ = sum(nums_list[i:i + windows])
    if sum_ > max_:
        max_ = sum_
print(max_)