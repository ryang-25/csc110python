# bpp.py
# Roland Yang
# 3/8/24
# file i was not paying attention in class
# On my honor I have neither given nor received unauthorized aid on this
# assignment

import re

def read_comment(file):
  line = "#"
  while len(line) and line[0] != "#":
    line = file.readline()
  return line

def read_dimensions(file):
  assert(file.readline()[:-1] == "P3")
  line = read_comment(file)
  return [int(x) for x in re.findall(r"\d+", line)]

def read_pixels(file):
  max_pixel = int(file.readline()) # unused!
  pixels = []
  raw_pixels = [l for l in file.readlines() if l[0] != "#"]
  lines = "".join(raw_pixels).split() # remove whitespace!
  for i in range(0, len(lines), 3):
    r = int(lines[i])
    g = int(lines[i+1])
    b = int(lines[i+2])
    pixels.append([r,g,b])
  return pixels

def is_green(pixel):
  red_distance = pixel[1] - pixel[0]
  blue_distance = pixel[1] - pixel[2]
  out = False
  # if green is greater than red and blue by 20 we assume it to be green.
  if red_distance >= 20 and blue_distance >= 20:
    out = True
  return out

def output_file(file, x, y, pixels):
  # write headers
  file.write("P3\n")
  file.write("# Roland Yang\n")
  file.write(f"{x} {y}\n")
  file.write("255\n")
  for pixel in pixels:
    file.write(f"{pixel[0]} {pixel[1]} {pixel[2]}\n")

def main():
  DINO = "dino2s800x531.ppm"
  dino = open(DINO, "r")
  GSSM = "scgssm800x531.ppm"
  gssm = open(GSSM, "r")

  dimensions = read_dimensions(dino)
  assert dimensions == read_dimensions(gssm)
  gssms = read_pixels(gssm)
  dinos = read_pixels(dino)
  for i in range(len(dinos)):
    if is_green(dinos[i]):
      dinos[i] = gssms[i]

  OUT = input("output file name: ")
  out = open(OUT, "a")
  output_file(out, dimensions[0], dimensions[1], dinos)

  dino.close()
  gssm.close()
  out.close()

main()
