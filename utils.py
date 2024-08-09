from math import sqrt


class Vector():
    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y
        self.Zero = Vector(0, 0)
    
    # Situação de divisão
    def __add__(self, other):
        #  Vector + Vector
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        
        return TypeError
    
    # Situação de divisão
    def __sub__(self, other):
        #  Vector + Vector
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        
        return TypeError
    
    # Situação de multiplicação
    def __mul__(self, other):
         # Vector * Vector
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
        # Vector * Numero
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        # Caso ocorra erro
        return TypeError
    
    # Situação de divisão
    def __truediv__(self, other) :
        # Vector / Vector
        if (isinstance(other, Vector)):
            return Vector(self.x / other.x, self.y / other.y)
        # Vector / Numero
        elif (isinstance(other, (int, float))):
            return Vector(self.x / other, self.y / other)
        
        return TypeError
    
    # Represnta em string a classe, depuração e exibição
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Valores pré-definidos
    @classmethod
    def ZERO(cls):
        return cls(0, 0)
    
    @classmethod
    def LEFT(cls):
        return cls(-1, 0)
    
    @classmethod
    def RIGHT(cls):
        return cls(1, 0)
    
    @classmethod
    def DOWN(cls):
        return cls(0, -1)
    
    @classmethod
    def UP(cls):
        return cls(0, 1)
    
    # Função que normaliza vector, deixando os valores x e y, entre -1 e 1
    def normalized(self):
        magnitude = sqrt(self.x**2 + self.y**2)
    
        if (magnitude != 0):
            v_x_normalized = self.x / magnitude
            v_y_normalized = self.y / magnitude
        else:
            return Vector(0, 0)

        return Vector(v_x_normalized, v_y_normalized)
    
    






