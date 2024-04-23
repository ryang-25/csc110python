# mystery.py
# Roland Yang
# 3/18/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

import re

# initialize

# whether or not to use graphics.py
USE_GRAPHICS = False
if USE_GRAPHICS:
  from graphics import GraphWin, Image, Point

# max value of a byte
BYTE_MAX = 255

def read_comment(file):
  """ Read the next line that is not a comment """
  line = ""
  while len(line) == 0:
    line = file.readline().split("#")[0]
  return line

def read_dimensions(file):
  """ Read the dimensions off the file. """
  assert file.readline()[:-1] == "P3"
  dimensions = []
  while len(dimensions) < 2:
    line = read_comment(file)
    # this isn't entirely within spec since if the max pixel is on the
    # same line we'll miss it but i don't want to build a whole
    # parser...
    dimensions += [int(x) for x in re.findall(r"\d+", line)]
  return dimensions

def read_pixels(file):
  """ Read the pixels out of the file in integers. """
  max_pixel = int(file.readline()) # unused!
  raw_pixels = [l for l in file.readlines() if len(l.split("#")[0]) != 0]
  lines = "".join(raw_pixels).split() # remove whitespace!
  # read each subpixel value by 3s and group into a logical pixel
  for i in range(0, len(lines), 3):
    r = int(lines[i])
    g = int(lines[i+1])
    b = int(lines[i+2])
    yield (r,g,b)

def output_file(file, x, y, pixels):
  # write headers
  file.write("P3\n")
  file.write("# Roland Yang 3/18/24\n")
  # apparently the grader doesn't like f-strings!!
  file.write("{} {}\n".format(x,y))
  file.write("255\n")
  # write each pixel value
  for pixel in pixels:
    file.write("{} {} {}\n".format(*pixel))

# output the binary file
def output_binary(file, x, y, pixels):
  # write headers
  file.write("P6\n".encode())
  file.write("# Roland Yang 3/18/24\n".encode())
  file.write("{} {}\n".format(x,y).encode())
  file.write("255\n".encode())
  # convert each pixel to binary
  pixels = b"".join([sub.to_bytes(1, "little") for sub in pixels])
  file.write(out)

def decryptA01(r,g,b):
  """ Sets all values to the red value multiplied by 10. """
  r = g = b = r*10
  return r,g,b

def decryptA02(r,g,b):
  r = 0
  g *= 20
  b *= 20
  return r,g,b

def decryptA03(r,g,b):
  """ Less branches. Multiplies by 16 unconditionally and only sets all to 255
      if it overflows a byte. """
  r = g = 0
  b *= 16
  if b > BYTE_MAX:
    r = g = b = BYTE_MAX
  return r,g,b

def decryptA04(r,g,b):
  """ Chinese remainder theorem. For all coprime numbers we just need to
    find integer multiples that add up to 1. For 3 and 17, 3(6) - 17
    (-1) = 1. Then, for any a % 3, b % 17, you will discover a*-17 +
     b*18 is congruent to both. """
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
  m = r*J + b*I
  r = g = b = (m*K + g*L) % BYTE_MAX
  return r,g,b

def decryptA05(r,g,b):
  """ Decrypts a pixel with data located in the 4 low bits. Shifts by 4 and
      masks by 255 very quickly instead of a contrived string manipulation """
  maskShift = lambda n : n << 4 & BYTE_MAX
  return maskShift(r), maskShift(g), maskShift(b)

def main():
  # input
  filename = input()
  algorithm_choice = int(input())
  file = open(filename, "r")
  width, height = read_dimensions(file)
  original_pixels = read_pixels(file)

  # process

  # just use the index you get
  # yet another comprehension (i'm allergic to indexing)
  pixels = []
  if algorithm_choice == 1:
    pixels = (decryptA01(*pixel) for pixel in original_pixels)
  elif algorithm_choice == 2:
    pixels = (decryptA02(*pixel) for pixel in original_pixels)
  elif algorithm_choice == 3:
    pixels = (decryptA03(*pixel) for pixel in original_pixels)
  elif algorithm_choice == 4:
    pixels = (decryptA04(*pixel) for pixel in original_pixels)
  elif algorithm_choice == 5:
    pixels = (decryptA05(*pixel) for pixel in original_pixels)

  # output
  # strip the extension
  filename = filename[:-4]
  outname = "{}_OutA0{}.ppm".format(filename, algorithm_choice)

  out = open(outname, "xb" if USE_GRAPHICS else "x")
  if USE_GRAPHICS:
    output_binary(out, width, height, pixels)

    # create the window!
    input_binary_name = "{}6.ppm".format(filename)
    input_binary = open(input_binary_name, "xb")
    output_binary(input_binary, width, height, original_pixels)
    input_binary.close()
    inputWin = GraphWin("INPUT", width, height)
    img = Image(Point(width//2, height//2), input_binary_name)
    img.draw(inputWin)
    win.getMouse()
    win.close()
  else:
    output_file(out, width, height, pixels)
  out.close()

  if USE_GRAPHICS:
    outputWin = GraphWin("OUTPUT", width, height)
    img = Image(Point(width//2, height//2), outname)
    img.draw(outputWin)
    win.getMouse()
    win.close()

  # terminate
  # lazy io!
  file.close()

if __name__ == "__main__":
  main()
