
from typing import List


def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    start = 0
    end = start + k
    final: List[int] = []
    while end <= len(nums):
        final.append(max(nums[start:end]))
        start += 1
        end += 1
    return final


def test_maxSlidingWindow():
    assert maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3) == [3,3,5,5,6,7]
    assert maxSlidingWindow(nums = [1], k = 1) == [1]
    assert maxSlidingWindow(nums = [1, -1], k = 1) == [1, -1]
    assert maxSlidingWindow(nums = [9, 11], k = 2) == [11]
    assert maxSlidingWindow(nums = [4, -2], k = 2) == [4]

