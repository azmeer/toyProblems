"""
Given an array containing both negative and positive integers. Find the contiguous sub-array with maximum sum.
 
Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.
 
Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.
 
Constraints:
1 ≤ T ≤ 200
1 ≤ N ≤ 1000
-100 ≤ A[i] <= 100
 
Example:
Input
2
3
1 2 3
4
-1 -2 -3 -4
Output
6
-1

See: https://en.wikipedia.org/wiki/Maximum_subarray_problem
Key note:
  either the max subarray sum ending at position i + 1 includes the max subarray sum ending at position i or it doesn't

"""
def max_sub_array(array):
    max_so_far = max_ending_here = array[0]
    for num in array[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far if (max_so_far > 0) else 0

array = [2, 7, 25, -11, 30, -125, 12]    
print(max_sub_array(array))
