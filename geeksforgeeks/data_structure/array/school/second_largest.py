"""
Given an array A of size N, print second largest element from an array.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line contains an integer N denoting the size of the array. The second line contains the N space seperated intgers of the array

Output:
For each testcase, in a new line, print the second largest element.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 500
1 ≤ Ai ≤ 1200

Example:
Input
2
5
89 24 75 11 23
6
56 42 21 23 65 20
Output
75
56
"""


def second_largest(arr):
    arr.sort()
    return arr[-2]


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        second_value = (lambda x: second_largest([int(i) for i in x.split()]))(input())
        print(second_value)
