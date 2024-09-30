# This code can check if the brackets in a string are correctly placed
def isValid(s: str) -> bool:
    list1 = []
    dict1 = {")": "(", "]": "[", "}": "{"}
    for i in range(len(s)):
        if i == 0 or list1 == []:
            list1.append(s[i])
        elif dict1.get(s[i]) == list1[-1]:
            list1.pop()
        else:
            list1.append(s[i])
    # 
    if list1 == []:
        print("List Empty")
    else: 
        print("problem")
    return 0
# 
# Run the function with the string below to check the brackets placement
isValid("(){(([({})]))}")

##################################################

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List
def removeDuplicates(nums: list[int]) -> int:
        list1 = []
        j = 0
        for itr in range(1, len(nums)):
            if nums[itr-1] != nums[itr]:
                list1.append(nums[itr-1])
                if itr == len(nums)-1:
                    list1.append(nums[itr])
        # 
        for itr in range(len(list1), len(nums)):
            list1.append("_")
        return len(list1)
# 
removeDuplicates([1,1,2])