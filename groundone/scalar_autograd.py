class Tensor:
    def __init__(self,value,grad=0,parents=None,op=None):
        self.value = value
        self.grad = grad
        self.parents = parents if parents is not None else []
        self.op = op

    def __repr__(self):
        return f"Value(value={self.value}, grad={self.grad}, op={self.op})"
    

    #def backward(self):

x = Tensor(2.0)

print(x)