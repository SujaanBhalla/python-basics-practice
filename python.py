# # # import numpy 
# # # # n = numpy.arange(11
# # # # )
# # # # print(type(n))
# # # # print(n)
# # # # print(n[0])
# # # #example
# # # # n = numpy.arange(12)
# # # # d = n.reshape(3,4)
# # # # print(d)

# # # #example
# # # #n = numpy.arange(12).reshape(4,3)
# # # # print(n)
# # # # make a 3 d array 
# # # # n = numpy.arange(8).reshape(2,2,2)
# # # # print(n)
# # # # n = numpy.arange(12).reshape(4,3)
# # # # print(n)
# # # #print(n[0:4:2, :])

# # # #import numpy
# # # # n = numpy.arange(12).reshape(4,3)
# # # #print(n)
# # # #print(n[1:3,1])

# # # import numpy as np
# # # #list1d
# # # l = [1,2,3]
# # # print(l)
# # # #array ld
# # # arr = np.array(l)
# # # print(arr)

# # # #2d python list
# # # l = [[1,2,3] , [4,5,6]]
# # # print(l)
# # # print(type(l))

# # # #2d numpy array
# # # l = [ [ 1,2 ,3 ], [4,5,6]]
# # # arr = np.array(l)
# # # print(arr)
# # # print(type(arr))
# # # #0d
# # # # import numpy as np
# # # arr = np.array(10)
# # # print(arr)
# # # print(arr.ndim)
# # # #1d
# # # arr = np.array([10,20,30,40,50])
# # # print(arr)
# # # print(arr.ndim)

# # # arr = np.array([
# # #     [10,20,30],
# # #     [40,50,60]
# # # ])
# # # print(arr[0][0])  # 10
# # # print(arr[1][1])  # 50


# # # arr = np.array([
# # #     [[10,20],[30,40]],
# # #     [[50,60],[70,80]]
# # # ])
# # # print(arr[0][1][1])

# # # #replace in python 2d array
# # # import numpy as np 
# # # arr = np.array([[1,2,3],[4,5,6]])
# # # print("before:")

# # # print(arr)
# # # print("after")
# # # arr[1][0] = 100
# # # print(arr)

# # # # replace in python 2d list

# # # l = [[1,2,3],[4,5,6]]
# # # l[1][0] = 100
# # # print(l)

# # # import numpy as np
# # # l = [1,2,3]
# # # ln = l*2
# # # print(ln)
# # # arr = np.array(l)
# # # arrM = arr*2
# # # print(arrM)

# # # # comparison 
# # # #list
# # # import time
# # # start = time.time()
# # # l = [i*2 for i in range(1000000)]
# # # print("list output :", time.time()- start)

# # # #array
# # # import numpy as np
# # # start = time.time()
# # # arr = np.array(1000000)*2
# # # print("array output",time.time() - start)

# # # #array
# # # # import numpy as np

# # # # start = time.time()
# # # # arr = np.array(1000000)*2
# # # # print(" array output"time.time() - start)

# # # #list
# # # # import time
# # # # start = time.time()
# # # # l = [i*2 for i in range(1000000)]
# # # # print("list output :" time.time()- start)
# # # # error aayega

# # # #import numpy as np
# # # # import time

# # # # NumPy
# # # # start = time.time()

# # # # arr = np.arange(1000000) * 2

# # # # print("array output :", time.time() - start)

# # # # # List
# # # # start = time.time()

# # # # l = [i * 2 for i in range(1000000)]

# # # # print("list output :", time.time() - start)
 
# # # #zeros array 1d 

# # # import numpy as np
# # # arr = np.zeros(5)
# # # print(arr)

# # # #zeros array 2d

# # # arr1 = np.zeros((3,4))
# # # print(arr1)

# # # #ones array 1d 

# # # import numpy as np
# # # arr = np.zeros(5)
# # # print(arr)

# # # #ones array 2d

# # # arr1 = np.zeros((3,4))
# # # print(arr1)




# # # #ques zero ka use karke 2d arry har ek eleement ko incremnet by + 10 and
# # # # in other ques   multiplyby 5 

# # # # full in 1 d array
# # # # full in 2d array

# # # # by thee qyes help of zeros 2d all vlue 6
# # # # import numpy as np
# # # # arr = np.zeros((3,4)) + 6
# # # # print(arr)
# # # # #by the helfo ogf fulll 2d array all value 1
# # # # import numpy as np
# # # # arr = np.full((3,4),1)
# # # # print(arr)

