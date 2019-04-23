"""
Given a list of names, display the longest name.

Input:
First line of input contains an integer T, the number of test cases. For each test case, there will be two lines. First line contains integer N i.e. total number of names, and second line contains N space seperated names of different length.

Output:
Longest name in the list of names.

Constraints:
1 <= T <= 10
1 <= N <= 10
1 <= |length of name| <= 1000

Example:
Input:
1
5
Geek
Geeks
Geeksfor
GeeksforGeek
GeeksforGeeks

Output:
GeeksforGeeks
"""


def display_longest_name(arr):
    longest_name = arr[0]
    for element in arr:
        if len(longest_name) < len(element):
            longest_name = element
    return longest_name


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        # array_length = input()
        arr = []
        # arr.append("ab")
        # print(arr)
        for i in range(int(input())):
            arr.append(str(input()))
        name = (lambda x: display_longest_name(x))(arr)
        print(name)
