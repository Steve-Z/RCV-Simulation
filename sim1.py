from itertools import permutations
from random import choice
from string import ascii_uppercase

candidates = list(ascii_uppercase)[:5]
# print(candidates)

possibilities = list(permutations(candidates))
# print(possibilities)

turnout = input("How many voters are voting?: ")
turnout = int(turnout)

ballots = []
count = 0

# Generate random ballots
while count < turnout:
    ballot = choice(possibilities)
    ballots.append(ballot)
    count += 1

# print(ballots)
ballots = [list(b) for b in ballots]

zeroes = [0, 0, 0, 0, 0]

d = dict(zip(candidates, zeroes))
# print(d)

# Round 1
for key in d.keys():
    for ballot in ballots:
        if ballot[0] == key:
            d[key] += 1

results = sorted(d, key=lambda x: d[x], reverse=True)

for i in results:
    print("Candidate", i, "received", d[i], "votes.")
print("Total:", sum(d.values()))


def runoff(d, results):
    # Allocate 2nd choices for last place candidate
    if (d[results[0]] / turnout) <= 0.5:
        loser = results[-1]
        print("\nCandidate", loser, "got the least votes.\n")

        for ballot in [b for b in ballots if b[0] == loser]:
            if ballot[1] in d.keys():
                d[ballot[1]] += 1

        del d[loser]

        results = sorted(d, key=lambda x: d[x], reverse=True)

        for i in results:
            print("Candidate", i, "received", d[i], "votes.")
        print("Total:", sum(d.values()))

        runoff(d, results)

    else:
        print(
            "Candidate",
            results[0],
            "has won with a majority:",
            str(d[results[0]] * 100 / turnout),
            "%.")

    return None


runoff(d, results)
