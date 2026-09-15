import sys
from typing import Self
#vector implementation
class Vec:
    def __init__(self, src=None) ->Self:
        if src is None:
            self.elements = ()
        else:
            self.elements = tuple(src)
            for x in self.elements:
                if not isinstance(x, (int, float)):
                    raise TypeError(f"scaler must be a number:{type(x)}")
            self.elements = elements
   
    def __add__(self, t: Self) -> Self:
        if not isinstance(t, Vec):
            raise TypeError(f"expected vec: {type(t)}")
        if len(self.elements) != len(t.elements):
            raise TypeError(f"vectors must be same dimensions")
        return Vec(tuple(round(x+y, 5) for x,y in zip(self.elements, t.elements)))
    
    def __rmul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"invalid type: {type(scalar)}")
        return Vec(tuple(round(x*scalar , 5) for x in self.elements))
    
    def __imul__(self, scalar: int | float) -> Self:
        if not isinstance(scalar, (int, float)):
            raise TypeError(f"invalid: {type(scalar)}")
        for i, val in enumerate(self.elements):
            self.elements(i) = round(val * scalar, 5)
        return self
    
    
    
       
    
        
        