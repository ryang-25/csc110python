import asciibars


def wasted(dems, gops):
    # simple majority requires average + 1 vote.
    average = floor((dems + gops) / 2) + 1
    calc_waste = lambda n : n if n - average < 0 else n - average
    return calc_waste(dems), calc_waste(gops)

def efficiency_gap(dems_waste, gops_waste, total_votes):
    gap = 100 * abs(dems_waste - gops_waste) / total_votes
    win = "Democrats"
    if gops_waste < dems_waste:
        win = "Republicans"
    return win, gap

def vote_chunks(ls):
    """ Since we don't need the district name... """
    out = []
    for i in range(0, len(ls), 3):
        out.append(ls[i+1:i+3])
    return out


def parse(input_str, target_state):
    """ Parser. """
    lines = input_str.splitlines()
    uncons = lambda ls : ls[0], ls[1:]
    states = [uncons(line.split(",")) for line in lines]
    districts = None
    i = 0
    while districts != None and i < len(states):
        cur_state, cur_districts = states[i]
        if cur_state.lower() == target_state:
            districts = chunks(cur_districts)
    return districts


def main():

    districts = open("districts.txt", "r")

    ds = parse(input_str, target)
    ws = [wasted(*d) for d in ds]

    eligible = open("eligible_voters.txt", "r")
    if len(districts) < 3:
        print("There are an insufficient number of districts to calculate an Efficiency Gap.")

    pass

if __name__ == '__main__':
    main()