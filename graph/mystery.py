# mystery.py
# Roland Yang
# N/N/24
# On my honor I have neither given nor received unauthorized aid on this
# assignment

import re
import graphics
from graphics import *
# from graphics import GraphWin, Image, Point

# initialize

def read_comment(file):
  line = ""
  while len(line) == 0:
    line = file.readline().split("#")[0]
  return line

def read_dimensions(file):
  assert file.readline()[:-1] == "P3"
  dimensions = []
  while len(dimensions) < 2:
    line = read_comment(file)
    # this isn't entirely within spec since if the max pixel is on the same line we'll miss it
    # but i don't want to build a whole parser...
    dimensions = dimensions + [int(x) for x in re.findall(r"\d+", line)]
  return dimensions

def read_pixels(file):
  max_pixel = int(file.readline()) # unused!
  raw_pixels = [l for l in file.readlines() if len(l.split("#")[0]) != 0]
  lines = "".join(raw_pixels).split() # remove whitespace!
  for i in range(0, len(lines), 3):
    r = int(lines[i])
    g = int(lines[i+1])
    b = int(lines[i+2])
    yield (r,g,b)

def output_file(file, x, y, pixels):
  # write headers
  file.write("P3\n")
  file.write("# Roland Yang\n")
  # apparently the grader doesn't like f-strings!!
  file.write("{} {}\n".format(x,y))
  file.write("255\n")
  for pixel in pixels:
    file.write("{} {} {}\n".format(pixel[0], pixel[1], pixel[2]))

# output the binary
def output_binary(file, x, y, pixels):
  # write headers
  file.write("P6\n".encode())
  file.write("# Roland Yang\n".encode())
  # apparently the grader doesn't like f-strings!!
  file.write("{} {}\n".format(x,y).encode())
  file.write("255\n".encode())
  for pixel in pixels:
    order = "little"
    red = pixel[0].to_bytes(1, order)
    green = pixel[1].to_bytes(1, order)
    blue = pixel[2].to_bytes(1, order)
    out = red + green + blue
    file.write(out)

BYTE_MAX = 255

def print_in(x):
    """ Accept input and print out the input to the terminal with a newline. """
    ret = input(x)
    print(ret)
    return ret

def decryptA01(r,g,b):
  """ Sets all values to the red value multiplied by 10. """
  r = g = b = r*10
  return (r,g,b)
def decryptA02(r,g,b):
  r = 0
  g *= 20
  b *= 20
  return (r,g,b)
def decryptA03(r,g,b):
  """ Less branches. Multiplies by 16 unconditionally and only sets all to 255
      if it overflows a byte. """
  b *= 16
  if b > BYTE_MAX:
    r = g = b = BYTE_MAX
  return (r,g,b)
def decryptA04(r,g,b):
  """ Chinese remainder theorem. For all coprime numbers we just need to find
      integer multiples that add up to 1. For 3 and 17, 3(6) - 17(-1) = 1. Then,
      for any a % 3, b % 17, you will discover a*-17 + b*18 is congruent to
      both. """
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
  return (r,g,b)
def decryptA05(r,g,b):
  """ Decrypts a pixel with data located in the 4 low bits. Shifts by 4 and
      masks by 255 very quickly instead of a contrived string manipulation """
  maskShift = lambda n : n << 4 & BYTE_MAX
  return (maskShift(r), maskShift(g), maskShift(b))

def main():
  # input
  # filename = input()
  # algorithm_choice = int(input())
  # file = open(filename, "r")
  # dimensions = read_dimensions(file)
  # pixels = read_pixels(file)

  # # compute

  # # why use an if statement if you have first class functions?
  # # just use the index you get
  # algorithms = [decryptA01, decryptA02, decryptA03, decryptA04, decryptA05]
  # algorithm = algorithms[algorithm_choice-1]
  # # yet another comprehension (i'm allergic to indexing)
  # pixels = (algorithm(*pixel) for pixel in pixels)

  # # output
  # # strip the extension
  # filename = filename[:-4]
  # outname = "{}_OutA0{}.ppm".format(filename, algorithm_choice)
  #out = open(outname, "x")
  #out = open(outname, "xb")
  #output_file(out, dimensions[0], dimensions[1], pixels)
  #output_binary(out, dimensions[0], dimensions[1], pixels)
  win = GraphWin("hi", 800, 450)
  c = Image(Point(5,5), "mystery1_OutA01.ppm")
  c.draw(win)
  win.getMouse()

  # lazy io!
  file.close()
  out.close()

main()