# # # # #random
# # # # # randomfor 1d 0 -> 1
# # # import numpy as np
# # # arr = np.random.random(5)
# # # print(arr)

# # # # random for 2d 0-> 1
# # # arr1 = np.random.random((3,4))
# # # print(arr1)

# # # # arrange for 1d
# # # import numpy as np
# # # arr = np.arange(10)

# # # #arrange for 1d with step (start, stop, step)
# # # arr1 = np.arange(0,10,2)
# # # print(arr1)

# # # # arrange for 2d used reshape
# # # arr1 = np.arange(12)
# # # arr1 = arr1.reshape(4,3)

# # # #vector (1d array) and matrix(2d array) and
# # # # vector 1d list
# # # import numpy as np
# # # l = [1,2,3]
# # # print(l)
# # # # vector 1d array
# # # arr = np.array(l)
# # # print(arr)
# # # # matrix 2d list
# # # l1 = [[1,2,3],[4,5,6]]
# # # print(l1)
# # # # matrix 2d array
# # # arr1 = np.array(l1)
# # # print(arr1)
# # # #tensor 3d array
# # # l2 = [[[1,2],[3,4]],[[5,6],[7,8]]]
# # # arr2 = np.array(l2)
# # # print(arr2)
# # # # tensor 3d list
# # # l3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
# # # print(l3)

# # #array
# # import numpy as np
# # arr = np.arange(11).reshape(11,1)
# # print("shape:",np.shape(arr))
# # print("dimension:", np.ndim(arr))
# # print("size:",np.size(arr))
# # print("data type:", arr.dtype)


# # # 3d mein array ke data ko reverse karke 1 d
# # #flatten it is used to create copy then work
# # import numpy as np
# # arr = np.array([[[1,2],
# #                  [3,4],
# #                  [5,6]]])
# # print(arr)
# # print("flatten")
# # print(arr.flatten())

# # #ravel - it works on original array original ko hi change karta h 
# # import numpy as np
# # arr = np.arange(12).reshape(4,3)
# # print(arr)
# # up_arr = arr.ravel()
# # print(up_arr)
# # print(arr)
# # print("ravel")
# # print(arr.ravel())
# # # example 3d print original array 
# # import numpy as np 
# # arr = np.array([[[1,2],
# #                  [3,4],
# #                  [5,6]]])
# # print(arr)
# # users = [[10,20,30]]
# # # example ravel 3d
# # arr = np.array([[[1,2],
# #                  [3,4],
# #                  [5,6]]])
# # arr = np.arange(12).reshape(2,2,3)
# # print(arr)
# # print("ravel")
# # print(arr.ravel())

# # #transpose
# # import numpy as np
# # arr = np.array([[1,2,3], [4,5,6]])
# # print(arr)
# # print("transpose")
# # print(arr.T)

# # #real life exapmle of transpose 
# # # example1
# # # 3d ke array ko trnspose karna
# # #pehle 2d array banega fir uska transpose hoga then its 3d array
# # import numpy as np
# # arr = np.array([[1,2],
# #                  [3,4],
# #                  [5,6]])
# # print(arr)
# # print("transpose:, ",arr.T )

# #       # slicing for 1d
# # import numpy as np
# # arr = np.arange(10)
# # print(arr)
# # print(arr[0:5])

# #       # slicing for 2d 
# # import numpy as np 
# # arr = np.arange(12).reshape(4,3)
# # print(arr)
# # print(arr[0:2,0:2])
# # print(arr[0:2,1:3])
# # print(arr[1:3,0:2])

# #       # slicing in 3d
# # import numpy as np 
# # arr = np.arange(24).reshape(2,3,4)
# # print(arr)
# # print(arr[0:2,0:2,0:2])

# # import numpy as np 
# # arr = np.arange(24).reshape(2,3,4)
# # print(arr)
# # print(arr[0:2,0:2,0:2])

# # import numpy as np 
# # arr = np.arange(16).reshape(4,4)
# # print(arr)
# # print(arr[0])
# # print(arr[1])
# # print(arr[:,0])
# # arr2 = np.arange(24).reshape(3,4,2)
# # #manually access
# # print(arr2[0][0][0])
# # print(arr2[::2,::3,0])

# # # looping with numpy
# # # 1. while loop 
# # #1d array
# # import numpy as np
# # arr = np.arange(12)
# # i = 0
# # while i < len(arr):
# #     print(arr[i], end = " ")
# #     i += 1
# # #2d array

