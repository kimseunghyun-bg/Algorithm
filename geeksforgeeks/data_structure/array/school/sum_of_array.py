"""
Given an integer array A[] of size N. The task is to find sum of it.

Input:
The first line of input contains an integer, the number of testcases T. Each testcase should contain an integer, size of array N in the first line. In the second line contains elements of the array in a single line separated by space.

Output:
Print the sum in seperate line.

Constraints:
1 <= T <= 30
1 <= N <= 100
1 <= Arr[i] <= 100

Example:
Input:
1
4
1 2 3 4

Output:
10
"""


def sum_of_array(arr):
    return sum(arr)


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        sum_val = (lambda x: sum_of_array([int(i) for i in x.split()]))(input())
        print(sum_val)
