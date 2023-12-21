
# function that makes sure input is valid
def valid_input(prompt:str):
  while True:
    try:
      res = float(input(prompt))
      if res > 0:
        return res
      else:
        print("Value must be a real positive number")
    except ValueError:
      print("Value must be a real positive number")

#Asks the user for the length
length = valid_input("Enter the length of the rectangle: ")

#Asks the user for the width
width = valid_input("Enter the width of the rectangle: ")

#Asks the user for the area
guessed_area = f"{valid_input('Guess the area of the rectangle: '):.2f}"
#Calculates Correct Area
correct_area = f"{length*width:.2f}"

#Tells them if they got the number right
if guessed_area == correct_area:
  print(f"The correct area of the rectangle is {correct_area}!")
  print(f"You guessed the area correctly! Your answer: {guessed_area}")
#Tells them if they got it wrong and what the correct answer was
else:
  print(f"The correct area of the rectangle is {correct_area}!")
  print(f"You guessed the area incorrectly! Your answer: {guessed_area}")
