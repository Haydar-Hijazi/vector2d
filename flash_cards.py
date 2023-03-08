import random
from vector2d import Vector2d
#Polar Conversion to Rectangular
def print_polar_conversion(vector):
    print("-" * 30)
    print("Convert")
    print("-"*30)
    print(vector)
    print(f"to polar form")
    print("-" * 30)
#Rectangular Conversion to Polar
def print_rectangular_conversion(vector):
    print("-" * 30)
    print("Convert")
    print(f"{abs(vector)} + {vector.angle()}")
    print("-"*30)
    print(f"to rectangular form")
    print("-" * 30)
#Random Vector Generator
def generate_vector():
   return Vector2d(random.randint(-20,21),random.randint(-20,21))
#Polar Solution
def print_polar_conversion_solution(vector):
   print("-"*30)
   print("Answer")
   print("-"*30)
   print(f"{abs(vector)} + {vector.angle()}")
   print("-"*30)
#Rectangular Solution
def print_rectangular_conversion_solution(vector):
   print("-"*30)
   print("Answer")
   print("-"*30)
   print(vector)
   print("-" * 30)
#Menu
def main_menu():
 print("#"*20)
 print("Flash Cards")
 print("1. Conversions")
 print("2. Addition")
 print("q. Quit")
 print("Choose an option:")
 print("#"*20,"\n")
 mode = input()
 if mode == "q":
  print("Goodbye!")
  if mode == "1":
   def conversion_menu():
    if __name__ == '__main__':
     while True:
      print("#"*50)
      print("p. Polar to Rectangular")
      print("r. Rectangular to Polar")
      print("m. Mixed Practice")
      print("q. Return to Main Menu")
      print("#"*50)
      practice = input()
      if practice == "p":
       a = generate_vector()
       print_polar_conversion(a)
      if practice == "r":
       a = generate_vector()
       print_rectangular_conversion(a)
      if practice == "p":
       print("*Type Enter to see the answer*")
       input()
       print_polar_conversion_solution(a)
      if practice == "r":
       print("*Type Enter to see the answer*")
       input()
       print_rectangular_conversion_solution(a)
      if practice == "m":
       mixed = random.randint(1,2)
       if mixed == 1:
        print_polar_conversion(a)
       if mixed == 2:
        print_rectangular_conversion(a)
        print("*Type Enter to see the answer*")
        input()
       if mixed == 1:
        print_polar_conversion_solution(a)
       if mixed == 2:
        print_rectangular_conversion_solution(a)
      if practice == "q":
        print(main_menu())