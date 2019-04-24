"""
Given a stream of numbers, print average or mean of the stream at every point.

Input: The first line of input contains an integer T denoting the number of test cases.
For each test case there will be two lines. The first line contains an integer N denoting the size of array C[], and second line contains N space seperated integers C[i].

Output:
Print the average of the stream at every point (in integer).

Constraints:
1 ≤ T ≤ 20
1 ≤ N ≤ 50
1 ≤ C[i] ≤ 100

Example:
Input
2
5
10 20 30 40 50
2
12 2

Output
10 15 20 25 30
12 7
"""


def average(arr):
    result_arr = []
    sum = 0
    for i in arr:
        sum += i
        result_arr.append(int(sum / (len(result_arr) + 1)))
    return result_arr


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        result_val = (lambda x: average([int(i) for i in x.split()]))(input())
        print(str(result_val)[1:-1].replace(",", ""))
