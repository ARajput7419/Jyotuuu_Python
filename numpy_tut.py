import numpy as np

jyotu = np.array([10,20,30])
print(jyotu)

jyotuu = np.array([10,20,30],dtype="str")
print(jyotuu)

jyotuu = np.array([10,'aniket',90.2])
print(jyotuu)

jyotuu = np.array([10,20.3])
print(jyotuu)


#################################################

d = np.array([[10,20,30],[30,40,50]])
print(d," : ",d.dtype)
print("dim : ",d.ndim)
print("shape : ",d.shape)


##########################################################

data1 = np.arange(10) # [ 0 , 1 , ....,9]
print(data1)

data1 = np.arange(1,10) # [ 1 ,2 ,3 .... , 9]
print(data1)

data1 = np.arange(1,10,2) # [ 1 , 3 , 5 , 7 , 9 ]
print(data1)

data1 = np.arange(10,20,-1) # []
print(data1)


###################################################
# reshape

matrix = np.arange(1,10).reshape((3,3)) # default order 'C'
print("Row major order \n",matrix)



