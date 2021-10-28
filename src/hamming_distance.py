"""
The Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
"""


def hammingDistance(x: int, y: int) -> int:
    n = x ^ y
    count = 0
    while n != 0:
        n = n & (n-1)
        count += 1
    return count

def test_hammingDistance():
    assert hammingDistance(1,4) == 2
    assert hammingDistance(3,1) == 1
