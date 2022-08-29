import numpy as np

jyotu = np.array([10, 20, 30])
print(jyotu)

jyotuu = np.array([10, 20, 30], dtype="str")
print(jyotuu)

jyotuu = np.array([10, 'aniket', 90.2])
print(jyotuu)

jyotuu = np.array([10, 20.3])
print(jyotuu)

#################################################

d = np.array([[10, 20, 30], [30, 40, 50]])
print(d, " : ", d.dtype)
print("dim : ", d.ndim)
print("shape : ", d.shape)

##########################################################

data1 = np.arange(10)  # [ 0 , 1 , ....,9]
print(data1)

data1 = np.arange(1, 10)  # [ 1 ,2 ,3 .... , 9]
print(data1)

data1 = np.arange(1, 10, 2)  # [ 1 , 3 , 5 , 7 , 9 ]
print(data1)

data1 = np.arange(10, 20, -1)  # []
print(data1)

###################################################
# reshape

matrix = np.arange(1, 10).reshape((3, 3))  # default order 'C'
print("Row major order \n", matrix)

array = np.arange(1, 10)
matrix = array.reshape((3, 3), order='F')  # default order 'C'
print("Column major order \n", matrix)

#####################################################################

data = np.linspace(20, 30, 10)
print(data)

###################################################################

array = np.arange(1, 5).reshape((2, 2))
print("Max ", np.max([1, 2, 34, 4, 5, 6, 7, 10]))  # first option to get maximum
print("Max ", array.max())  # second option to get maximum

print("Min ", array.min())
print("Min ", np.min(array))

print("Sum ", array.sum())
print("Sum ", np.sum(array))

####################################################################
matrix1 = np.arange(1, 10).reshape((3, 3))
matrix2 = np.arange(11, 20).reshape((3, 3))
print("Matrix 1 ", matrix1)
print("Matrix 2 ", matrix2)
print("************* sum  *********")
print(matrix1 + matrix2)

print("*********** subtract *******")
print(matrix1 - matrix2)

print("*****  simple product *****")
print(matrix1 * matrix2)

print("****** matrix product ***** ")
print(matrix1 @ matrix2)  # option 1
print(np.matmul(matrix1, matrix2))  # option 2

###############################################################

array = np.array([1, 2, 3, 4])
print(" * ", 10 * array)
print("+ ", 10 + array)
print("original ", array)

##############################################################
# ****************    AXIS [ IMP ] ********************


# ---> AXIS 1
# |         1 2 3
# |         4 5 6
# Axis 0    7 8 9


print("Matrix ", matrix1)
print("overall sum ", np.sum(matrix1))
print("sum axis 0 ", np.sum(matrix1, axis=0))
print("sum axis 1 ", np.sum(matrix1, axis=1))

matrix1 = np.array([[34, 2, 4], [10, -1, 89], [90, 0, 100]])
print("Matrix is ")
print(matrix1)
print("sorting axis 0  ", np.sort(matrix1, axis=0))
print("sorting axis 1 ", np.sort(matrix1, axis=1))


######################################################

array1 = np.array([[1,2,3,4]])
array2 = np.array([[5,6,7,8]])
print("array 1 ",array1)
print("array 2 ",array2)
print("concatenate axis 0 ")
print(np.concatenate((array1,array2),axis=0))
print("concatenate axis 1 ")
print(np.concatenate((array1,array2),axis=1))
