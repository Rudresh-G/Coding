
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


def calc1(D, Dx, Dy):
    d = det(D, 2)
    dx = det(Dx, 2)
    dy = det(Dy, 2)
    x = dx/d
    y = dy/d
    return x, y


def calc2(D, Dx, Dy, Dz):
    d = det(D, 3)
    dx = det(Dx, 3)
    dy = det(Dy, 3)
    dz = det(Dz, 3)
    x = dx/d
    y = dy/d
    z = dz/d
    return x, y, z


while True:
    Choice = int(input("Enter type of Equation:\n1)ax + by = c \n2)ax + by + cz = d \n3)Exit\n"))

    if Choice == 1:
        coef = [[0 for u in range(3)]for v in range(2)]
        D = [[0 for u in range(2)]for v in range(2)]
        Dx = [[0 for u in range(2)]for v in range(2)]
        Dy = [[0 for u in range(2)]for v in range(2)]
        for i in range(2):
            for j in range(3):
                coef[i][j] = (float(input(f"Enter the variable-{j} for Equation-{i}\n")))
                if j < 2:
                    D[i][j] = Dx[i][j] = Dy[i][j] = coef[i][j]
                else:
                    Dx[i][j-2] = Dy[i][j-1] = coef[i][j]
        print(coef, D, Dx, Dy)
        result = calc1(D, Dx, Dy)
        print("(x, y) = ", result)

    elif Choice == 2:
        coef = [[0 for u in range(4)] for v in range(3)]
        D = [[0 for u in range(3)] for v in range(3)]
        Dx = [[0 for u in range(3)] for v in range(3)]
        Dy = [[0 for u in range(3)] for v in range(3)]
        Dz = [[0 for u in range(3)] for v in range(3)]
        for i in range(3):
            for j in range(4):
                coef[i][j] = (int(input(f"Enter the variable-{j} for Equation-{i}\n")))
                if j < 3:
                    D[i][j] = Dx[i][j] = Dy[i][j] = Dz[i][j] = coef[i][j]
                else:
                    Dx[i][j - 3] = Dy[i][j - 2] = Dz[i][j - 1] = coef[i][j]
        print(coef, D, Dx, Dy, Dz)
        result = calc2(D, Dx, Dy, Dz)
        print("(x, y, z) = ", result)
    elif Choice == 3:
        break
