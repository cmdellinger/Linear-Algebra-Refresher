# implementation of a vector class for linear algerbra refresher

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

def __str__(self):
    return 'Vector: {}'.format(self.coordinates)
    
    def __eq__(self, other):
        return self.coordinates == other.coordinates
    
    def __add__(self, other):
        return Vector(map(lambda x,y: x+y, self.coordinates, other.coordinates))
    
    def __sub__(self, other):
        return Vector(map(lambda x,y: x-y, self.coordinates, other.coordinates))
    
    def __rmul__(self, scalar):
        return Vector(map(lambda x: x*scalar, self.coordinates))
