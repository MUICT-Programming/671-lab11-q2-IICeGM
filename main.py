# YOUR CODE HERE
def  summation(list1,list2):
    updated_list = []
    for i in range(len(list1)):
        sum_x_y = list1[i] + list2[i]
        updated_list.append(sum_x_y)
    return updated_list

def find_min_max(updated_list):
    max = updated_list[0]
    min = updated_list[0]
    for i in updated_list:
        if i > max:
            max = i
        if i < min:
            min = i
    return min,max

list1 = []
list2 = []

n = int(input())

for i in range(n):
    list1.append(int(input()))

for i in range(n):
    list2.append(int(input()))

sum = summation(list1,list2)
min_max = find_min_max(sum)
print(sum)
print(min_max)
