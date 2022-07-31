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
