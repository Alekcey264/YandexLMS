from math import sqrt
 
 
class Indentity:
    def __call__(self, x):
        return x
 
 
class SqrtFun:
    def __call__(self, x):
        return sqrt(x)
 
 
class Const:
    def __init__(self, value):
        self.value = value
 
    def __call__(self, x):
        return self.value
 
 
class Expression:
    def __init__(self, f1, op, f2):
        self.f1 = f1
        self.f2 = f2
        self.op = op
 
    def __call__(self, x):
        a = self.f1(x)
        b = self.f2(x)
        if self.op == '+':
            return a + b
        if self.op == '-':
            return a - b
        if self.op == '/':
            return a / b
        if self.op == '*':
            return a * b
 
 
def main():
    functions = {'x': Indentity(), 'sqrt_fun': SqrtFun()}
    n = int(input())
    for _ in range(n):
        command, *args = input().split()
        if command == 'define':
            name, f1, op, f2 = args
            if f1.isdigit() or (f1[0] == '-' and f1[1:].isdigit()):
                f1 = Const(int(f1))
            else:
                f1 = functions[f1]
            if f2.isdigit() or (f2[0] == '-' and f2[1:].isdigit()):
                f2 = Const(int(f2))
            else:
                f2 = functions[f2]
            functions[name] = Expression(f1, op, f2)
        elif command == 'calculate':
            name, *x_values = args
            print(' '.join(str(functions[name](int(x))) for x in x_values))
 
 
if __name__ == '__main__':
    main()