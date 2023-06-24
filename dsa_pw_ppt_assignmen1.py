# -*- coding: utf-8 -*-
"""DSA_PW_PPT_Assignmen1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tj2Ts4kuftk7mA1GTF4_zeJli56t1zPY

Question no-1
"""

def twoSum(nums, target):
    num_dict = {}  # Map numbers to their indices
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []  # No valid solution found

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]

"""Question No-2"""

def removeElement(nums, val):
    slow = 0  # Pointer to track the position of non-val elements
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

# Example usage
nums = [3, 2, 2, 3]
val = 3
count = removeElement(nums, val)
print(count)  # Output: 2
print(nums)

"""Question No.-3"""

def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return left

# Example usage
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print(index)

"""Question No - 4"""

def plusOne(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
        else:
            carry = 0
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits

# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)

"""Question No - 5"""

def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

    return nums1

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

result = merge(nums1, m, nums2, n)
print(result)

"""Question No-6"""

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)

"""Question No - 7"""

def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1
    return nums

# Example usage
nums = [0, 1, 0, 3, 12]
result = moveZeroes(nums)
print(result)

"""Question No. 8"""

def findErrorNums(nums):
    numSet = set()
    duplicate = -1
    missing = -1

    for num in nums:
        if num in numSet:
            duplicate = num
        else:
            numSet.add(num)

    for i in range(1, len(nums) + 1):
        if i not in numSet:
            missing = i
            break

    return [duplicate, missing]

# Example usage
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)