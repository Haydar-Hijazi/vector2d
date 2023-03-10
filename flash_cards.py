import random
from vector2d import Vector2d
#Polar Conversion to Rectangular
def print_polar_conversion(vector):
    print("="*30)
    print("-" * 30)
    print("Convert")
    print("-"*30)
    print(vector)
    print("to polar form")
    print("-" * 30)
    print("="*30)
#Rectangular Conversion to Polar
def print_rectangular_conversion(vector):
    print("="*30)
    print("-" * 30)
    print("Convert")
    print(f"{abs(vector)} + {vector.angle()}")
    print("-"*30)
    print("to rectangular form")
    print("-" * 30)
    print("="*30)
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
 #Rectangular Flash Card
def rectangular_flash_card():
  a = generate_vector()
  print_rectangular_conversion(a)
  print("Press Enter to see the answer")
  input()
  print_rectangular_conversion_solution(a)
  print("Press Enter to continue or q to quit")
  n = input()
  if n == "":
   print(rectangular_flash_card())
  if n == "q":
    print(conversion_menu())
#Polar Flash Card
def polar_flash_card(): 
  a = generate_vector()
  print_polar_conversion(a)
  print("Press Enter to see the answer")
  input()
  print_polar_conversion_solution(a)
  print("Press Enter to continue or q to quit")
  n = input()
  if n == "":
   print(polar_flash_card())
  if n == "q":
    print(conversion_menu())
#Conversion Menu
def conversion_menu():
   if __name__ == '__main__':
    while True:
      print("="*25)
      print("Choose Conversion:")
      print("-"*25)
      print("p. Polar to Rectangular")
      print("r. Rectangular to Polar")
      print("m. Mixed Practice")
      print("q. Return to Main Menu")
      print("="*25)
      practice = input()
      if practice == "q":
       print(main_menu())
      if practice == "p":
        print(rectangular_flash_card())
      if practice == "r":
        print(polar_flash_card())
      if practice == "m":
       while True:
        r = random.randint(1,2)
        a = generate_vector()
        if r == 1:
         print_rectangular_conversion(a)
         print("Press Enter to see the answer")
         input()
         print_rectangular_conversion_solution(a)
         print("Press Enter to continue or q to quit")
         n = input()
         if n == "q":
          print(conversion_menu())
        if r == 2:
          print_polar_conversion(a)
          print("Press Enter to see the answer")
          input()
          print_polar_conversion_solution(a)
          print("Press Enter to continue or q to quit")
          n = input()
          if n == "q":
           print(conversion_menu())

          
         
#Addition Menu
def addition_menu():
 pass
#Menu
def main_menu():
 print("="*20)
 print("Flash Cards")
 print("-"*20)
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
   print(addition_menu())
 if mode == "1":
   print(conversion_menu())
 else:
   print("\n!!!Please choose one of the available options!!!\n")
   print(main_menu())

print(main_menu())