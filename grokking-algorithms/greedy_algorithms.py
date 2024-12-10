"""
Suppose you’re starting a radio show. You want to
reach listeners in all 50 states. You have to decide what
stations to play on to reach all those listeners. It costs
money to be on each station, so you’re trying to minimize the
number of stations you play on. You have a list of stations.

Each station covers a region, and
there’s overlap.
How do you figure out the smallest set of
stations you can play on to cover all 50
states? Sounds easy, doesn’t it? Turns out
it’s extremely hard. Here’s how to do it:

1. List every possible subset of stations.
This is called the power set. There are
2^n possible subsets.

2. From these, pick the set with the smallest number of stations that
covers all 50 states.
The problem is, it takes a long time to calculate every possible subset
of stations. It takes O(2^n) time, because there are 2^n stations. It’s
possible to do if you have a small set of 5 to 10 stations. But with all
the examples here, think about what will happen if you have a lot of
items. It takes much longer if you have more stations. Suppose you can
calculate 10 subsets per second.
There’s no algorithm that solves it fast enough! What can you do?

Approximation algorithms
Greedy algorithms to the rescue! Here’s a greedy algorithm that comes
pretty close:
1. Pick the station that covers the most states that haven’t been covered
yet. It’s OK if the station covers some states that have been covered
already.
2. Repeat until all the states are covered.
This is called an approximation algorithm. When calculating the exact
solution will take too much time, an approximation algorithm will
work. Approximation algorithms are judged by
• How fast they are
• How close they are to the optimal solution
Greedy algorithms are a good choice because not only are they simple
to come up with, but that simplicity means they usually run fast, too.
In this case, the greedy algorithm runs in O(n^2) time, where n is the
number of radio stations.
"""

# Code for setup
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])  #You pass an array in and it gets converted to a set.

# You also need the list of stations that you're choosing from. I chose to use a hash for this:
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

# Finally, you need something to hold the final set of stations you’ll use:
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
        
states_needed -= states_covered
final_stations.add(best_station)

print(final_stations)