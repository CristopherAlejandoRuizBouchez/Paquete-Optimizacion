class FibonacciOptimization:
    def __init__(self, func, a, b, n):
        self.func = func
        self.a = a
        self.b = b
        self.L = b - a
        self.n = n
        self.k = 2

    def fibonacci(self, n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            fib = [0, 1]
            for i in range(2, n + 1):
                fib.append(fib[-1] + fib[-2])
            return fib[n]

    def optimize(self):
        while self.k <= self.n:
            Lk_star = (self.fibonacci(self.n - self.k + 1) / self.fibonacci(self.n + 1)) * self.L
            x1 = self.a + Lk_star
            x2 = self.b - Lk_star

            f_x1 = self.func(x1)
            f_x2 = self.func(x2)

            if f_x1 < f_x2:
                self.b = x2
            else:
                self.a = x1

            self.L = self.b - self.a

            self.k += 1

        return (self.a + self.b) / 2


