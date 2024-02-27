## Project title: Are You Ready?
## Roland Yang
## 2/26/24
## On my honor, I have neither given nor received unauthorized help on this
## assignment

# initialize

def int_input(prompt):
  """Input a prompt and cast it to integer"""
  out = int(input(prompt)) # cast to integer
  print(out)
  return out

def restrict_int_input(prompt):
  """Input but restrict the output."""
  num = int_input(prompt)
  if 0 < num > 10: # restrict the allowed values
    raise ValueError("value should be between 0 and 10!")
  return num

def main():
  print("ARE YOU PREPARED (TO GIVE A PRESENTATION, TAKE A TEST, ETC)?\n")

  # input
  importance = restrict_int_input('Enter the importance of the event (1 - 10 with 10 being "singing the national anthem at the Super Bowl"): ')
  sleep = int_input("Enter the hours of sleep you had last night: ")
  shots = int_input("Enter the shots of espresso or other stimulants consumed: ")
  excel = int_input("Enter the hours of preparation needed to excel: ")
  if excel <= 0: # prevent divide by zero by restricting excel to be nonzero.
    raise ValueError("Excelling hours should be positive!! ") 
  prepare = int_input("Enter the hours you actually spent preparing: ")
  difficulty = restrict_int_input('Enter the difficulty of the subject matter (1 - 10 with 10 being "theoretical particle physics"): ')
  nervousness = restrict_int_input('Enter the level of nervousness (1 - 10 with 10 being "tightrope across the Grand Canyon on a windy day"): ')

  # process
  numberator = 8*prepare*(sleep+shots)
  denominator = 3*excel*(difficulty+nervousness+importance)
  if denominator == 0:
    raise ValueError("cannot have a zero in the denominator!")

  # output
  print()
  print("If your level of Preparedness is greater than 1, you will be just fine.")
  output = numberator / denominator
  print("Your level Preparedness is ", output)
  """
  if output > 1: # bonus
    print("GO IN CONFIDENCE")
  else:
    print("YOU NEED MORE PREPARATION")
  """

# terminate

main()
