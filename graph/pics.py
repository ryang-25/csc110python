from graphics import *


def test():
  win = GraphWin("My Circle", 100, 100)
  c = Circle(Point(50,50), 10)
  c.draw(win)
  win.getMouse() # pause for click in window
  win.close()

def main():
  print("hi")
  test()

main()
