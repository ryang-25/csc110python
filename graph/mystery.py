# mystery.py
# Roland Yang
# N/N/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

from bpp import read_dimensions, read_pixels, output_file

BYTE_MAX = 255

def print_in(x):
    """ Accept input and print out the input to the terminal with a newline. """
    ret = input(x)
    print(ret)
    return ret

def decryptPixel1(r,g,b):
  """ Sets all values to the red value multiplied by 10. """
  r = g = b = r*10
  return (r,g,b)
def decryptPixel2(r,g,b):
  r = 0
  g *= 20
  b *= 20
  return (r,g,b)
def decryptPixel3(r,g,b):
  """ Less branches. Multiplies by 16 unconditionally and only sets all to 255
      if it overflows a byte. """
  b *= 16
  if b >= BYTE_MAX+1:
    r = g = b = BYTE_MAX
  return (r,g,b)
def decryptPixel4(r,g,b):
  """ Chinese remainder theorem decryption. For all coprime numbers we just need
      to find integer multiples that add up to 1. For 3 and 17, 3(6) - 17(-1) =
      1. Then, for any a % 3, b % 17, you will discover a*-17 + b*18 is
      congruent to both."""
  # for all x:
  # a - x = b
  # x = a - b
  r = 255 - r
  g = 170 - g
  b = 85 - b

  # select i, j such that 3i + 17j = 1
  I = 3*6
  J = 17*-1
  # select k, l such that 5k + 3*17l = 1
  K = 5*-10
  L = 3*17*1

  # m is an integer % 51.
  m = (r*J + b*I)
  r = g = b = (m*K + g*L) % BYTE_MAX
  return (r,g,b)
def decryptPixel5(r,g,b):
  """
    Decrypts a pixel with data located in the 4 low bits. Shifts by 4 and
    masks by 255 very quickly instead of a contrived string manipulation
  """
  maskShift = lambda n : n << 4 & BYTE_MAX
  return (maskShift(r), maskShift(g), maskShift(b))

def main():
  # input
  filename = input("hey bud give me the filename ")
  algorithm_choice = int(input("hey bud which algorithm are you using "))
  file = open(filename, "r")
  dimensions = read_dimensions(file)
  pixels = read_pixels(file)

  # compute

  # why use an if statement if you have first class functions?
  # just use the index you get
  algorithms = [decryptPixel1, decryptPixel2, decryptPixel3, decryptPixel4, decryptPixel5]
  algorithm = algorithms[algorithm_choice-1]
  # yet another comprehension (i'm allergic to indexing)
  pixels = (algorithm(*pixel) for pixel in pixels)

  # output
  # strip the extension
  filename = filename[:-4]
  outname = f"{filename}_OutA0{algorithm_choice}.ppm"
  out = open(outname, "a")
  output_file(out, *dimensions, pixels)
  # lazy io!
  file.close()
  out.close()

main()
