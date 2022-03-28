class Matrix:
    def __init__(self, arr=[]):
        self.arr = arr
        self.numrows = len(self.arr)
        self.numcols = len(self.arr[0])
        if self.numrows == self.numcols:
            self.square_mat = True
            self.order = self.numrows
        else:
            self.square_mat = False
        pass

    def det(self):
        if self.square_mat:
            if self.order == 2:
                determinant = self.arr[0][0] * self.arr[1][1] - self.arr[0][1] * self.arr[1][0]
                return determinant
            else:
                minor = Matrix([[0 for u in range(self.order - 1)] for v in range(self.order - 1)])
                determinant = 0
                s = 1
                for i in range(self.order):
                    c1, c2 = 0, 0
                    for j in range(self.order):
                        for k in range(self.order):
                            if j != 0 and k != i:
                                minor.arr[c1][c2] = self.arr[j][k]
                                c2 += 1
                                if c2 > self.order - 2:
                                    c1 += 1
                                    c2 = 0
                    determinant = determinant + s * (self.arr[0][i] * Matrix.det(minor))
                    s *= -1
                return determinant
        else:
            raise ValueError("Determinant doesn't exist: Not a square matrix!")

    def prnt(self):
        for rows in self.arr:
            print(rows)

    def dim(self):
        return self.numrows, self.numcols

    def inverse(self):
        if self.square_mat:
            determinant = self.det()
            if determinant == 0:
                print("Inverse doesn't exist")
            elif self.order == 2:
                inv = Matrix([[0, 0], [0, 0]])
                for u in range(2):
                    for v in range(2):
                        inv.arr[u][v] = self.arr[u][v]*(-1)**(u+v)
                tmp = inv.arr[0][0]
                inv.arr[0][0] = inv.arr[1][1]
                inv.arr[1][1] = tmp
                return inv
            else:
                minor = Matrix([[0 for u in range(self.order - 1)] for v in range(self.order - 1)])
                inv = Matrix([[0 for u in range(self.order)]for v in range(self.order)])
                for i in range(self.order):
                    for j in range(self.order):
                        c1, c2 = 0, 0
                        for k in range(self.order):
                            for l in range(self.order):
                                if k != i and l != j:
                                    minor.arr[c1][c2] = A.arr[k][l]
                                    c2 += 1
                                    if c2 > self.order-2:
                                        c1 += 1
                                        c2 = 0
                        inv.arr[j][i] = minor.det()*((-1)**(i + j))/determinant
                return inv
        else:
            raise ValueError("Inverse doesn't exist: Not a square matrix")

    def dot(self, mat2):
        output = Matrix([[0 for u in range(self.numrows)] for v in range(mat2.numcols)])
        for i in range(self.numrows):
            for j in range(mat2.numcols):
                val = 0
                for k in range(self.numcols):
                    val += self.arr[i][k] * mat2.arr[k][j]
                output.arr[i][j] = val
        return output

