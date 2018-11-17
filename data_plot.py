import matplotlib.pyplot as plt
with open('results', 'r') as f:
   x = list()
   res = list()
   for line in f:
      temp = line.split()
      x.append(float(temp[0]))
      res.append(float(temp[1]))

plt.subplot(1, 2, 1)
plt.plot(x, res)
plt.title('LU-decomposition')
plt.xlabel('Size')
plt.ylabel('Time')

with open('results_b', 'r') as f:
   x_b = list()
   res_b = list()
   for line in f:
      temp = line.split()
      x_b.append(float(temp[0]))
      res_b.append(float(temp[1]))

plt.subplot(1, 2, 2)
plt.plot(x_b, res_b)
plt.title('Solving for diff B')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('log(size)')
plt.ylabel('log(summ time)')
plt.grid(True)

plt.show()