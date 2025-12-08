class Vector:
    def __init__(self, data):
        self.data = data
        self.dim = len(data)

    def add(self, other):

        temp = []

        if len(other.data) == len(self.data):
            for i in range(len(self.data)):
                temp.append(other.data[i] + self.data[i]) 

        return Vector(temp)

    def sub(self, other):

        temp = []

        if len(other.data) == len(self.data):
            for i in range(len(self.data)):
                temp.append(self.data[i] - other.data[i]) 

        return Vector(temp)   
    
    def scalar_mult(self, c):
     
        temp = [] 

        for i in range(len(self.data)):
            temp.append(self.data[i] * c)

        return Vector(temp)   

    def dot(self, other):
     
        temp = [] 
        K = 0

        if len(other.data) == len(self.data):
            for i in range(len(self.data)):
                temp.append(self.data[i] * other.data[i]) 

        for item in temp:
            K += item
        
        return K
    
    def get(self):
        
        for i in range(len(self.data)):
            print(self.data[i])


v1 = Vector([1,3,4,5,2])
v2 = Vector([2,4,7,5,3])

v3 = v1.add(v2)
c = v1.dot(v2)

print(c)
v3.get()