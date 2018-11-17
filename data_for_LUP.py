import random
import Matrix_utils as mu

def write_data(L, U, X, filename, iter_number):
   matrix = [[0 for _ in range(len(X))] for _ in range(len(X))]
   matrix = mu.matrix_dot(L, U)
   B = mu.matrix_vector_dot(matrix, X)
   with open(f'Data/data({filename}){iter_number}', 'w') as f:
      for _i in range(len(matrix)):
         for _j in range(len(matrix)):
            f.write(str(matrix[_i][_j]) + ',')
         f.write(str(B[_i])+ ',' + str(X[_i]) + '\n')

def gen_b_data(data_size):
   nums_of_b = 100
   for size_temp in range(1, data_size):
      size = 2**size_temp
      L = [[0 for _ in range(size)] for _ in range(size)]
      U = [[0 for _ in range(size)] for _ in range(size)]
      X = list()
      B = list()
      for _k in range(size):
            for _j in range(_k + 1):
               L[_k][_j] = round(random.uniform(1, 10), 0)
               U[_j][_k] = round(random.uniform(1, 10), 0)
      matrix = mu.matrix_dot(L, U)
      for _j in range(nums_of_b):
         x_temp = [round(random.uniform(1, 10), 0) for _ in range(size)]
         X.append(x_temp)
         b_temp = mu.matrix_vector_dot(matrix, x_temp)
         B.append(b_temp)
      with open(f'Data/data_b({size})', 'w') as f:
         for _j in range(size):
            for _k in range(size):
               f.write(f'{matrix[_j][_k]} ')
            for _k in range(nums_of_b):
               f.write(f'{X[_k][_j]} {B[_k][_j]} ')
            f.write('\n')
      
def gen_data(data_size, iter_number):
   for i in range (2, data_size):
      L = [[0 for _ in range(i)] for _ in range(i)]
      for _k in range(i):
         for _j in range(_k + 1):
            L[_k][_j] = round(random.uniform(1, 10), 0)
      U = [[0 for _ in range(i)] for _ in range(i)]
      for _k in range(i):
         for _j in range(_k + 1):
            U[_j][_k] = round(random.uniform(1, 10), 0)
      X = [round(random.uniform(1, 10), 0) for _ in range(i)]
      write_data(L, U, X, f'{i}', f'{iter_number}')
      # print(U)


if __name__ == '__main__':
   #for i in range(1):
      #gen_data(100, f'{i+1}')
   gen_b_data(13)