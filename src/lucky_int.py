
"""
Given an array of integers arr, a lucky integer is an integer which has a
frequency in the array equal to its value.

Return a lucky integer in the array. If there are multiple lucky integers
return the largest of them. If there is no lucky integer return -1.
"""

def findLucky(arr: list[int]) -> int:
    return max([arr.count(x) for x in arr if x == arr.count(x)], default=-1)

def test_findLucky():
    assert findLucky(arr = [2,2,3,4]) == 2
    assert findLucky(arr = [1,2,2,3,3,3]) == 3
    assert findLucky(arr = [2,2,2,3,3]) == -1

