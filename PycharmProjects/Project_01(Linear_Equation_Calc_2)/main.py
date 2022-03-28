from matrix import Matrix

a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
b = Matrix([[1, 2], [5, 6], [7, 8], [3, 4]])
c = a.dot(b)
c.prnt()
