import numpy as np

def gauss_jordan_inversion(A):
    n = len(A)

    I = np.eye(n)
 
    augmented_matrix = np.hstack([A, I])
    
    for i in range(n):
        
        if augmented_matrix[i, i] == 0:
            raise ValueError("La matriz no es invertible")
        
       
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        
       
        for j in range(n):
            if j != i:
                augmented_matrix[j] -= augmented_matrix[j, i] * augmented_matrix[i]
    
  
    inverse = augmented_matrix[:, n:]
    return inverse

def verificar_inversa(A, A_inv):
    
    result = np.dot(A, A_inv)
 
    return np.allclose(result, np.eye(len(A)))


A = np.array([[3, 2, 2], [3, 1, -3], [1, 0, -2]], dtype=float)
B = np.array([[1, 2, 0], [2, 0, -1], [1, 0, 1], [4, -1, 1], [4, -2, 0]], dtype=float)

A_inv = gauss_jordan_inversion(A)
print("Inversa de A:")
print(A_inv)


if verificar_inversa(A, A_inv):
    print("La inversa de A es correcta.")
else:
    print("La inversa de A no es correcta.")


B_inv = gauss_jordan_inversion(B)
print("\nInversa de B:")
print(B_inv)

 
if verificar_inversa(B, B_inv):
    print("La inversa de B es correcta.")
else:
    print("La inversa de B no es correcta.")
