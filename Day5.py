# from typing import List

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False
# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# solution = Solution()
# if solution.containsDuplicate(nums):
#     print("Output: True")
#     print("Explanation: The array contains duplicate values.")
# else:
#     print("Output: False")
#     print("Explanation: All elements in the array are distinct.")

# from typing import List

# class Solution:
#     def combine(self, n: int, k: int) -> List[List[int]]:
#         result = []

#         def backtrack(start: int, path: List[int]):
#             if len(path) == k:
#                 result.append(path[:])  
#                 return
#             for i in range(start, n + 1):
#                 path.append(i)          
#                 backtrack(i + 1, path)  
#                 path.pop()               

#         backtrack(1, [])
#         return result
# n = int(input("Enter the value of n: "))
# k = int(input("Enter the value of k: "))
# solution = Solution()
# combinations = solution.combine(n, k)
# print("\nAll possible combinations:")
# print(combinations)
# print(f"\nTotal combinations: {len(combinations)}")

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         if x < 2:
#             return x

#         left, right = 1, x // 2
#         while left <= right:
#             mid = (left + right) // 2
#             if mid * mid == x:
#                 return mid
#             elif mid * mid < x:
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return right  
# x = int(input("Enter a non-negative integer: "))

# solution = Solution()
# print("Output:", solution.mySqrt(x))

# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n <= 0:
#             return False
        
#         while n % 4 == 0:
#             n //= 4
        
#         return n == 1


# n = int(input("Enter an integer: "))

# solution = Solution()
# if solution.isPowerOfFour(n):
#     print("Output: True")
#     print(f"Explanation: {n} is a power of 4.")
# else:
#     print("Output: False")
#     print(f"Explanation: {n} is not a power of 4.")

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
        
#         while n % 3 == 0:
#             n //= 3
        
#         return n == 1
# n = int(input("Enter an integer: "))

# solution = Solution()
# if solution.isPowerOfThree(n):
#     print("Output: True")
#     print(f"Explanation: {n} is a power of 3.")
# else:
#     print("Output: False")
#     print(f"Explanation: {n} is not a power of 3.")

# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n <= 0:
#             return False

#         while n % 2 == 0:
#             n //= 2
        
#         return n == 1
# n = int(input("Enter an integer: "))

# solution = Solution()
# if solution.isPowerOfTwo(n):
#     print("Output: True")
#     print(f"Explanation: {n} is a power of 2.")
# else:
#     print("Output: False")
#     print(f"Explanation: {n} is not a power of 2.")

# from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')  
#         max_profit = 0           
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             profit = price - min_price
#             if profit > max_profit:
#                 max_profit = profit

#         return max_profit
# prices = list(map(int, input("Enter stock prices separated by space: ").split()))

# solution = Solution()
# print("Output:", solution.maxProfit(prices))


# oops

# def func(a,b):
#     return a+b
# result=func(5,8)
# print(result)

# inhertiance

# class Student:
#     def details(self,name,marks):
#         if marks>=40:
#             result="pass"
#             print(result)
#             print(name,marks)
#         else:
#             print("fail")
# s1=Student()
# s2=Student()

# s1.details("rvs",35)

# syntax
# class ClassName:
#     def method_name(self):
#         print("message")

# with constructor
# class Student:
#     def __init__(self,name,marks):      #constructor
#         self.name=name
#         self.marks=marks
#     def show_result(self):
#         if self.marks>=40:
#             result="pass"
#         else:
#             result="fail"
#         print(" Student name:" self.name)
#         print("Marks",self.marks)
#         print("result",result)

# name=input("enter name ")
# marks=int(input("enter marks"))
# s1=Student(name,marks)
# s1.show_result()

class TemperatureConverter:
    def __init__(self, celsius_list):
        # Constructor: initializes the Celsius temperature list
        self.celsius_list = celsius_list
        self.fahrenheit_list = []  # will store converted values

    def convert_to_fahrenheit(self):
        # Convert each Celsius temperature to Fahrenheit
        for c in self.celsius_list:
            f = (c * 9/5) + 32
            self.fahrenheit_list.append(f)

    def display(self):
        # Display both arrays
        print("Celsius temperatures:    ", self.celsius_list)
        print("Fahrenheit temperatures: ", self.fahrenheit_list)
celsius_values = list(map(float, input("Enter Celsius temperatures separated by space: ").split()))
converter = TemperatureConverter(celsius_values)
converter.convert_to_fahrenheit()
converter.display()