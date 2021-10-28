"""
Given 2 integers n and start. Your task is return any permutation p of (0,1,2.....,2^n -1) such that :

    p[0] = start
    p[i] and p[i+1] differ by only one bit in their binary representation.
    p[0] and p[2^n -1] must also differ by only one bit in their binary representation.
"""

from typing import List

def circularPermutation(n: int, start: int) -> List[int]:
    temp_list = []
    for i in range(2**n):
        temp_list.append(i^(i>>1))
    start_idx = temp_list.index(start)
    print(temp_list)
    return temp_list[start_idx:] + temp_list[0:start_idx]


print(circularPermutation(3, 2))


# def test_circularPermutation():
#     temp = circularPermutation(3, 3)
#     print([bin(x) for x in temp])
#     temp_bin_list = [bin(x ^ temp[i+1]) for i,x in enumerate(temp[:-1])]
#     print(temp_bin_list)

