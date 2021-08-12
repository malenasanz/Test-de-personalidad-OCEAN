import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as npl


#ejercicio 5.1.1.

matriz = [[1/3, 1/2, 0],[1/3,0,1/2], [1/3, 1/2, 1/2]]
M = np.array(matriz)
vector = [1/3, 1/3, 1/3]
v = np.array(vector)
c = []
diferencia = []
converg = []

for i in range(40):
    i = i + 1
    A = npl.matrix_power(M, i)
    B = np.dot(A,v)
    c.append(B)
    dif = np.abs(c[i-1] - c[i-2])
    diferencia.append(dif)
    
    
for i in range (1,40):
    d = np.array([0.000000000000001,0.000000000000001,0.000000000000001])
    e = np.less(diferencia[i],d)
    h = e.all()
    if h == True:
        converg.append(i)
print(converg[0]-1)
        
M_33 = npl.matrix_power(M,33)
vec = np.dot(M_33,v)
print(vec)

#ejercicio 5.1.2. 

v_prima = 0.8*vec + (0.2/3)*np.array([1,1,1])
print(v_prima)

#ejercicio 5.1.3

A = np.array([[0, 1/4, 1/4, 1/4, 0], [1/4, 0, 1/4, 1/4, 0], [1/4, 1/4, 0, 1/4, 0],[1/4, 1/4, 1/4, 0,0], [1/4, 1/4, 1/4, 1/4, 0]])
v_0 = np.array([1/5,1/5,1/5,1/5,1/5])

B = npl.matrix_power(A,30)
v = np.dot(B,v_0)
print(v)

#tiende a (0,0,0,0)

#modifico

a = [1/3,1/3,1/3,1/3]
A_prima = np.array([a,a,a,a])
np.fill_diagonal(A_prima,0)
v_0_prima = np.array([1/4,1/4,1/4,1/4])

B_prima = npl.matrix_power(A_prima,30)
v_primaprima = np.dot(B_prima, v_0_prima)
print(v_primaprima)

#ahora es (1/4,1/4,1/4,1/4). tiene sentido porque es simetrico

#la probabilidad del otro nodo es 4*(1/4)*(1/4) = 1/4

#la probabilidad en general es 1/n de estar en cada pag











          
    
   



