def canStopIterative(runway, initSpeed, startIndex=0):
    # maximum speed cannot be larger than length of the runway. We will talk about
    # making this bound tighter later on.
    maxSpeed = len(runway)
    if (
        startIndex >= len(runway)
        or startIndex < 0
        or initSpeed < 0
        or initSpeed > maxSpeed
        or not runway[startIndex]
    ):
        return False
    # {position i : set of speeds for which we can stop from position i}
    memo = {}
    # Base cases, we can stop when a position is not a spike and speed is zero.
    for position in range(len(runway)):
        if runway[position]:
            memo[position] = set([0])
    # Outer loop to go over positions from the last one to the first one
    for position in reversed(range(len(runway))):
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
