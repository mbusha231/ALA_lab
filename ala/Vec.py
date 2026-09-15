from __future__ import annotations
from typing import Self
import math
import random

class Vec:
  def __init__(self, src=None) -> None:
    if src is None:
      self.elements = tuple()
    else:
      elements = tuple(src)
      for x in elements:
        if not isinstance(x, (int, float)):
          raise TypeError(f"All elements must be numbers: {type(x)}")
      self.elements = elements

  def __add__(self, t: Self) -> Self:
    if not isinstance(t,Vec):
      raise TypeError(f"Expected vector: {type(t)}")
    if len(self.elements) != len(t):
      raise TypeError(f"Type error vectors must have same length")
    return Vec(tuple(round(x+y, 5) for x, y in zip(self.elements, t.elements)))

  def __mul__(self, scalar: int | float) ->Self:
    if not isinstance(scalar, (int ,float)):
        raise TypeError(f"vector multi with invalid type: {type(scalar)}")
    return Vec(tuple(round(x*scalar, 5) for x in self.elements))

  def __rmul__(self, scalar: int|float) ->Self:
    return self.__mul__(scalar)
     
  def __imul__(self, scalar: int|float) ->Self:
    if not isinstance(scalar, (int, float)):
      raise TypeError(f"invalid type: {type(scalar)}")
    scaled_elements = tuple(round(val * scalar, 5) for val in self.elements)
    self.elements = tuple(scaled_elements)
    return self

  def __repr__(self) -> str:
    return f"Vec({self.elements})"

  def __len__(self) -> int:
    return len(self.elements)

  def __sub__(self, t: Self) -> Self:
    if not isinstance(t, Vec):
      raise TypeError(f"Expected vector: {type(t)}")
    if len(self.elements) != len(t):
        raise RuntimeError("vec must have same dimensions")
    return Vec(
      tuple(a-b for a, b in zip(self.elements, t.elements))
    )

  def __neg__(self) -> Self:
    if not self.elements:
      raise RuntimeError("Cannot negate empty vector")
    return Vec(tuple(-x for x in self.elements))

  def __radd__(self, other: Self) -> Self:
    if not isinstance(other, Vec):
      raise TypeError(f"Expected vector: {type(other)}")
    if len(self.elements) != len(other.elements):
      raise RuntimeError("vec must have same dimensions")
    return Vec(
      tuple(a+b for a, b in zip(self.elements, other.elements))
    )

  def __iadd__(self, other: Self) -> Self:
    if not isinstance(other, Vec):
      raise TypeError(f"Expected vector: {type(other)}")
    if len(self.elements) != len(other.elements):
      raise RuntimeError("vec must have same dimensions")
    self.elements = tuple(a+b for a, b in zip(self.elements, other.elements))
    return self

  @staticmethod
  def zeros(n: int) -> 'Vec':
    if n <= 0:
      raise RuntimeError("size must be greater than 0")
    tuple_of_zeros = (0,) * n
    return Vec(tuple_of_zeros)

  @staticmethod
  def ones(n:int)-> 'Vec':
    if n <= 0:
      raise RuntimeError("size must be greater than 0")
    tuple_of_ones = (1,) * n
    return Vec(tuple_of_ones)

  @staticmethod
  def uniform(n:int) -> Self:
    if n <= 0:
      raise RuntimeError("size must be greater than 0")
    return Vec(tuple(random.uniform(0,1) for _ in range(n)))

  def norm(self) -> float:
    if len(self.elements) == 0:
      raise RuntimeError("Vector cannot be empty for norm calculation")
    return math.sqrt(sum(x**2 for x in self.elements))

  def __eq__(self, other) -> bool:
    if isinstance(other, Vec):
      return self.elements == other.elements
    if isinstance(other, (list, tuple)):
      return self.elements == tuple(other)
    return False
  
  def mean(self) -> float:
    if len(self.elements) == 0:
      raise RuntimeError("cannot calcualte mean")
    return sum(self.elements)/len(self.elements)
  
  def demean(self) -> Self:
    mean_val = self.mean()
    new_val = tuple(x- mean_val for x in self.elements)
    return Vec(new_val)
  
  def variance(self) -> float:
    if len(self.elements) == 0:
      raise RuntimeError("cannot calcualte variance")
    demened_vec = self.demean()
    vari_diff = tuple(x**2 for x in demened_vec.elements)
    return sum(vari_diff)/len(self.elements)
  
  