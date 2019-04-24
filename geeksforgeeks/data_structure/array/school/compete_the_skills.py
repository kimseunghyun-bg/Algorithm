"""
A and B are good friend and programmers. They are always in a healthy competition with each other. They decide to judge the best among them by competing. They do so by comparing their three skills as per their values. Please help them doing so as they are busy.

Set for A are like [a1, a2, a3]
Set for B are like [b1, b2, b3]

Compare ith skill of A with ith skill of B
if a[i] > b[i] , A's score increases by 1
if a[i] < b[i] , B's score increases by 1

Input :
The first line of input contains an integer T denoting the test cases. For each test case there will be two lines. The first line contains the skills of A and the second line contains the skills of B

Output :
For each test case in a new line print the score of A and B separated by space.

Constraints :
1 ≤ T ≤ 50
1 ≤ a[i] ≤ 1017
1 ≤ b[i] ≤ 1017

Example:
Input :
2
4 2 7
5 6 3
4 2 7
5 2 8

Output :
1 2
0 2
"""


def compete_the_skills(arr_A, arr_B):
    result = [0, 0]
    for i in range(len(arr_A)):
        if arr_A[i] > arr_B[i]:
            result[0] += 1
        elif arr_A[i] < arr_B[i]:
            result[1] += 1
    return result


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        arr_A = input()
        arr_B = input()
        score = (lambda x, y: compete_the_skills([int(i) for i in x.split()], [int(j) for j in y.split()]))(arr_A,
                                                                                                            arr_B)
        print(str(score)[1:-1].replace(",", ""))
