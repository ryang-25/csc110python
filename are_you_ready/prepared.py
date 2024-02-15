# initialize

def int_input(prompt):
  out = int(input(prompt)) # cast to integer
  print(out)
  return out

def restrict_int_input(prompt):
  num = int_input(prompt)
  if 0 < num > 10: # restrict the allowed values
    raise ValueError("value should be between 0 and 10!")
  return num

def main():
  # input
  importance = restrict_int_input("Please enter the Importance of the event (from 1 to 10):")
  sleep = int_input("Please enter the Hours of sleep you had last night:")
  shots = int_input("Please enter the number of Shots of expresso or other stimulants consumed:")
  excel = int_input("Please enter the number of Hours needed to excel:")
  if excel <= 0: # prevent divide by zero by restricting excel to be nonzero.
    raise ValueError("Excelling hours should be positive!!") 
  prepare = int_input("Please enter the number of Hours you actually spent preparing:")
  difficulty = restrict_int_input("Please enter the Difficulty of the subject matter (from 1 to 10):")
  nervousness = restrict_int_input("Please enter your Level of nervousness (from 1 to 10):")

  # process
  numberator = 8*prepare*(sleep+shots)
  denominator = 3*excel*(difficulty+nervousness+importance)
  if denominator == 0:
    raise ValueError("cannot have a zero in the denominator!")

  # output
  print("If your Prepared-ness score is greater that 1, you will be just fine.")
  output = numberator / denominator
  print("Your Preparded-ness score is:", output)
  if output > 1: # bonus
    print("GO IN CONFIDENCE")
  else:
    print("YOU NEED MORE PREPARATION")

# terminate

main()
