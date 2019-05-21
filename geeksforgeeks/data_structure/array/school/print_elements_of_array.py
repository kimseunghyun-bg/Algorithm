"""
Given an array, print all its elements.

Input:

The first line of the input contains T denoting the total number of testcases. The first line of each testcase contains N denoting the size of array. The second line contains N space separated positive integers denoting the elements of array.


Output:

For each testcase, print all its element in new line.


Constraints:

1<=T<=20
1<=N<=100
1<=a[i]<=100

Example:
Input:
1
5
1 2 3 4 5

Output:
1 2 3 4 5

** For More Input/Output Examples Use 'Expected Output' option **
"""


def print_elements_of_array(arr):
    return arr


if __name__ == '__main__':
    test_cases = int(input())
    for i in range(test_cases):
        array_length = input()
        result_val = (lambda x: print_elements_of_array([int(i) for i in x.split()]))(input())
        print(str(result_val)[1:-1].replace(",", ""))
