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

#if Tensor has op --> it is a node
#for two paths, each node stores two grads, one for each parent
#the total grad for the ancestor tensors is given by multiplying e
#finish path 1 --> raise flag --> add future grad to past
    def backward(self,upstream=1.0): #pass 1 into final.backward(1)   
        self.grad += upstream
        if self.op == "mul":
            t1 = self.parents[0]
            t2 = self.parents[1]
            grad_to_t1 = t2.value * upstream
            grad_to_t2 = t1.value * upstream
            t1.backward(grad_to_t1)
            t2.backward(grad_to_t2)
        elif self.op == "add":
            t1 = self.parents[0]
            t2 = self.parents[1]
            grad_to_t1 = 1 * upstream
            grad_to_t2 = 1 * upstream
            t1.backward(grad_to_t1)
            t2.backward(grad_to_t2)
        elif self.op == None:
            return

def zero_grads(*tensors):
    for t in tensors:
        t.grad = 0.0

print("=== TEST ===")
x = Tensor(2.0)
y = Tensor(3.0)
z = Tensor(7.0)

k = x.add(y)        # a = x*y
g = k.mul(z)        # b = z^2  (dead branch, not used)
f = g.mul(g)        # L = x*y + x

zero_grads(x, y, z, k, g, f)
f.backward()

# dL/dx = y + 1 = 4
# dL/dy = x     = 2
# dL/dz = 0, because b is not connected to L
print("x.grad (expected):", x.grad)
print("y.grad (expected):", y.grad)
print("z.grad (expected):", z.grad)
print("b.grad (expected):", k.grad)
print()
