#!/usr/bin/env python3

# this is an implentation of a min binary heap

#read
#----
#https://www.geeksforgeeks.org/what-is-binary-heap/
#https://www.geeksforgeeks.org/binary-heap/

import heapq


'''
min_heap = []
heapq.heappush(min_heap, 10)
print(min_heap)
heapq.heappush(min_heap, 5)
print(min_heap)
heapq.heappush(min_heap, 0.1)
print(min_heap)

mheap = []
heapq.heappush(mheap, 10)
heapq.heappush(mheap, 5)
heapq.heappush(mheap, 15)

# 查看最小元素
print(mheap)
print("最小元素:", mheap[0])  # 输出 5



# convert list to heap
l = [5,4,3,2,1]
heapq.heapify(l)
print(l)
'''





'''
s = [4, 5, 6]
t = s  # t is another reference to the same list as s
print("Original s:", s)
print("Original t:", t)

tt = [1,2,3]

for i in range(len(s)):
  s[i] = tt[i]
  print("s[", i, "] = ", s[i])

print("Modified s:", s)
print("t now?:", t)  #
'''



'''
s[:] = [1, 2, 3]  # Modifies the list in-place
print("Modified s:", s)
print("t sees the change:", t)  # t also sees the change


print("---------------")




#my_list = [1, 2, 3, 2, 4, 2, 5] # wont work in this
my_list = [1, '2', 3, '2', 4, '2', 5]
while '2' in my_list:
    my_list.remove('2')
print(my_list)  # Output: [1, 3, 4, 5]



print('-------------------')


my_list = [1, '2', 3, '2', 4, '2', 5]

while 2 in my_list:
    my_list.remove(2)

print(my_list)  # Output: [1, 3, 4, 5]



'''

