import math

#№1

def rot_matrix(x, y, alpha):
    disp_matrix = [[1, 0, 0], [0, 1, 0], [-x, -y, 1]]
    r_matrix = [[math.cos(alpha), -math.sin(alpha)], [math.sin(alpha), math.cos(alpha)], [0, 0, 1]]
    s = 0
    t = []
    C = []
    r1 =len(disp_matrix)
    c1 = len(disp_matrix[0])
    r2 = c1
    c2 = len(r_matrix[0])
    for z in range(0,r1):
        for j in range(0,c2):
            for i in range(0,c1):
                s = s+disp_matrix[z][i]*r_matrix[i][j]
            t.append(s)
            s = 0
        C.append(t)
        t = []
    for i in range(0,2):
        disp_matrix[2][i] *= -1
    s = 0
    t = []
    final = []
    r1 = len(C)
    c1 = len(C[0])
    r2 = c1
    c2 = len(disp_matrix[0])
    for z in range(0,r1):
        for j in range(0,c2):
            for i in range(0,c1):
                s = s+C[z][i]*disp_matrix[i][j]
            t.append(s)
            s = 0
        final.append(t)
        t = []
    return final

#№2


def normalized(point_A: list, point_B: list, point_C: list):
    """
    :param point_A: координаты точки А
    :param point_B: координаты точки B
    :param point_C: координаты точки C
    :return: координаты нормали
    """

    n_y: int = (point_B[2] - point_A[2]) * (point_C[0] - point_A[0]) - (point_C[2] - point_A[2]) * (
            point_B[0] - point_A[0])
    n_z: int = -((point_B[1] - point_A[1]) * (point_C[0] - point_A[0]) - (point_C[1] - point_A[1]) * (
            point_B[0] - point_A[0]))

    n_x: int = -(n_z * (point_B[2] - point_A[2]) + n_y * (point_B[1] - point_A[1])) / (point_B[0] - point_A[0])

    gcd = math.gcd(int(n_x), int(n_y))  # кратно уменьшим координаты

    gcd = math.gcd(gcd, int(n_z))

    return n_x / gcd, n_y / gcd, n_z / gcd


#№3

def belongs_projection(point_A: list, point_B: list, point_C: list, point_O: list):
    """
    :param point_A: координаты точки А
    :param point_B: координаты точки B
    :param point_C: координаты точки C
    :param point_O: координаты точки, для которой определяется принадлежность
    """

    check_1 = (point_A[0] - point_O[0]) * (point_B[1] - point_A[1]) - \
              (point_B[0] - point_A[0]) * (point_A[1] - point_O[1])

    check_2 = (point_B[0] - point_O[0]) * (point_C[1] - point_B[1]) - \
              (point_C[0] - point_B[0]) * (point_B[1] - point_O[1])

    check_3 = (point_C[0] - point_O[0]) * (point_A[1] - point_C[1]) - \
              (point_A[0] - point_C[0]) * (point_C[1] - point_O[1])

    belongs: bool = (check_1 < 0 and check_2 < 0 and check_3 < 0) or (check_1 > 0 and check_2 > 0 and check_3 > 0)

    if belongs:
        print('Точка принадлежит проекции')
    else:
        print('Точка не принадлежит проекции')

if __name__ == '__main__':

    print('Задание 1:', rot_matrix(5, 5, 0.35), end='\n', sep='\n')

    print('Задание 2:')
    A = [26, 22, 77]
    B = [11, 44, 44]
    C = [90, 19, 25]
    print(normalized(A, B, C), end='\n')

    print('Задание 3:')
    A = [20, 20, 20]
    B = [60, 50, 75]
    C = [30, 120, 100]
    does_belong = [30, 30]
    belongs_projection(A, B, C, does_belong)