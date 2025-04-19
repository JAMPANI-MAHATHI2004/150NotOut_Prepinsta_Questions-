# Program for checking duplicate in an array – Duplicate Integer Problem
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1
# Input: nums = [1, 2, 3, 3]
# Output: true
# Example 2
# Input: nums = [1, 2, 3, 4]
# Output: false
#--------------------------------------------------------------------------

# method 1: Brute Fore without functions
nums = list(map(int, input("enter: ").split(',')))
found = False
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums[j]:
            print("True")
            found = True
            break
    if found:
        break
if not found:
    print("False")
#------------------------------------------------------------------
#method 2: Bruteforce with functions
class Solution():
    def ContainsDuplicates(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
sol = Solution()
nums = list(map(int, input("enter:").split(',')))
print(sol.ContainsDuplicates(nums))
#-------------------------------------------------------------------
#method 3: Sorting
def duplicates(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False
nums = list(map(int, input("enter:").split(',')))
print(duplicates(nums))
#--------------------------------------------------------------------
#method 4: Hashset
def duplicates(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
nums = list(map(int, input("enter:").split(',')))
print(duplicates(nums))
#--------------------------------------------------------------------
#method 5: Hashset length
def duplicate(nums):
    if (len(nums) > len(set(nums))):
        return True
    return False
nums = list(map(int, input("enter:").split(',')))
print(duplicate(nums))