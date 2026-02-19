# class Solution:
#     def isPowerOfThree(self, n):
#         if n <= 0:
#             return False
        
#         while n % 3 == 0:
#             n //= 3
        
#         return n == 1


# if __name__ == "__main__":
#     sol = Solution()

#     test_values = [27, 9, 45, 0, 1, 81, 10, -3]

#     for n in test_values:
#         print(f"{n} → {sol.isPowerOfThree(n)}")


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         return sorted(s) == sorted(t)


# if __name__ == "__main__":
#     sol = Solution()

#     s = "anagram"
#     t = "nagaram"

#     print(f"Is '{t}' an anagram of '{s}'? → {sol.isAnagram(s, t)}")

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n

#         first, second = 1, 2

#         for i in range(3, n + 1):
#             third = first + second  # ways to reach current step
#             first, second = second, third  # move the window

#         return second


# if __name__ == "__main__":
#     sol = Solution()

#     n = 5  
#     print(f"Number of distinct ways to climb {n} steps: {sol.climbStairs(n)}")


# from typing import List

# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         answer = []

#         for i in range(1, n + 1):
#             if i % 3 == 0 and i % 5 == 0:
#                 answer.append("FizzBuzz")
#             elif i % 3 == 0:
#                 answer.append("Fizz")
#             elif i % 5 == 0:
#                 answer.append("Buzz")
#             else:
#                 answer.append(str(i))
        
#         return answer


# if __name__ == "__main__":
#     sol = Solution()
#     n = 15 
#     print(sol.fizzBuzz(n))

# from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         count = 0
#         candidate = None

#         for num in nums:
#             if count == 0:
#                 candidate = num
#             count += (1 if num == candidate else -1)
        
#         return candidate


# if __name__ == "__main__":
#     sol = Solution()
#     nums = [3, 2, 3]
#     print(f"Majority element in {nums} is: {sol.majorityElement(nums)}")

# from typing import List

# class Solution:
#     def arraySign(self, nums: List[int]) -> int:
#         product_sign = 1  

#         for num in nums:
#             if num == 0:
#                 return 0      
#             elif num < 0:
#                 product_sign *= -1  

#         return product_sign


# if __name__ == "__main__":
#     sol = Solution()
#     nums = [-1, -2, -3, -4, 3, 2, 1]
#     print(f"Sign of product for {nums} is: {sol.arraySign(nums)}")


# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip()
        
#         words = s.split(" ")
        
#         return len(words[-1])


# if __name__ == "__main__":
#     sol = Solution()
#     s = "Hello World"
#     print(f"Length of last word in '{s}': {sol.lengthOfLastWord(s)}")

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        result = list(set1 & set2)

        return result


if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2,4,]
    print(f"intersection  of {nums1} and {nums2}: {sol.intersection(nums1, nums2)}")



# from typing import List

# class Solution:
    # def union(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     set1 = set(nums1)
    #     set2 = set(nums2)

    #     result = list(set1 | set2)

    #     return result


# if __name__ == "__main__":
    # sol = Solution()
    # nums1 = [1, 2, 3, 4]
    # nums2 = [5, 6,7, 8]
    # print(f"union  of {nums1} and {nums2}: {sol.union(nums1, nums2)}")

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# from typing import Optional

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         tail = dummy 

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next  

#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2

#         return dummy.next


# def build_linked_list(values):
#     dummy = ListNode()
#     current = dummy
#     for v in values:
#         current.next = ListNode(v)
#         current = current.next
#     return dummy.next

# def print_linked_list(head):
#     result = []
#     while head:
#         result.append(head.val)
#         head = head.next
#     print(result)

# if __name__ == "__main__":
#     list1 = build_linked_list([1, 2, 4])
#     list2 = build_linked_list([1, 3, 4])

#     sol = Solution()
#     merged = sol.mergeTwoLists(list1, list2)
#     print_linked_list(merged)


# from typing import List

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """

#         i = m - 1 
#         j = n - 1  
#         k = m + n - 1  

#         while i >= 0 and j >= 0:
#             if nums1[i] > nums2[j]:
#                 nums1[k] = nums1[i]
#                 i -= 1
#             else:
#                 nums1[k] = nums2[j]
#                 j -= 1
#             k -= 1

#         while j >= 0:
#             nums1[k] = nums2[j]
#             j -= 1
#             k -= 1


# if __name__ == "__main__":
#     sol = Solution()
#     nums1 = [1, 2, 3, 0, 0, 0]
#     nums2 = [2, 5, 6]
#     m, n = 3, 3

#     sol.merge(nums1, m, nums2, n)
#     print(f"Merged array: {nums1}")


# from typing import List

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if not strs:
#             return ""
#         prefix = strs[0]
#         for s in strs[1:]:
#             while not s.startswith(prefix):
#                 prefix = prefix[:-1]  
#                 if not prefix:
#                     return ""  
#         return prefix
# if __name__ == "__main__":
#     sol = Solution()
#     strs = ["flower", "flow", "flight"]
#     print(f"Longest common prefix of {strs}: '{sol.longestCommonPrefix(strs)}'")


# from typing import List

# class Solution:
#     def reverseString(self, s: List[str]) -> None:
#         """
#         Do not return anything, modify s in-place instead.
#         """
#         left, right = 0, len(s) - 1
#         while left < right:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
# if __name__ == "__main__":
#     sol = Solution()
#     s = ["h", "e", "l", "l", "o"]
#     sol.reverseString(s)
#     print(f"Reversed string: {s}")


# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         else:
#             return 1 + (num - 1) % 9
# if __name__ == "__main__":
#     sol = Solution()
#     num = 38
#     print(f"Final single digit of {num}: {sol.addDigits(num)}")

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        while insert_pos < len(nums):
            nums[insert_pos] = 0
            insert_pos += 1
if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    print(f"Modified array: {nums}")
