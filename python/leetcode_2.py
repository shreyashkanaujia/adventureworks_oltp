from typing import List
# https://leetcode.com/problems/search-insert-position/
def searchInsert(nums: list[int], target: int) -> int:
        pos = -1
        for i in range(len(nums)):
            if target > nums[i]: pos = i
            if target == nums[i]: return i
        return pos+1
# searchInsert([1,3,5,6], 2)

##################################################

# https://leetcode.com/problems/length-of-last-word/description/
def lengthOfLastWord(s: str) -> int:
    pos = -1
    for i in range(len(s)-1, 0, -1):
        if s[i] != " ":
             break
        pos = i
    if pos == -1:
         pos = len(s)
    pos2 = 0
    for i in range(pos-1, -1, -1):
         if s[i] == " ":
              break
         pos2 = pos2+1
    return pos2
# lengthOfLastWord("Hello World")
# lengthOfLastWord("   fly me   to   the moon  ")
# lengthOfLastWord("a")

##################################################

# https://leetcode.com/problems/plus-one/
def plusOne(digits: List[int]) -> List[int]:
    digits.reverse()
    digits[0] = digits[0] + 1
    carry = 0
    for i in range(len(digits)):
        digits[i] = digits[i] + carry
        carry = 0
        if digits[i] == 10:
            digits[i] = 0
            carry = 1
        # 
    if carry == 1:
         digits.append(1)
    digits.reverse()
    print(digits)
    return digits
# plusOne([4,3,2,1])
plusOne([4,3,2,9])
