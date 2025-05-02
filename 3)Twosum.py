#--Pair with Given Sum – 2Sum Problem
"""Given an array of integers nums and an integer target, return the 
        indices i and j such that nums[i] + nums[j] == target and i != j."""
# You may assume that every input has exactly one pair of indices 
        # i and j that satisfy the condition.
# *** Return the answer with the smaller index first.

"""
#-*-Example 1
Input: nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].
#-*-Example 2
Input: nums = [4,5,6], target = 10
Output: [0,2]
#-*-Example 3
Input: nums = [5,5], target = 10
Output: [0,1]"""

# Method-1: Brute Force
def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[i] + nums[j] == target:
                return i,j
nums = list(map(int, input("nums: ").split(',')))
target = int(input("target: "))
print(twosum(nums,target))

# Method-2: Sorting
def twosums(nums, target):
    enum = list(enumerate(nums)) # As we want a list of pairs of nums [( , ),( , ),( , )...]
    enum.sort(key=lambda x: x[1])
    # execute 2 pointers
    l = 0
    r = len(enum) - 1
    while l < r:
        sum_ = enum[l][1] + enum[r][1]
        if sum_ == target:
            i,j = enum[l][0], enum[r][0]
            return (min(i,j), max(i,j))
        elif sum_ < target:
            l += 1
        else:
            r -= 1
nums = list(map(int, input("nums: ").split(',')))
target = int(input("target: "))
print(twosum(nums, target))

# Method-3: HashMap(Two pass)
def twopass(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        hashmap[num] = i # stores in key-value pair
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hashmap and hashmap[complement] != i:
            j = hashmap[complement]
            return [min(i,j),max(i,j)]
        
print(twopass([3,4,5,6],7))

# Method-4: HashMap(One Pass)
def onepass(nums,target):
    hashmap = {}
    for i, num in enumerate(nums):
        complement = target - num
    
        if complement in hashmap:
            j = hashmap[complement]
            return [min(i,j),max(i,j)]
        hashmap[num] = i
print(onepass([3,4,5,6],7))