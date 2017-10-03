# implementation of a vector class for linear algerbra refresher
from math import acos, degrees

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
    
    def __mul__(self, other):
        ''' default multiplacation behavior is dot product '''
        return Vector.dot(self, other)
    #        return reduce(lambda x,y: x+y, map(lambda x,y: x*y, self.coordinates, other.coordinates))
    
    def __rmul__(self, scalar):
        ''' when multiplacation is not b/t vectors treat as scalar '''
        return Vector(map(lambda x: x*scalar, self.coordinates))
    
    def magnitude(self):
        return (reduce(lambda x,y: x+y, map(lambda x: x**2, self.coordinates)))**0.5
    
    def normalized(self):
        try:
            return (1/self.magnitude())*self
        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    @staticmethod
    def dot(vector1, vector2):
        return reduce(lambda x,y: x+y, map(lambda x,y: x*y, vector1.coordinates, vector2.coordinates))
    
    # angle between vectors in static and instance methods
    @staticmethod
    def __find_angle(vector1, vector2, radians = True):
        ''' private method to find angle between two vectors'''
        try:
            angle = acos(vector1*vector2/(vector1.magnitude() * vector2.magnitude()))
        except ZeroDivisionError:
            raise Exception('Cannot use a vector with magnitude zero')
        if radians:
            return angle
        else:
            return degrees(angle)
    @staticmethod
    def angle_between(vector1, vector2, radians = True):
        ''' static method that can be called with Vector.angle(instance_1, instance_2) '''
        return Vector.__find_angle(vector1, vector2, radians)
    
    def angle_with(self, other, radians = True):
        ''' instance method that is called with instance_name.angle(other_instance) '''
        return Vector.__find_angle(self, other, radians)
