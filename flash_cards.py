import random
from vector2d import Vector2d
def print_conversion(vector,type):
    print("-" * 30)
    print("Convert")
    print("-"*30)
    if type == "polar":
      print(vector)
    if type == "rectangular":
      print(f"{abs(vector)} + {vector.angle()}")
    print("-"*30)
    print(f"to {type} form")
    print("-" * 30)
e = Vector2d(3,4)
def generate_vector():
   return Vector2d(random.randint(-20,21),random.randint(-20,21))
def print_conversion_solution():