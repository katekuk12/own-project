import random

#print(kate)
"""
def nEvens(list):
    nEvens = 0
    for number in list:
        if number % 2 == 0:
            nEvens = nEvens + 1
            print(number)
    return nEvens


kate = [1, 2, 4, 6, 7, 11, 91,92,89]
print(nEvens(kate))
"""



"""
list = [3, 4, 6, 98, 5, 6]
max_num = list[0]

for i in list:
    if i > max_num:
        max_num = i
print(max_num)
"""






def problem(num,target):
    for i in range(0,len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]


nums = [2,15,11,7]
target = 9
print(problem(nums,target))


n = 12
for i in range (1, n+1):
    for j in range (n+1, 0, -1):
        if i * j == n:
            print (i, j)

