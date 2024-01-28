class X:
    def __init__(self):
        pass
    def evaluate(self, x):
        return x
    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    def evaluate(self, x):
        return self.i
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def evaluate(self, x):
        return self.p1.evaluate(x) + self.p2.evaluate(x)
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def evaluate(self, x):
        return self.p1.evaluate(x) * self.p2.evaluate(x)
    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def evaluate(self, x):
        return self.p1.evaluate(x) - self.p2.evaluate(x)
    def __repr__(self):
        return f"({repr(self.p1)} - {repr(self.p2)})"

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def evaluate(self, x):
        denominator = self.p2.evaluate(x)
        if denominator == 0:
            raise ValueError("Division by zero")
        return self.p1.evaluate(x) / denominator
    def __repr__(self):
        return f"({repr(self.p1)} / {repr(self.p2)})"

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))
