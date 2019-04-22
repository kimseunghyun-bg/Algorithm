"""
Given a binary array A[] of size N. The task is to arrange array in increasing order.

Note: The binary array contains only 0  and 1.

Input:
The first line of input contains an integer T, denoting the testcases. Every test case contains two lines, first line is N(size of array) and second line is space separated elements of array.

Output:
Space separated elements of sorted arrays. There should be a new line between output of every test case.

Constraints:
1 < = T <= 100
1 <= N <= 106
0 <= A[i] <= 1

Example:
Input:
2
5
1 0 1 1 0
10
1 0 1 1 1 1 1 0 0 0

Output:
0 0 1 1 1
0 0 0 0 1 1 1 1 1 1
"""


def binary_array_sorting(arr):
    arr.sort()
    return arr


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        arr = (lambda x: binary_array_sorting([int(i) for i in x.split()]))(input())
        print(str(arr)[1:-1].replace(",", ""))
