"""
Given an array of size N, swap the kth element from beginning with kth element from end.

Input:
The first line of input contains an integer T denoting the number of test cases. T testcases follow. Each testcase contains 2 lines of input:
The first line contains an integer N, where N is the size of array.
The second line contains N integers(elements of the array) sperated with spaces.

Output:
For each test case, print the modified array.

Constraints:
1 ≤ T ≤ 200
1 ≤ K ≤ N ≤ 500
1 ≤ A[i] ≤ 1000

Example:
Input
1
8 3
1 2 3 4 5 6 7 8
Output
1 2 6 4 5 3 7 8
"""


def swap_kth_elements(arr, index):
    temp = arr[index - 1]
    arr[index - 1] = arr[index * -1]
    arr[index * -1] = temp
    return arr


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        len_idx = [int(i) for i in input().split()]
        arr = input()
        result = (lambda x, y: swap_kth_elements([int(i) for i in x.split()], int(y)))(arr, len_idx[1])
        print(str(result)[1:-1].replace(",", ""))
