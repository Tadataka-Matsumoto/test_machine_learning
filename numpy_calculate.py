import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)


print(np.zeros(10))
print(np.zeros((3, 2)))


print(np.arange(5))
print(np.arange(2,9))
print(np.arange(5,8,0.5))


c = np.array([1, 2, 3, 4, 5])#初期化
d = c * 2 #計算
print(d)


x = np.arange(10)
y = 3 * x  + 5
print(y)


e = np.array([[1,2,3],[4,5,6]])
print(e.shape)
f = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f.shape)


g = np.array([[1,2,3],[4,5,6]])
print("g=", g)
h = g.flatten()
print("h=",h)

j = np.array([[1,2,3],[4,5,6]])
print(j)
print(j.reshape(3,2))


# Numpy配列の要素にアクセスする方法
v = np.array([[1,2,3],[4,5,6],[7,8,9]])
k = v[0]
l = v[1:]
m = v[: , 0]
print("k=", k)
print("l=", l)
print("m=", m)


