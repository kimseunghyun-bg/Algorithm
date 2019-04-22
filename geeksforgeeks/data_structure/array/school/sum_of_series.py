"""
Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)

Input:
The first line of input contains an integer, the number of test cases T. Each test case should contain a positive integer N.

Output:
Print the sum in a separate line.

Constraints:
1 <= T <= 30
1 <= N <= 100

Example:
Input:
2
1
5

Output:
1
15

Explanation:
Testcase 2: For n=5 , sum will be 1+2+3+4+5=15.
"""


def sum_of_series(end_number):
    return sum(range(end_number + 1))


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        print((lambda x: sum_of_series(int(x)))(input()))
