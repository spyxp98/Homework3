import Matrix_utils as mu
import time

def preload(filename, iter_number):
   size = 0
   with open(f'Data/data({filename}){iter_number}', 'r') as f:
      A = list()
      B = list()
      X = list()
      for line in f:
         temp_line = line.split(',')
         A.append([float(s) for s in temp_line[:-2]])
         B.append(float(temp_line[-2]))
         X.append(float(temp_line[-1]))
   return A, B, X
   
def preload_b(filename):
   nums_of_b = 100
   with open(f'Data/data_b({filename})', 'r') as f:
      A = list()
      B = [[] for _ in range(100)]
      X = [[] for _ in range(100)]
      for line in f:
         temp_line = line.split()
         A.append([float(s) for s in temp_line[:-200]])
         for _k in range(0, -nums_of_b, -2):
            B[_k].append(float(temp_line[_k-1]))
            X[_k].append(float(temp_line[_k]))
   return A, B, X

def LU_decompose(A):
   size = len(A)
   L = [[0 for _ in range(size)] for _ in range(size)]
   U = [[0 for _ in range(size)] for _ in range(size)]
   for _j in range(size):
      L[_j][_j] = 1

      for _i in range(_j + 1):
         s1 = sum(U[_k][_j] * L[_i][_k] for _k in range(_i))
         U[_i][_j] = A[_i][_j] - s1 
         # mu.matrix_print(U)
         # print('\n')
      for _i in range(_j, size):
         s2 = sum(U[_k][_j] * L[_i][_k] for _k in range(_j))
         try:
            L[_i][_j] = (A[_i][_j] - s2) / U[_j][_j]
         except ZeroDivisionError:
            pass
         # mu.matrix_print(L)
         # print('\n')
   return L, U

def LUP_decompose(A, B, X):
   size = len(B)
   perm = mu.matrix_pivot(A)
   for _i in range(size):
      B[_i] = B[perm[_i]]
      X[_i] = X[perm[_i]]
   return LU_decompose(A)

def solve(L, U, B):
   size = len(B)
   y = [0 for _ in range(size)]
   x = [0 for _ in range(size)]
   for _i in range(size):
      y[_i] = B[_i]
      temp_sum = sum(L[_i][_k] * y[_k] for _k in range(_i))
      y[_i] -= temp_sum
   # print(y)
   for _i in range(size-1, -1, -1):
      temp_sum = sum(U[_i][_k] * x[_k] for _k in range(_i+1, size))
      try:
         x[_i] = (y[_i] - temp_sum) / U[_i][_i]
      except ZeroDivisionError:
         pass
   return x

def check_answer(x_true, x):
   return x_true == x
   
def main():
   with open('results', 'w') as f:
      results = dict()
      cnt = dict()
      # for i in range(2, 100):
         # results[i] = 0
         # cnt[i] = 0
      for iter in range(1):
         for _i in range(2, 100):
            A, B, X = preload(f'{_i}', f'{iter + 1}')
            start_time = time.time()
            L, U = LU_decompose(A)
            # print(solve(L, U, B), X)
            if check_answer(solve(L, U, B), X):
               f.write(f'{_i} {time.time() - start_time} \n')
   
def main1():
   with open('results_b', 'w') as f:
      res = [0 for _ in range(10)]
      data_size = 11
      for _i in range(1, data_size):
         A, B, X = preload_b(f'{2**_i}')
         L, U = LU_decompose(A)
         for _k in range(100):
            b_temp = B[_k]
            x_temp = X[_k]
            start_time = time.time()
            ans = solve(L, U, b_temp)
            res[_i-1] += time.time() - start_time
         f.write(f'{2**_i} {res[_i-1]} \n')

if __name__ == '__main__':
   main1()