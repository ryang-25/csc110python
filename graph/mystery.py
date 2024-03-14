# mystery.py
# Roland Yang
# N/N/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

from bpp import read_dimensions, read_pixels, output_file

def print_in(x):
    """ Accept input and print out the input to the terminal with a newline. """
    ret = input(x)
    print(ret)
    return ret

def decryptPixel1(r,g,b):
  r = g = b = r*10
  return (r,g,b)
def decryptPixel2(r,g,b):
  r = 0
  g *= 20
  b *= 20
  return (r,g,b)
def decryptPixel3(r,g,b):
  b *= 16
  if b >= 256:
    r = g = b = 255
  return (r,g,b)
def decryptPixel3(r,g,b):
  return None
def decryptPixel4(r,g,b):
  return None
def decryptPixel5(r,g,b):
  """
    Decrypts a pixel with data located in the 4 low bits. Shifts by 4 and
    masks by 255 very quickly instead of a contrived string manipulation
  """
  maskShift = lambda n : n << 4 & 255
  (maskShift(r), maskShift(g), maskShift(b))

def main():
  # input
  filename = input("hey bud give me the filename")
  algorithm = int(input("hey bud which algorithm are you using"))
  file = open(filename, "r")
  dimensions = read_dimensions(file)
  pixels = read_pixels(file)
  file.close()

  # compute

  # why use an if statement if you have first class functions?
  # just use the index you get
  algorithms = [decryptPixel1, decryptPixel2, decryptPixel3, decryptPixel4, decryptPixel5]
  for i in range(len(pixels)):
    pixels[i] = algorithms[algorithm-1](*pixels[i])

  # output
  # strip the extension
  filename = filename[:-4]
  outname = f"{filename}_OutA0{algorithm}.ppm"
  out = open(outname, "a")
  output_file(out, dimensions[0], dimensions[1], pixels)
  out.close()

main()