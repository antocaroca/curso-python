from math import log, gamma, pi

x, y = map(int, input('ingrese números: ').strip().split())

print(gamma(log(pi*x , y)))

#   math.log(x[, base])
#   https://docs.python.org/3/library/math.html
#   jupyter notebook Clase4.ipynb
