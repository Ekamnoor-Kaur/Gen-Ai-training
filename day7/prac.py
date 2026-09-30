import numpy as np
# n1=np.array([1,2,4,5,6])
# print(n1)
# print(n1.size)
# print(type(n1))
# print(n1.ndim)

# n2=np.array([[1,2,3],[5,4,6]])
# print(n2)
# print(n2.size)
# print(type(n2))
# print(n2.ndim)

# n3=np.array([[[1,2],[4,5],[4,6]]])
# print(n3)
# print(n3.size)
# print(type(n3))
# print(n3.ndim)

# n4=np.array([[[[1,2],[4,5],[4,6],[6,3]]]])
# print(n4)
# print(n4.size)
# print(type(n4))
# print(n4.ndim)

n5=np.array(list(map(int,input("enter number").split())))
print(n5)

n=int(input("enter number of elements"))
n6=np.array([(int(input())) for i in range(n)])

n7=np.zeros(4)
print(n7)

n8=np.zeros((4,4))
print(n8)

n9=np.eye(3)
print(n9)

a = np.array([10, 20, 30, 40, 50])

a[0]      # 10  (first element)
a[-1]     # 50  (last element)
a[1:4]    # [20, 30, 40]  (slice: start:stop)
a[:3]     # [10, 20, 30]  (from beginning)
a[2:]     # [30, 40, 50]  (till end)
a[::2]    # [10, 30, 50]  (step of 2)
a[::-1]   # [50, 40, 30, 20, 10]  (reversed)

b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

b[0, 0]     # 1   (row 0, col 0)
b[1, 2]     # 6   (row 1, col 2)
b[2]        # [7, 8, 9]  (entire row 2)
b[:, 0]     # [1, 4, 7]  (entire column 0)
b[0:2, 1:3] # [[2, 3], [5, 6]]  (sub-matrix)
b[:, ::-1]  # reverses each row