# # print("2 d array")
# # import numpy as np
# # arr = np.arange(12).reshape(3,4)
# # i = 0
# # while i < len(arr):
# #     j = 0
# #     while j < len(arr[i]):
# #         print(arr[i][j], end = " ")
# #         j += 1
# #     i += 1

# # # 3d array
# # print("\n  array")
# # import numpy as np 
# # arr = np.arange(24).reshape(2,3,4)
# # i = 0
# # while i < len(arr):
# #     j = 0
# #     while j < len(arr[i]):
# #         k = 0
# #         while k < len(arr[i][j]):
# #             print(arr[i][j][k],end = " ")
# #             k +=1
# #             j +=1
# #             i +=1
# # #2. for loop
# # # 1d array
# # import numpy as np 
# # arr = np.arange(12)
# # for i in arr:
# #     print(i, end = " ")

# # #2d array
# # print("2d array")
# # import numpy as np
# # arr = no.arange(12).reshape(3,4)
# # for i in arr:
# #     for j in i:
# #         print(j,end = " ")
# # #3d array 
# # print("3d array")
# # import numpy as np
# # arr = np.arange(24).reshape(2,3,4)
# # for i in arr:
# #     for i in i:
# #         for j in i:
# #             print(j,end = " ")

# #sorting in numpy
# #1d array sorting
# import numpy as np
# arr = np.array([10,40,30,60,90,7,5])

# # directly
# print("before sorting:", arr)
# arr_sorted = np.sort(arr)
# print("after sorting:", arr_sorted)

# #2d array sorting
# import numpy as np
# #bydefault sorting ascending and descending
# arr = np.array([[10,20,30], [40,50,60]])
# print("before sorting:", arr)
# arr_sorted = np.sort(arr)
# print("after sorting:", arr_sorted)
# print("ascending order:", np.sort(arr, axis = 0))
# print("descending order:", np.sort(arr, axis = 1)[::-1])

# #filter 
# # 1d array filter
# import numpy as np
# arr = np.array([10,20,30,40,50])
# filter_arr = arr > 30
# print(filter_arr)

# #2d array filter
# import numpy as np
# arr = np.array([[10,20,30], [40,50,60]])
# filter_arr = arr > 30
# print(filter_arr)


# # filter for even and odd
# import numpy as np
# arr = np.array([10,20,30,40,50])
# even_filter = arr % 2 == 0
# odd_filter = arr % 2 != 0
# print("even filter:", even_filter)
# print("odd filter:", odd_filter)

# #fancy indexing
# # 1d array 
# #example 1 
# import numpy as np
# arr = np.array([10,20,30,40,50])
# print(arr)
# arr_fancy = arr[[0,2,4]] # 0 index value , 2 , 4 index value
# print(arr_fancy)

# #example 2
# import numpy as np
# arr = np.array([10,20,30,40,50])

# #np.where
# import numpy as np
# #1d array
# arr = np.array([10,20,30,40,50])
# filter_arr = np.where(arr>30)
# print(filter_arr)
# print(arr[filter_arr])
# # if (arr>40):
# # arr + 2
# # else: 
# # arr - 2

# import numpy as np
# arr = np.array([10,20,30,40,50])
# new_arr = np.where( arr> 40) 
# if new_arr[0].size > 0:  # Check if any elements satisfy the condition
#     arr = arr + 2
# else:
#     arr = arr - 2
# print(arr)

# # concatenate
# import numpy as np
# arr1 = np.array([10,20,30])
# arr2 = np.array([40,50,60])
# print( np.concatenate((arr1,arr2)))
# print(np.concatenate((arr1,arr2), axis = 0 ))

# #example 2d array concatenate
# import numpy as np
# arr1 = np.array([[10,20,30], [40,50,60]])
# arr2 = np.array([[70,80,90], [100,110,120]])
# print(np.concatenate((arr1,arr2), axis = 0))
# print(np.concatenate((arr1,arr2), axis = 1))

# q1.  np.sum(a) -> Sum of all elements
import numpy as np
arr = np.array([10,20,30,40,50])
print("Sum of all elements:", np.sum(arr))
# q2. np.mean(a) -> Average = Sum of elements / Number of elements
print("average of all elements:", np.mean(arr))
# np.median(a) -> Middle value after sorting
print("median of all elements:", np.median(arr))
# q4. np.min(a) -> Smallest value in array
print("smallest value in array:", np.min(arr))
# q5. np.max(a) -> Largest value in array
print("largest value in array:", np.max(arr))
 