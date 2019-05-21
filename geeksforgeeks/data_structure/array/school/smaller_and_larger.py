"""
Given a sorted array and a value x, find the number of array elements less than or equal to x and elements more than or equal to x.

Input:
The first line of input contains an integer T denoting the number of test cases. For each test case there will be two lines. The first line contains the two space seperated integers N and x, where N is the size of array. Second line contains the space seperated integers of the array C[i].

Output:
Print the number of Array elements less than or equal to x and array elements greater than or equal to x.

Constraints:
1 ≤ T ≤ 50
1 ≤ N ≤ 100
0 ≤ X ≤ 1000
1 ≤ C[i] ≤ 200

Example:
Input:
3
7 0
1 2 8 10 11 12 19
7 5
1 2 8 10 11 12 19
7 10
1 2 8 10 11 12 19

Output:
0 7
2 5
4 4
"""


def smaller_and_larger(arr, num):
    same_num = 0
    smaller_num = 0
    for i in range(0, len(arr), 1):
        if arr[i] == num:
            same_num += 1
        elif arr[i] > num:
            break

        smaller_num += 1
    return [smaller_num, len(arr) - smaller_num + same_num]


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        input_temp = [int(i) for i in input().split()]
        input_num = input_temp[1]
        result_val = (lambda x: smaller_and_larger([int(i) for i in x.split()], input_num))(input())
        print(str(result_val)[1:-1].replace(",", ""))
