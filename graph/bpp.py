def read_dimensions(file):


  
  while True:
    file.readline()


def read_until(file, n):
  for _ in range(0, n-1):
    file.readline()
  return file.readline()

def main():
  #minion = "minion.ppm"
  minion = input("hi")
  file = open(minion, "r+")
  # data = file.read()
  print(read_until(file, 3))

main()
