"""
Given a string str. The task is to find the maximum occurring character in the string str. If more than one character occurs maximum number of time then print the lexicographically smaller character.

Input:
The first line of input contains an integer T denoting the number of test cases. Each test case consist of a string in 'lowercase' only in a separate line.

Output:
For each testcase, in a new line, print the lexicographically smaller character which occurred the maximum time.

Constraints:
1 ≤ T ≤ 30
1 ≤ |s| ≤ 100

Example:
Input:
2
testsample
output

Output:
e
t

Explanation:
Testcase 1: e is the character which is having highest frequency.
Testcase 2: t and u are the characters with the same frequency, but t is lexicographically smaller.
"""


def maximum_occuring_character(character):
    most_char = character[0]
    most_char_cnt = 0
    while character is not "":
        c = character[0]
        if most_char_cnt < character.count(c):
            most_char = c
            most_char_cnt = character.count(c)
        elif most_char_cnt == character.count(c) and c < most_char:
            most_char = c
        character = character.replace(c, "")
    return most_char


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(0, test_cases):
        print(maximum_occuring_character(input()))
