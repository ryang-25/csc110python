"""
gerrymandering.py
Roland Yang
5/19/24
On my honor I have neither given nor received unauthorized aid on this
assignment
"""

# whether or not to use graphics.py
USE_GRAPHICS = False
if USE_GRAPHICS:
  from graphics import GraphWin, Image, Line, Point, Rectangle, Text

from math import floor
from asciibars import plot

WIDTH = 500
HEIGHT = 500
LGAP = 72
RGAP = 49
# threshold
EGAPTHRESH = 7

def wasted(dems, gops):
    """
    Calculate wasted votes for a district of democrats and republicans.
    """
    avg = floor(1 + (dems+gops)/2)
    # the waste for the winner is any above the average, but all for the loser
    waste = lambda n : n if n - avg < 0 else n - avg
    return waste(dems), waste(gops)

def read_data(file, state):
    """
    Read the districts associated with a state.
    """
    split = lambda : file.readline().split(",")
    line = split()
    # The first element is the state name.
    while line[0] != state and line != [""]:
        line = split()
    if line == [""]:
        line = None
    return line

def parse(districts):
    """
    Parse the districts.
    """
    data = []
    d_waste = r_waste = 0
    for i in range(0, len(districts), 3):
        # parties
        pts = int(districts[i+1]), int(districts[i+2])
        # We only need the democratic percentage of votes and district name
        tot = pts[0]+pts[1]
        # avoid div by 0, say they're both 50%
        per = 50 if tot == 0 else int(100*pts[0]/tot)
        data.append((districts[i], per))
        # and then we need the wasted votes.
        dw, rw = wasted(*pts)
        d_waste += dw
        r_waste += rw

    return data, d_waste, r_waste

def draw_window(state, total, percentages):
    """
    Draw graphics window.
    """
    win = GraphWin("gerrymandering", WIDTH, HEIGHT)
    win.setBackground("white")

    state_t = Text(Point(len(state)*4,10), state)
    voters = str(total) + " eligible voters"
    voters_t = Text(Point(WIDTH-len(voters)*3.7, 10), voters)

    state_t.draw(win)
    voters_t.draw(win)

    dash = Line(Point(0, 20), Point(WIDTH, 20))
    dash.draw(win)

    bar = Line(Point(WIDTH/2, 0), Point(WIDTH/2, HEIGHT))
    bar.draw(win)

    # starting y coordinate
    y = 25
    for percent in percentages:
        x = int(percent*WIDTH/100)
        r1 = Rectangle(Point(0, y), Point(x, y+20))
        r1.setFill("blue")
        r1.draw(win)
        r2 = Rectangle(Point(x, y), Point(WIDTH, y+20))
        r2.setFill("red")
        r2.draw(win)
        y += 25

    win.getKey()
    win.close()


def main():
    # Initialize
    print("This program allows you to search through data about congressional voting districts")
    print("and determine whether a particular state is gerrymandered.\n")

    # Input

    state = input("Which state do you want to look up? ")
    print(state)
    # title case to fix erroneous imnput

    districts = open("districts.txt", "r")
    ds = read_data(districts, state.title())

    # handle missing.
    if ds == None:
        print('"{}" not found.'.format(state))
        districts.close()
        exit()

    state = state.title()
    data, d_waste, r_waste = parse(ds[1:])

    eligible = open("eligible_voters.txt", "r")
    total = int(read_data(eligible, state)[1])

    # Recycle fds early

    districts.close()
    eligible.close()

    print("Total Wasted Democratic votes:", d_waste)
    print("Total Wasted Republican votes:", r_waste)
    print(total, "elgible voters")
    district_count = len(data)
    if district_count >= 3:
        # round to one decimal place
        gap = round(100 * abs(d_waste - r_waste)/total, 1)
        favor = "Democrats" if d_waste < r_waste else "Republicans"
        print("The Efficiency Gap is {}% in favor of the {}.".format(gap, favor))
        if gap >= EGAPTHRESH:
            print("The State does appear to be gerrymandered.")
        else:
            print("The State does not appear to be gerrymandered.")
    else:
        print("There are an insufficient number of districts to calculate an Efficiency Gap.")
        print("This State has", district_count, "districts. ",
            "States with less than three districts cannot be gerrymandered.")

    print()
    print("{:72}||{:>33} eligible voters".format(state, total))
    print("="*LGAP+"++"+"="*RGAP)

    data = [("District "+name, percent) for name, percent in data]
    plot(data, max_length=100, neg_max=100, unit='d', neg_unit='r',sep_lc=' \w D = ',count_pf='%')

    if USE_GRAPHICS:
        draw_window(state, total, [percent for _, percent in data])

if __name__ == '__main__':
    main()