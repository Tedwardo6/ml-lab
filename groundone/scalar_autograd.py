class Tensor:
    def __init__(self,value,grad=0,parents=None,op=None):
        self.value = value
        self.grad = grad
        self.parents = parents if parents is not None else []
        self.op = op

    def __repr__(self):
        return f"Tensor(value={self.value}, grad={self.grad}, op={self.op})"
    
    def add(self,other):
        grad_place = 0
        temp = self.value + other.value
        par = [self,other]
        return Tensor(temp,grad_place,par,"add")
        
    def mul(self,other):
        grad_place = 0
        temp = self.value * other.value
        par = [self,other]
        return Tensor(temp,grad_place,par,"mul")

    def backward(self,upstream): #pass 1 into final.backward(1)
        self.grad += upstream
        if self.op == "mul":
            x = self.parents[0]
            y = self.parents[1]
            grad_to_x = 0
            grad_to_y = 0
            grad_to_x += self.grad * y.value    
            grad_to_y += self.grad * x.value   #error propogating duplicated objects, dont use self.grad for contributions just for storage
            x.backward(grad_to_x)
            y.backward(grad_to_y)
        elif self.op == "add":
            x = self.parents[0]
            y = self.parents[1]
            grad_to_x = 0
            grad_to_y = 0     
            grad_to_x += self.grad
            grad_to_y += self.grad
            x.backward(grad_to_x)
            y.backward(grad_to_y)
        elif self.op == None:
            return

x = Tensor(2.0)
y = Tensor(3.0)
k = Tensor(5.0)

z = x.add(y)
g = z.mul(z)


g.backward(1)

print(g)
print(g.parents)
print(z.parents)