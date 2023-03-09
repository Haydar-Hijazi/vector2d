import random
from vector2d import Vector2d
#Polar Conversion to Rectangular
def print_polar_conversion(vector):
    print("-" * 30)
    print("Convert")
    print("-"*30)
    print(vector)
    print("to polar form")
    print("-" * 30)
#Rectangular Conversion to Polar
def print_rectangular_conversion(vector):
    print("-" * 30)
    print("Convert")
    print(f"{abs(vector)} + {vector.angle()}")
    print("-"*30)
    print("to rectangular form")
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
#Conversion Menu
def conversion_menu():
   if __name__ == '__main__':
    while True:
      print("="*25)
      print("Choose Conversion:")
      print("p. Polar to Rectangular")
      print("r. Rectangular to Polar")
      print("m. Mixed Practice")
      print("q. Return to Main Menu")
      print("="*25)
      practice = input()
      if practice == "q":
       print(main_menu())
      if practice == "p":
       a = generate_vector()
       print_polar_conversion(a)
       print("Press Enter to see the answer")
       input()
       print_polar_conversion_solution(a)
       print("Press Enter to continue")
       input()
      if practice == "r":
       a = generate_vector()
       print_rectangular_conversion(a)
       print("Press Enter to see the answer")
       input()
       print_rectangular_conversion_solution(a)
       print("Press Enter to continue")
       input()
      if practice == "m":
       b = generate_vector()
       mixed = random.randint(1,2)
       if mixed == 1:
         print_polar_conversion(b)
         print("Press Enter to see the answer")
         input()
         print_polar_conversion_solution(b)
         print("Press Enter to continue")
         input()
       if mixed == 2:
         print_rectangular_conversion(b)
         print("Press Enter to see the answer")
         input()
         print_rectangular_conversion_solution(b)
         print("Press Enter to continue")
         input()
#Menu
def main_menu():
 print("="*20)
 print("Flash Cards")
 print("1. Conversions")
 print("2. Addition")
 print("q. Quit")
 print("Choose an option!")
 print("="*20,"\n")
 mode = input("> ")
 if mode == "q":
  print("\nGoodbye!")
  quit()
 if mode == "2":
   pass
 if mode == "1":
   print(conversion_menu())
 else:
   print("\n!!!Please choose one of the available options!!!\n")
   print(main_menu())

print(main_menu())