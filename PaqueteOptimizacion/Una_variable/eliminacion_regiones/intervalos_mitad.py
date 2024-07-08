class Optimization:
    def __init__(self, func, a, b, epsilon):
        self.func = func
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.xm = (a + b) / 2
        self.L0 = b - a
        self.L = self.L0

    def optimize(self):
        while abs(self.L) >= self.epsilon:
            xm = (self.a + self.b) / 2
            x1 = self.a + self.L / 4
            x2 = self.b - self.L / 4
            
            f_xm = self.func(xm)
            f_x1 = self.func(x1)
            f_x2 = self.func(x2)
            
            if f_x1 < f_xm:
                self.b = xm
                self.xm = x1
            elif f_x2 < f_xm:
                self.a = xm
                self.xm = x2
            else:
                self.a = x1
                self.b = x2
                
            self.L = self.b - self.a
        
        return self.xm

