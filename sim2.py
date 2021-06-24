from itertools import permutations
from random import choice
from string import ascii_uppercase

field_size = int(input("How many candidates are running? "))

candidates = list(ascii_uppercase)[:field_size]
# print(candidates)

possibilities = list(permutations(candidates))
# print(possibilities)

turnout = int(input("How many voters are voting?: "))

ballots = []
count = 0

# Generate random ballots
while count < turnout:
    ballot = choice(possibilities)
    ballots.append(ballot)
    count += 1

ballots = [list(b) for b in ballots]

zeroes = [0]
zeroes *= field_size

d = dict(zip(candidates, zeroes))


def run_off(d, results, ballots):
    for key in d.keys():
        d[key] = 0
        first_choices = [b for b in ballots if b[0] == key]
        # if ballot[0] == key:
        d[key] += len(first_choices)

    results = sorted(d, key=lambda x: d[x], reverse=True)

    for i in results:
        print("Candidate", i, "received", d[i], "votes.")
    print("Total:", sum(d.values()))

    loser = results[-1]
    print("\nCandidate", loser, "got the least votes.\n")

    second_choices = [b for b in ballots if b[0] == loser]
    for second in second_choices:
        ballots.remove(second)
        ballots.append(second[1:])

    # print(results)

    del d[loser]

    run_off(d, results, ballots)

    return None


results = d.keys()
run_off(d, results, ballots)

# print(d)
# print(len([b for b in ballots if len(b) == 4]))

# if (d[results[0]] / turnout) > 0.5:
    # print("Candidate", results[0], "has won with a majority:", str(d[results[0]] * 100 / turnout), "%.")
