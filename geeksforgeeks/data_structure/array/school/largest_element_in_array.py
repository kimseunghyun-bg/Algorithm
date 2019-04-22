"""
Given an array a[] of size N. The task is to find the largest element in it.

Input:
The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case contains an integer N , the number of elements in the array. Then next line contains N integers of the array separated by space.

Output:
Print the maximum element in the array.

Constraints:
1 <= T <= 100
1 <= N <= 100
1 <= a[i] <= 103

Example:
Input:
2
5
10 324 45 90 9808
7
1 2 0 3 2 4 5

Output:
9808
5

Explanation:
Testcase 1: The largest element of given array is: 9808.
"""


def largest_element_in_array(arr):
    arr.sort()
    return arr[-1]


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        max_value = (lambda x: largest_element_in_array([int(i) for i in x.split()]))(input())
        print(max_value)
