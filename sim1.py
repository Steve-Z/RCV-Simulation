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

print("ROUND 1\n")
for i in results:
    print("Candidate", i, "received", d[i], "votes.")
print("Total:", sum(d.values()))


def runoff(d, results, round):
    # Allocate 2nd choices for last place candidate
    if (d[results[0]] / turnout) <= 0.5:
        loser = results[-1]
        print("\nCandidate", loser, "got the least votes.\n")

        round += 1
        count = 1
        losers = [b for b in ballots if b[0] == loser]
        # print(len(losers), 'losers\n')
        # print(*losers, sep='\n')
        print("\nROUND", round, "\n")
        for ballot in losers:
            i = 1
            while True:
                # print("Ballot", count, "\n", ballot)
                try:
                    d[ballot[i]] += 1
                    # print(ballot[i])
                    ballots.append(ballot[i:])
                    ballots.remove(ballot)
                    # print("Replacing", ballot, "with", ballot[i:])
                    break
                except Exception:  # as e:
                    # print(f'Error: {e}')
                    i += 1
                    continue
            count += 1

        del d[loser]

        results = sorted(d, key=lambda x: d[x], reverse=True)

        for i in results:
            print("Candidate", i, "received", d[i], "votes.")
        print("Total:", sum(d.values()))

        if len(results) > 1:
            runoff(d, results, round)

    else:
        print(
            "Candidate",
            results[0],
            "has won with a majority:",
            str(d[results[0]] * 100 / turnout),
            "%.")

    return None


runoff(d, results, 1)
