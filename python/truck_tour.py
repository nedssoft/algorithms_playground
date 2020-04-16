"""
Suppose there is a circle. There are N petrol pumps on that circle. Petrol pumps are numbered 0 to (N-1) (both inclusive).
 You have two pieces of information corresponding to each of the petrol pump: 
 (1) the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the next petrol pump.

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps.
 Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps.
  The truck will move one kilometer for each litre of the petrol.

Input Format

The first line will contain the value of .
The next  lines will contain a pair of integers each, 
i.e. the amount of petrol that petrol pump will give and the distance between that petrol pump and the next petrol pump.

Constraints:


Output Format

An integer which will be the smallest index of the petrol pump from which we can start the tour.
"""

from queue import Queue


def truckTour(petrolpumps):
    route = Queue()

    # add all pumps to the queue
    for p in petrolpumps:
        route.put(p)

    # keeps track of the pump we start at
    start = 0
    # keeps track of the number of pumps we've traversed
    passed = 0
    # amount of gas we currently have
    gas = 0

    while passed < len(petrolpumps):
        # get the next pump along the route
        pump = route.get()  # dequeue
        # add the amount of gas this pump has
        gas += pump[0]
        # check if our gas tank has enough to get us to the next pump
        if gas >= pump[1]:
            passed += 1
            gas -= pump[1]
        else:
            # if it doesn't, reset our gas tank, the number of pumps
            # we've passed, and move on to consider the next pump
            # as the starting point
            start += passed + 1
            passed = 0
            gas = 0
        # add the pump to the back of the route
        route.put(pump)

    return start


pumps = [
    [1, 5],
    [10, 3],
    [3, 4]
]

print(truckTour(pumps))
