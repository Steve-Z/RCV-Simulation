from itertools import permutations
from random import choices
from string import ascii_uppercase
from collections import Counter


class RCV:

    def ballots(
        self,
        fieldsize=5,
        ranksize=5,
        turnout=10000
    ):
        """Randomly generate ballots

        Keyword arguments:
        fieldsize -- How many candidates are running (default 5)
        ranksize -- How many candidates can be ranked (default 5)
        turnout -- How many ballots are being cast (default 1000)

        Adds 1 unranked single-choice ballot for each candidate.
        Length of ballot list will be turnout + fieldsize.
        """
        if not (turnout + fieldsize) % 2:
            turnout += 1

        candidates = list(ascii_uppercase)[:fieldsize]

        possibilities = list(permutations(candidates, ranksize))

        # Generate random ballots
        ballots = list(choices(possibilities, k=turnout))

        ballots = [list(b) for b in ballots]

        # Test single choice, i.e., not fully ranked ballots
        singles = [list(c) for c in candidates]
        ballots = ballots + singles

        return ballots

    def count(self, ballots):
        """Counts first round votes.

        Returns dictionary of results, first and last place candidates.
        """
        first_choices = [b[0] for b in ballots]
        c = Counter(first_choices)
        d = dict(c.most_common())
        first = list(d)[0]
        last = list(d)[-1]
        return d, first, last

    def runoff(
        self,
        first=None,
        last=None,
        rnd=1,
        d=None,
        ballots=None,
        threshold=None,
    ):
        """Allocate 2nd choices for last place candidate.

        Runs recursively until there is a majority winner.
        """
        if not threshold:
            threshold = len(ballots) * 0.5
        if d[first] <= threshold:
            print("\nCandidate", last, "got the least votes.\n")
            print("\nROUND", rnd, "\n")

            rnd += 1

            losers = [b for b in ballots if b[0] == last]

            for ballot in losers:
                ballots.remove(ballot)
                i = 0
                while i < len(ballot) > 1:
                    i += 1
                    try:
                        d[ballot[i]] += 1
                        ballots.append(ballot[i:])
                        break
                    except Exception:
                        continue

            del d[last]

            # Need a new variable 'e'; re-declaring 'd' causes bug.
            e = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
            first = list(e)[0]
            last = list(e)[-1]

            for k, v in e.items():
                print("Candidate", k, "received", v, "votes.")
            print("Total:", sum(e.values()))

            if len(d.keys()) > 2:
                self.runoff(
                    first=first,
                    last=last,
                    rnd=rnd,
                    d=d,
                    ballots=ballots,
                    threshold=threshold
                )

            else:
                print(
                    "Candidate",
                    first,
                    "has won with a majority:",
                    str(d[first] * 100 / len(ballots)),
                    "%.\n")

        return d
