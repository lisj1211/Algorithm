# -*- coding: utf-8 -*-
# 你这个学期必须选修 numCourses 门课程，记为0到numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites 给出，其中prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/course-schedule
from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        next_course = defaultdict(list)
        for course, pre in prerequisites:
            in_degree[course] += 1
            if pre not in in_degree:
                in_degree[pre] = 0
            next_course[pre].append(course)

        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            cur = queue.popleft()
            numCourses -= 1
            if next_course[cur]:
                for i in next_course[cur]:
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)
        return numCourses == 0


class Solution1:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = defaultdict(int)
        next_course = defaultdict(list)

        for cur, pre in prerequisites:
            next_course[cur].append(pre)
            in_degree[pre] += 1

        queue = deque()
        for cur, pre_num in in_degree.items():
            if pre_num == 0:
                queue.append(cur)

        while queue:
            cur = queue.popleft()
            numCourses -= 1
            for next_ in next_course[cur]:
                in_degree[next_] -= 1
                if in_degree[next_] == 0:
                    queue.append(next_)

        return numCourses == 0


s = Solution1()
s.canFinish(2, [[1,0]])