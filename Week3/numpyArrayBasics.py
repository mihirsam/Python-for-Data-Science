import numpy as np

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(arr1.shape)
# (5,)

arr2 = np.array([[1,2,3], [2,3,4], [4,5,6], [5,6,7]])
print(arr2)
print(arr2.shape)
# (4,3)

#accessing 2nd and 3rd row/column
print(arr2[1:3,])
print(arr2[:,1:])

arr3 = np.eye(5,5)
print(arr3)

arr4 = np.ones([5,5])
print(arr4)

arr5 = np.zeros([2,3])
print(arr5)

arr6 = np.random.random([3,3])
print(arr6)
