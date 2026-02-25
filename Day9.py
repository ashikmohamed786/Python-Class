# priority queue
# removes elements based on priority instead of order


# highest priority removed first
# not normal fifo
# smaller number=highest priority

# task-1
# task-3
# task-2

# real time example:

# hospital emergency room
# cpu task scheduling
# printer task priority
# network packet routing


# normal queue vs priority queue

# heap
# smallest number = highest priority
# automatic sorting
# uses heapq module


# pseudo code
# insert
# import heapq
# create empty priority queue - create empty list
# insert elements with priority
# heap arranges automatically

# remove
# remove smallest priority element

# import heapq

# pq=[]

# heapq.heappush(pq,3)

# heapq.heappush(pq,1)

# heapq.heappush(pq,2)

# print("priority queue",pq)

# print("removed",heapq.heappop(pq))

# print("removed",heapq.heappop(pq))

# print("removed",heapq.heappop(pq))







# import heapq

# pq=[]

# heapq.heappush(2,"medium task")

# heapq.heappush(1,"high task")

# heapq.heappush(3,"low task")
# while pq:
#     priority,task=heapq.heappop(pq)
#     print(priority,task)




# nums = [3, 0, 1]
# n = len(nums)
# total = n * (n + 1) // 2   
# result=total - sum(nums)  
# print("Missing number is:", result)



# num = [1, 2, 2, 3, 4, 4, 5]
  
    
# result = []
# for n in num:
#     if n not in result:
#         result.append(n)
    

# print("remove_duplicate",result)  
# Program to reverse the order of characters in each word
# while preserving spaces and word order

# Reverse the characters in each word while keeping word order

s = input("Enter the sentence: ")

words = s.split(" ")

reversed_words = [word[::-1] for word in words]

result = " ".join(reversed_words)

print("Original String: ", s)
print("Reversed Words:  ", result)