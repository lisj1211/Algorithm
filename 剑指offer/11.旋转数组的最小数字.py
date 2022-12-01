# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 给你一个可能存在重复元素值的数组numbers，它原来是一个升序排列的数组，并按上述情形进行了一次旋转。
# 请返回旋转数组的最小元素。例如，数组[3,4,5,1,2] 为 [1,2,3,4,5] 的一次旋转，该数组的最小值为 1。
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
#
# 输入：numbers = [3,4,5,1,2]
# 输出：1
from typing import List


# 方法一： 排序
def min_array(numbers: List[int]) -> int:
    return min(numbers)


# 方法二： 二分
def min_array1(numbers: List[int]) -> int:
    if len(numbers) == 1:
        return numbers[0]

    l, r = 0, len(numbers) - 1
    while l < r:
        mid = l + ((r - l) >> 1)
        if numbers[mid] == numbers[r] == numbers[l]:  # 特殊情况，如[3, 3, 1, 3]
            l += 1
            r -= 1
        elif numbers[mid] > numbers[r]:
            l = mid + 1
        else:
            r = mid

    return numbers[l]



