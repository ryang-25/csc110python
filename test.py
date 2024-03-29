from math import cos, radians, sin

def calculate_coordinates(length_a, length_b, angle):
  rads = radians(angle)
  x1, y1 = -(length_a + length_b*cos(rads))/3, -length_b*sin(rads)/3

#  x1, y1 = (length_b*(sin(rads) - cos(rads)) - length_a)/3, 0
  x2, y2 = x1 + length_a, y1
  x3, y3 = x1 + length_b*cos(rads), y1 + length_b*sin(rads)
  return [(x1,y1), (x2,y2), (x3,y3)]

print(calculate_coordinates(3,4,45))
