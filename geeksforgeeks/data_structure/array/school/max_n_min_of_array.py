"""
Given an array A[ ], find maximum and minimum elements from the array.

Input:
The first line of input contains an integer T, denoting the number of testcases. The description of T testcases follows. The first line of each testcase contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
For each testcase in a new line, print the maximum and minimum element in a single line with space in between.

Constraints:
1 ≤ T ≤ 30
1 ≤ N ≤ 100
0 ≤A[i]<100

Example:
Input:
2
4
5 4 2 1
1
8

Output:
5 1
8 8

Explanation:
Testcase 1:
Maximum element is: 5
Minimum element is: 1
"""


def max_n_min_of_array(arr):
    arr.sort(reverse=True)
    return [arr[0], arr[-1]]


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        arr = (lambda x: max_n_min_of_array([int(i) for i in x.split()]))(input())
        print(str(arr)[1:-1].replace(",", ""))
