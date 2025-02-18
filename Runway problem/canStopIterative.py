def canStopIterative(runway, initSpeed, startIndex=0):
    if not check_input(runway, initSpeed, startIndex):
        return False
    # maximum speed cannot be larger than length of the runway. We will talk about
    # making this bound tighter later on.
    maxSpeed = len(runway)
    negative_conditions = (
        startIndex >= len(runway)
        or startIndex < 0
        or initSpeed < 0
        or initSpeed > maxSpeed
        or not runway[startIndex]
    )
    if negative_conditions:
        return False
    # {position i : set of speeds for which we can stop from position i}
    memo = {}
    # Base cases, we can stop when a position is not a spike and speed is zero.
    length = len(runway)
    for position in range(length):
        if runway[position]:
            memo[position] = set([0])
    # Outer loop to go over positions from the last one to the first one
    for position in reversed(range(length)):
        # Skip positions which contain spikes
        if not runway[position]:
            continue
        # For each position, go over all possible speeds
        for speed in range(1, maxSpeed + 1):
            # Recurrence relation is the same as in the recursive version.
            for adjustedSpeed in [speed, speed - 1, speed + 1]:
                if (
                    position + adjustedSpeed in memo
                    and adjustedSpeed in memo[position + adjustedSpeed]
                ):  # Duplicate line
                    memo[position].add(speed)
                    break
    return initSpeed in memo[startIndex]


def check_input(runway, initSpeed, startIndex):
    if not isinstance(runway, list) or runway == None or runway == []:
        return False
    for i in runway:
        if not isinstance(i, bool):
            return False
    if initSpeed is None or not isinstance(initSpeed, int):
        return False
    if startIndex is None or not isinstance(startIndex, int):
        return False
    return True
