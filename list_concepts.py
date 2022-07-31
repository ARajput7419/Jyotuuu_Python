l = []  # empty list

print(l)

l = [10, 20, 30]

print(l[0])  # print element at index 0
print(l)  # print complete list

# iterate over list using for in loop

for element in l:
    if element == 100:
        break
    print(element)

# iterate over list using indices

for index in range(0, len(l)):
    if index == 20:
        break
    print(l[index])

# iterate using while loop

index = 0
while index < len(l):
    print(index, l[index], sep=":", end=",")
    index += 1

print()

# difference between is and ==
# is checks whether variables are referring to the same  object or not
# == checks whether two objects are equal or not

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
print(l1 == l2)

l2 = [1, 2, 3, 4]

print(l1 == l2)  # True
print(l1 is l2)  # False

l1 = l2

print(l1 == l2)  # True
print(l1 is l2)  # True

# append function
# because list objects are always mutable

l = [1, 2]
print("Address of list ", id(l), " elements are ", l)
l.append(30)
print("Address of list ", id(l), " elements are ", l)

# extend function
l1 = [1, 2, 3]
l2 = [5, 6, 7, 8, 9]
l1.extend(l2)
print("List l1 ")
print(l1)
print("List l2 ")
print(l2)

# extend using different iterable objects
l1 = [100, 200, 300]
print("List l1 is ", l1)
l1.extend(range(0, 10))
print(l1)

# sort a list
l1 = [10, 4, 2, 10.3, 899, 85]
l1.sort()
print(l1)

# insert an element at an index . it does not replace

l1 = [1, 2, 3, 4]
print("Before Insertion ", l1)
l1.insert(1, 100)
print("After insertion ", l1)

# replace an element
l1[2] = 101
print(l1)

# reverse an list
l1 = [1, 2, 3, 4, 1000, 2, 4, -1]
l1.reverse()
print(l1)

# slicing l1 [ start : end ] default step = 1 or [ start:end :step]
l1 = [1, 2, 3, 4, 5]
print(l1[:-3:-1])
print(l1[1:4:2])

# index
l1 = [1, 2, 300, 4, 5, 300, 6]
print(l1.index(300))  # return first index where 300 is present

# print(l1.index(10000)) # raise Exception when not present

# count function
l1 = [1, 2, 3, 1, 1, 1, 2, 3, 4, 5]
print(l1.count(1))

# pop function

l1 = [1, 2, 3, 400, 5, 6]
print(l1.pop(3))  # returns popped element
print(l1)  # list after popping

# remove function
l1 = [1, 2, 3, 100, 20000, 100, 1]
l1.remove(100)  # removes first occurrence of the given element
print(l1)
