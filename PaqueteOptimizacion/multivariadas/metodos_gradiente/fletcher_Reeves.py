import numpy as np

class OptimizadorGradienteConjugado:
    def __init__(self, funcion, gradiente, x0, epsilon1, epsilon2, epsilon3, max_iter):
        self.funcion = funcion
        self.gradiente = gradiente
        self.x0 = np.array(x0)
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.epsilon3 = epsilon3
        self.max_iter = max_iter

    def buscar_lambda(self, xk, sk):
        lambda_ = 1.0
        while True:
            xk1 = xk + lambda_ * sk
            if self.funcion(xk1) < self.funcion(xk) - self.epsilon1 * lambda_ * np.dot(self.gradiente(xk), sk):
                break
            lambda_ *= 0.5  # Reducir el tamaño del paso
        return lambda_

    def optimizar(self):
        xk = self.x0
        k = 0

        gradiente_xk = self.gradiente(xk)
        sk = -gradiente_xk

        while k < self.max_iter:
            lambda_k = self.buscar_lambda(xk, sk)
            xk1 = xk + lambda_k * sk

            if np.linalg.norm(xk1 - xk) / np.linalg.norm(xk) <= self.epsilon2 or np.linalg.norm(self.gradiente(xk1)) <= self.epsilon3:
                break

            gradiente_xk1 = self.gradiente(xk1)
            beta_k = np.dot(gradiente_xk1, gradiente_xk1) / np.dot(gradiente_xk, gradiente_xk)
            sk = -gradiente_xk1 + beta_k * sk

            xk = xk1
            gradiente_xk = gradiente_xk1
            k += 1

        return xk


