# Project title: Book Code (ISBN) isbn.py
# Author: Roland Yang
# N/N/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

def checksum(isbn):
  isbn = isbn[:-2] # remove checksum
  nums = [int(n) for n in isbn if n != "-"] # remove dashes and work with ints
  weighted = 0
  for i in range(len(nums)):
    weighted += nums[i]*(i+1) # add 1 to account for zero based indexing
  weighted %= 11 # take the remainder
  # remainder will never be above 10
  return "X" if weighted == 10 else str(weighted)

def verify_checksum(checksum, isbn):
  return isbn[-1] == checksum

def main():
  # input
  isbn = input("Enter an ISBN number: ")

  # compute
  check_sum = checksum(isbn)
  valid = verify_checksum(check_sum, isbn)

  outcome = "Values do not match, ISBN entered is invalid"
  if valid:
    outcome = "Values match, ISBN entered is valid"

  # tentative output, will probably be changed
  print(isbn) # satisfy submitty

  print("OUTCOME:", outcome)

main()
