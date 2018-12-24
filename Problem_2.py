"""
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""
def solution(arr):
    new_arr = []
    for i in range(len(arr)):
        pro=1
        for j in range(len(arr)):
            if j==i:
                continue
            pro*=arr[j]
        new_arr.append(pro)
    return new_arr

#Driver Code
print(solution([1,2,3,4,5]))
print(solution([3,2,1]))
