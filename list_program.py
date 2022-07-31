# program to add two list's corresponding elements
n = int(input("Enter size for list 1 "))
l1 = []
print("Enter element of first list ")
for i in range(n):
    l1.append(int(input()))
print("The first given list is", l1)

n2 = int(input("Enter size for list 2 "))
l2 = []
print("Enter element of second list ")
for i in range(n2):
    l2.append(int(input()))
print("The second given list is", l2)

if len(l1) != len(l2):
    print("Not compatible")

else:
    result = []
    for i in range(n):
        result.append(l1[i] + l2[i])
    print("Result is ", result)
