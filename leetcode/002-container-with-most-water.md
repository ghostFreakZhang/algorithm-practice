## 题目内容

[盛最多水的容器题目链接](https://leetcode-cn.com/problems/container-with-most-water/)

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

输入：[1,8,6,2,5,4,8,3,7]

输出：49 

解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

## 题解

- 直接暴力解法

执行超时，通过80%左右用例

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, (j - i) * min(height[i], height[j]))
        return res
```

- 双指针解法

两端向中间收缩的双指针

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while right > left:
            res = max(res, (right - left) * min(height[right], height[left]))
            # 移动较低的一边，移动高边肯定不会有更大的面积
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return res
```

- 优化速度的双指针

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        maxh = max(height)
        while right > left:
            res = max(res, (right - left) * min(height[right], height[left]))
            # 移动较低的一边，移动高边肯定不会有更大的面积
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
            if res >= maxh * (right - left):
                break
        return res
```