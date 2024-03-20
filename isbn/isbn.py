# Project title: Book Code (ISBN) isbn.py
# Author: Roland Yang
# 3/18/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

def weighted_sum(isbn):
  isbn = isbn[:-2] # remove checksum
  nums = [int(n) for n in isbn if n != "-"] # remove dashes and work with ints
  weighted = 0
  for i in range(len(nums)):
    weighted += nums[i]*(i+1) # add 1 to account for zero based indexing
  return weighted

def checksum(isbn):
  weighted = weighted_sum(isbn) % 11 # take the remainder
  # remainder will never be above 10
  return "X" if weighted == 10 else str(weighted)

def checkdigit(checksum, isbn):
  return isbn[-1] == checksum

def main():
  # input
  isbn = input("Enter an ISBN number: ")

  # process
  weighted = weighted_sum(isbn)
  check_digit = checksum(isbn)
  isbn_check_digit = isbn[-1]

  valid = checkdigit(check_digit, isbn)

  outcome = "Values do not match, ISBN entered is invalid"
  if valid:
    outcome = "Values match, ISBN entered is valid"

  # output
  print(isbn) # satisfy submitty
  print()

  print("RESULT:\n")
  print("  Check sum: {}\n".format(weighted))
  print("  Check digit: {}\n".format(check_digit))
  print("  ISBN check digit: {}\n".format(isbn_check_digit))

  print("OUTCOME: {}\n".format(outcome))
  print("END RUN.")

  # terminate

main()
