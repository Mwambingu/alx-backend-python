#!/usr/bin/env python3

def add(num1: int, num2: int, num3: int) -> int:
  return num1 + num2 + num3

print(add(1,2,3))

# Complicated Types
type_imported = False

# Working with lists
if type_imported:
  from typing import List
  x: List[List[int]] = []
else:
  try:
    x: list[list[int]] = []
  except TypeError:
    print('List hasn\'t been imported!')
  
#Working with Dictionaries
if type_imported:
  from typing import Dict
  y: Dict[str, str] = {"a": "b"}
else:
  try:
    y: dict[str, str] = {"a": "b"}
  except TypeError:
    print('Dict hasn\'t been imported!')

# Custom Types
from typing import List, Dict, Set, Optional, Any, Sequence
Vector = List[float]

def foo(v: Vector) -> Vector:
  print(v)

foo([1.3, 3.5, 2.5])
print(foo.__annotations__)

# Special Types
def foo2(output: Optional[bool]=False):
  pass

print(foo2.__annotations__)

def foo3(output: Any):
  pass

print(foo3.__annotations__)

# Working with Sequences
