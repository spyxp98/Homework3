def matrix_dot(A, U):
   n = len(A)
   res = [[0 for _ in range(n)] for _ in range(n)]
   for _i in range(n):
      for _j in range(n):
         res[_i][_j] = sum(A[_i][_k] * U[_k][_j] for _k in range(n))
   return res

def matrix_vector_dot(A, X):
   n = len(A)
   res = [0 for _ in range(n)]
   for _i in range(n):
      res[_i] = sum(A[_i][_k] * X[_k] for _k in range(n))
   return res
def matrix_transpose(matrix):
   n = len(matrix)
   matrix_tr = [[0 for _ in range(n)] for _ in range(n)]
   for _i in range(n):
      for _j in range(n):
         matrix_tr[_i][_j], matrix_tr[_j][_i] = matrix[_j][_i], matrix[_i][_j]
   return matrix_tr

def matrix_print(matrix):
   for _i in range(len(matrix)):
      print(matrix[_i])

def matrix_pivot(matrix):
   size = len(matrix)
   perm = [s for s in range(size)]
   for _j in range(size):
      max_elem = 0
      imax = _j
      for _i in range(_j, size):
         if matrix[_i][_j] > max_elem:
            max_elem = matrix[_i][_j]
            imax = _i
      matrix[_j], matrix[imax] = matrix[imax], matrix[_j]
      perm[_j], perm[imax] = perm[imax], perm[_j]
   return perm

# def matrix_pivot(matrix):
   # size = len(matrix)
   # P = [[0 for _ in range(size)] for _ in range(size)]
   # for cnt in range(size):
      # P[cnt][cnt] = 1
   # 
   # for _i in range(size):
      # max_elem = 0
      # jmax = 0
      # for _j in range(_i + 1, size):
         # if matrix[_j][_i] > max_elem:
            # jmax = _j
            # max_elem = matrix[_j][_i]
      # P_temp = [[0 for _ in range(size)] for _ in range(size)]
      # for cnt in range(size):
         # P_temp[cnt][cnt] = 1
      # P_temp[_i], P_temp[jmax] = P_temp[jmax], P_temp[_i]
      # matrix_print(P_temp)
      # P = matrix_dot(P_temp, P)
      # print('\n')
   # matrix_print(P)
   # return P


if __name__ == '__main__':
   A = [[0, 2, 1, 4], [7, 0, 1, 2], [5, 2, 0, 1], [10, 9, 8, 0]]
   P = [[1, 0, 0], [0, 0, 1], [0, 1, 0]]
   perm = matrix_pivot(A)
   matrix_print(A)
   print(perm)
   # matrix_pivot(A)
   # matrix_print(matrix_dot(matrix_pivot(A), A))