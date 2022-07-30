def anikethatesjyotuu():  # function without parameters
    print("aniket hates jyotuu ")


anikethatesjyotuu()


def functionwithparameter(a, b):
    print(a, b, 30, 40, sep="__")  # sep is used for seperating all arguments while printing


# this called function does not return anything still we can catch some value thats gonna be always be None [ It is not an error ]
val = functionwithparameter(10, 20)
print("Returned value ", val)


def factorial(n):
    ans = 1
    for j in range(1, n + 1):
        ans *= j
    return ans


ans = factorial(4)
print("Factorial is", ans, end=" []\n")


# calling functions with  arguments by name

def printValues(a, b, c, d):
    print(a, b, c, d)


printValues(10, d=20, b=30, c=40)


def printValues2(a, b, c=100, d=200):
    print(a, b, c, d)


printValues2(10, 20)

printValues2(10, 20, d=1000)

printValues2(20, 30, c=9000)


def functionisalsoanobject():
    return "Aniket hates jyotuuu "


op = functionisalsoanobject  # function is not called but its object is assigned to an variable op
print(op)
print(functionisalsoanobject)
print(op())  # function is called and returned value is printed




