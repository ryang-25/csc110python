# Project title: Chess
# Roland Yang
# 2/20/24
# On my honor, I have neither given nor received unauthorized help on this
# assignment
# Chess assignment.

def sum(numbers):
  """ Sum a list. """
  acc = 0
  for n in numbers:
    acc += n
  return acc

def main():
  # process

  # use a Tamerlane's board
  squares = 8*8
  rice_squares = [2**n for n in range(0, squares)]
  total_rice = sum(rice_squares)

  # www.ncbi.nlm.nih.gov/pmc/articles/PMC6145214/
  # We use a grain of Batken rice, which has a volume of 21.13 mm^3
  grain_volume = 21.13e-3
  rice_volume = grain_volume * total_rice

  # Volume of the whole. Since 15% of the volume of a container of rice is void,
  # we multiply the whole by 1.15.
  total_volume = 1.15 * rice_volume

  # www2.census.gov/library/publications/decennial/2010/cph-2/cph-2-1.pdf
  # The total surface area of South Carolina, in square miles.
  # We convert to metric for easier maths, so m^2
  surface_area = 32_020.49 * 2.59 / 10e6

  depth = total_volume/surface_area

  # www.statista.com/statistics/255945/top-countries-of-destination-for-us-rice-exports-2011/
  # China produces 145.95 million metric tons of rice per year.
  year_metric_tons = 145.95e6

  # Mass of 1000 kernels in grams.
  thousand_kernel_weight = 24.37

  # Mass of the rice we would need to produce, in kilograms.
  # Convert to metric tons by multiplying by 1000.
  rice_weight = total_rice*thousand_kernel_weight*1000

  # Output
  print(f"The depth of rice that would cover the whole of South Carolina would be {depth:.2e} km.")
  print(f"China, the largest rice producing country, would take {rice_weight/year_metric_tons:.2e} years \
to produce the necessary rice.")

main()
