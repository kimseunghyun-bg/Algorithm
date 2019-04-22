"""
Given an sorted array A of size N. Find number of elements which are less than or equal to given element X.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each testcase contains 3 lines of input. The first line contains an integer N denoting the size of the array. Then the next line contains N space separated integers forming the array. The third line contains an element X.

Output:
For each testcase, in a new line, print the number of elements which are less than or equal to given element.

Constraints:
1 <= T <= 105
1 <= N <= 105
1 <= Ai <= 105
0 <= X <= 105

Example:
Input:
2
6
1 2 4 5 8 10
9
7
1 2 2 2 5 7 9
2
Output:
5
4

def count_of_smaller(arr, num):
    while arr.count(num) == 0:
        num -= 1
    return arr.index(num)+arr.count(num)

"""


def count_of_smaller(arr, num):
    temp = 0
    for i in arr:
        if i <= num:
            temp += 1
        else:
            break
    return temp


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        arr = input()
        num = input()
        result = (lambda x, y: count_of_smaller([int(i) for i in x.split()], int(y)))(arr, num)
        print(result)
