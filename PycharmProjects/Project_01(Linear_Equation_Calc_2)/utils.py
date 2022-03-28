def det(mat, n):
    if n == 2:
        determinant = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
        return determinant
    else:
        minor = [[0 for u in range(n-1)]for v in range(n-1)]
        determinant = 0
        s = 1
        for i in range(n):
            c1, c2 = 0, 0
            for j in range(n):
                for k in range(n):
                    if j != 0 and k != i:
                        minor[c1][c2] = mat[j][k]
                        c2 += 1
                        if c2 > n-2:
                            c1 += 1
                            c2 = 0
            determinant = determinant + s*(mat[0][i]*det(minor, n-1))
            s *= -1
        return determinant


def inverse(A, n):
    determinant = det(A, n)
    if determinant == 0:
        print("Inverse doesn't exist")
    else:
        minor = [[0 for u in range(n - 1)] for v in range(n - 1)]
        Adj = [[0 for u in range(n)]for v in range(n)]
        for i in range(n):
            for j in range(n):
                c1, c2 = 0, 0
                for k in range(n):
                    for l in range(n):
                        if k != i and l != j:
                            minor[c1][c2] = A[k][l]
                            c2 += 1
                            if c2 > n-2:
                                c1 += 1
                                c2 = 0
                Adj[j][i] = det(minor, n-1)*((-1)**(i + j))/determinant
        return Adj

