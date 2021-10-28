"""
Given an integer n, return an array ans of length n + 1 such that for each i (0
<= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

def countBits(n: int) -> list[int]:
    val = 0
    ans = []
    for i in range(0, n+1):
        while i:
            i &= (i-1)
            val += 1
        ans.append(val)
        val = 0
    return ans

def test_countBits():
    assert countBits(n = 2) == [0,1,1]
    assert countBits(n = 5) == [0,1,1,2,1,2]
