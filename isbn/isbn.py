# Title: Book Code (ISBN) mystery.py
# Author: Roland Yang
# N/N/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

def checksum(isbn):
  isbn = isbn[:-2] # remove checksum
  nums = [int(n) for n in isbn if n != "-"] # remove dashes and work with ints
  weighted = 0
  for i in range(0, len(nums)):
    weighted += nums[i]*(i+1) # add 1 to account for zero based indexing
  weighted %= 11 # take the remainder
  if weighted == 10: # remainder will never be above 10
    weighted = "X"
  else:
    weighted = str(weighted)
  return weighted

def verify_checksum(checksum, isbn):
  return isbn[-1] == checksum

def main():
  # input
  isbn = input("Enter an ISBN number: ")
  print(isbn) # satisfy submitty

  check_sum = checksum(isbn)
  valid = verify_checksum(check_sum, isbn)

  # output
  





  i = "1-23-123123-8"
  c = checksum(i)
  print(verifyChecksum(c,i))

main()
