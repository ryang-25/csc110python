# etude04.py
# Roland Yang
# 4/10/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

def reverse(n, base):
  """ Reverse an integer modulo a specific base. """
  acc = 0
  while n != 0:
    acc = acc * base + n % base # multiply accumulator by base and take modulo
    n //= base # reduce by floor
  return acc

def display_base(n, base):
  """ Convert an integer to its base representation.  """
  acc = ""
  while n != 0:
    acc += str(n % base)
    n //= base
  return acc

def palindrone(n, base):
  n = int(n, base) # convert the initial n value to appropriate base
  i = 0
  while n - reverse(n, base) != 0 and i < 10:
    n += reverse(n, base)
    i += 1
  n = reverse(n, base) # final reverse for sum
  out = display_base(n, base)
  if i == 10:
    out = "NONE, " + out # add out if it hits 10
  return out

def main():
  raw_num, base = input().split() # raw data
  num = raw_num[:-1] # remove the comma
  base = int(base) # convert the base string to an int

  print(palindrone(num, base))

if __name__ == '__main__':
  main()