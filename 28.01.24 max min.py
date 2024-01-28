You will be given a list of integers, , and a single integer . You must create an array of length  from elements of  such that its unfairness is minimized. Call that array . Unfairness of an array is calculated as

Where:
- max denotes the largest integer in 
- min denotes the smallest integer in 

Example



Pick any two elements, say .

Testing for all pairs, the solution  provides the minimum unfairness.

Note: Integers in  may not be unique.

Function Description

Complete the maxMin function in the editor below.
maxMin has the following parameter(s):

int k: the number of elements to select
int arr[n]:: an array of integers
Returns

int: the minimum possible unfairness
Input Format

The first line contains an integer , the number of elements in array .
The second line contains an integer .
Each of the next  lines contains an integer  where .

Constraints




Sample Input 0

7
3
10
100
300
200
1000
20
30
Sample Output 0

20
Explanation 0

Here ; selecting the  integers , unfairness equals

max(10,20,30) - min(10,20,30) = 30 - 10 = 20
Sample Input 1

10
4
1
2
3
4
10
20
30
40
100
200
Sample Output 1

3
Explanation 1

Here ; selecting the  integers , unfairness equals

max(1,2,3,4) - min(1,2,3,4) = 4 - 1 = 3
Sample Input 2

5
2
1
2
1
2
1
Sample Output 2

0
Explanation 2

Here .  or  give the minimum unfairness of .

Submissions: 59
Max Score: 35
Difficulty: Medium
Rate This Challenge:

    
More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
#
10
# Complete the 'maxMin' function below.
11
#
12
# The function is expected to return an INTEGER.
13
# The function accepts following parameters:
14
#  1. INTEGER k
15
#  2. INTEGER_ARRAY arr
16
#
17
​
18
def maxMin(k, arr):
19
    arr.sort()  # Sort the array in ascending order
20
    min_unfairness = float('inf')
21
​
22
    for i in range(len(arr) - k + 1):
23
        unfairness = arr[i + k - 1] - arr[i]
24
        min_unfairness = min(min_unfairness, unfairness)
25
​
26
    return min_unfairness
27
​
28
if __name__ == '__main__':
29
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
30
​
31
    n = int(input().strip())
32
​
33
    k = int(input().strip())
34
​
35
    arr = []
36
​
37
    for _ in range(n):
38
        arr_item = int(input().strip())
39
        arr.append(arr_item)
40
​
41
    result = maxMin(k, arr)
42
​
43
    fptr.write(str(result) + '\n')
44
​
45
    fptr.close()
