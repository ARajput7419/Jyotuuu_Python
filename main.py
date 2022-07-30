# aniket = 67+348j
# aniket2 = 959j
# print(type(aniket))
# aniket3 = True
# aniket4 = False
# print(type(aniket3))
#
#
# a = 10
# b = 20
#
# a,b = b,a
#
# print(a,b)
#
# # only single line comment
#
#
# a = None
#
# if a:
#     print("Condition true")
#
# else:
#     print("Condition false")
#
# number = int(input("Enter number"))
# if number == 10:
#     print("Number is 10 ")
# elif number == 11:
#     print("Number is 11 ")
# elif number == 12:
#     print("Number is 12 ")
# else:
#     print("Condition is not true ")
#
#
# i = 10
# print(i)
#







aniket_list = [1,2,3,4,5,6,7,8,9,10,11,12]
op = iter(aniket_list)

while True :
    try:
        print(op.__next__())
    except Exception:
        break





io = 8758945
print(io/100) # float division
print(io//100) # integer division
print(2**10) # power operator


i = 0
while i<10:
    print(i,"aniket","weds","jyotuu",sep="____",end="\n")
    i+=1




