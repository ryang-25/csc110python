# Project title: Chess
# Roland Yang
# 2/22/24
# On my honor, I have neither given nor received unauthorized help on this
# assignment
# Chess assignment.

def print_in(prompt):
    """ Accept input and print out the input to the terminal with a newline. """
    ret = input(prompt)
    print(ret)
    return float(ret)

def sum_squares(n):
  """ Calculate a power of two by accumulator. """
  acc = 0
  for i in range(0, n):
    acc += 2**i
  return acc

def main():
  print("THE CHESSBOARD PROBLEM")

  # input
  squares = int(print_in("What is the number of squares on the gameboard?"))
  volume = print_in("What is the volume of a single grain of rice (in cubic mm)?")
  mass = print_in("What is the mass of a single grain of rice (in mg)?")
  packing = print_in("What is the fraction of air gaps (%age of voids)?")
  area = print_in("What is the total surface area of South Carolina (in square miles)?")

  # process
  rice = sum_squares(squares)
  # Convert from mm (10^-3) to meters by multiplying by (10^-3)^3. Round to 2 digits.
  rice_volume = round(rice * volume * 1e-9, 2)
  total_volume = round(rice_volume / (1 - packing), 2)

  # Conversions to feet.
  # meters cubed to feet cubed.
  rice_volume *= 35.315
  total_volume *= 35.315

  # Convert the area to square feet.
  area *= 27878400

  # divide by area.
  rice_depth = rice_volume / area
  total_depth = total_volume / area





  # Output
  print()
  print("RESULTS")
  print(f"The total number of grains of rice for a gameboard of {squares} squares is {rice} grains.")
  print(f"The total volume of rice is {rice_volume} cubic meters (compacted)")
  print(f"The total volume of rice is {total_volume} cubic meters (with air gaps).")
  print(f"The total depth of rice over the state of South Carolina is {rice_depth} feet (compacted)")
  print(f"The total depth of rice over the state of South Carolina is {total_depth} feet (with air gaps)")
  print(f"The total number of metric tons (mtu) requested is {area} tonnes.")

main()
