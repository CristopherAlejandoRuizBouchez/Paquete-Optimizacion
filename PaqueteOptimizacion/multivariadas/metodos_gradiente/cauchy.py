import numpy as np

class Cauchy:
    def __init__(self, funcion, gradiente, x0, epsilon1, epsilon2, max_iter):
        self.funcion = funcion
        self.gradiente = gradiente
        self.x0 = np.array(x0)
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.max_iter = max_iter

    def buscar_alpha(self, xk, gradiente_xk):
        alpha = 1.0
        while True:
            xk1 = xk - alpha * gradiente_xk
            if np.linalg.norm(self.gradiente(xk1)) <= self.epsilon2:
                break
            alpha *= 0.5  
        return alpha

    def optimizar(self):
        xk = self.x0
        k = 0

        while k < self.max_iter:
            gradiente_xk = self.gradiente(xk)
            if np.linalg.norm(gradiente_xk) <= self.epsilon1:
                break

            alpha_k = self.buscar_alpha(xk, gradiente_xk)
            xk1 = xk - alpha_k * gradiente_xk

            if np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) <= self.epsilon1:
                break

            xk = xk1
            k += 1

        return xk


