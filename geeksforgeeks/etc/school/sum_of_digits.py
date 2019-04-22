"""
Given an integer N. The task is to find sum of all digits of N.

Input:
The first line of input contains an integer T, total number of testcases. Then following T lines contains an integer N.

Output:
For each testcase in a new line, print the sum of digits of N.

Constraints:
1 ≤ T ≤ 30
1 ≤ N ≤ 103

Example:
Input:
2
123
45

Output:
6
9

Explanation:
Testcase 1: The sum of digits the given number 123: 1 + 2 +3 = 6.
"""


def sum_of_digits(digits):
    sum_val = 0
    for i in str(digits):
        sum_val += int(i)
    return sum_val


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(0, test_cases):
        print(sum_of_digits(input()))
