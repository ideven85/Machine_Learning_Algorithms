from math import sqrt


class Vector:
    def __init__(self,x=0,y=0):
        self._x=x
        self._y=y

    def __len__(self):
        return sqrt(abs(self._x**2+self._y**2))


    def __repr__(self):
        return f"Vector({self._x},{self._y})"

    def quadrant(self):
        matrix=[self._x,self._y]
        if matrix[0]>=0 and matrix[1]>=0:
            return "First Quadrant"
        elif matrix[0] > 0 >= matrix[1]:
            return "Second Quadrant"
        elif matrix[0] < 0 <= matrix[1]:
            return "Third Quadrant"
        else:
            return "Fourth Quadrant"

    def getX(self): return self._x

    def getY(self): return self._y
    def __add__(self,other):
        assert type(other) is Vector
        return Vector(self._x+other.getX(),self._y+other.getY())
    """
    Call is used for decorators, to make function decorator
    
    """
    def __call__(self, *args, **kwargs):
        return self._x


if __name__ == '__main__':
    v1 = Vector(3,4)
    print(v1.quadrant())
    v2 = Vector(-3,5)
    print(v1+v2)
    assert callable(Vector)
    print(callable(v1))
