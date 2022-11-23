# 轮询机制的设计
# 给定一个字符串列表，每次选取一个字符串的第一个字符
# ['ABC', 'D', 'EF'] --> A D E B F C
from collections import deque


def roundrobin(*iterables):
    iterators = deque(map(iter, iterables))
    while iterators:
        try:
            while True:
                yield next(iterators[0])
                iterators.rotate(-1)
        except StopIteration:
            iterators.popleft()


if __name__ == '__main__':
    print(list(roundrobin('ABC', 'D', 'EF')))
