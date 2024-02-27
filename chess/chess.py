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
    return int(ret)


def sum(numbers):
  """ Sum a list. """
  acc = 0
  for n in numbers:
    acc += n
  return acc

def main():
  # process

  squares = print_in("What is the number of squares on the gameboard?")
  rice_squares = [2**n for n in range(0, squares)]
  total_rice = sum(rice_squares)

  grain_volume = 21.13e-3
  # Convert to m^3.
  grain_volume = print_in("What is the volume of a single grain of rice (in cubic mm)?") * 1e-9
  rice_volume = grain_volume * total_rice

  # Volume of the whole. Divide by the packing fraction to find the total volume.
  packing_faction = print_in("what is the packing fraction?")
  total_volume = rice_volume / packing_faction

  # www2.census.gov/library/publications/decennial/2010/cph-2/cph-2-1.pdf
  # The total surface area of South Carolina, in square miles.
  # We convert to metric for easier maths, so m^2
  surface_area = print_in("What is the total surface area of South Carolina (in square miles)?") * 2.59e6

  # Depth in ft.
  depth = total_volume * 3.28 / surface_area

  # www.statista.com/statistics/255945/top-countries-of-destination-for-us-rice-exports-2011/
  # China produces 145.95 million metric tons of rice per year.
  year_metric_tons = 145.95e6

  # Mass of 1000 kernels in grams.
  thousand_kernel_weight = 24.37

  # Mass of the rice we would need to produce, in kilograms.
  # Convert to metric tons by multiplying by 1000.
  rice_weight = total_rice*thousand_kernel_weight*1000

  # Output
  print(f"The total number of grains of rice for a gameboard of {squares} many squares is {total_rice}.")
  print(f"The total volume of rice is {total_volume} cubic meters.")
  print(f"The total depth of rice over the state of South Carolina is {depth} feet.")
  print(f"The total number of metric tonnes requested is {rice_weight} tonnes.")

main()
