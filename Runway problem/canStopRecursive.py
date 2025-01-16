def CanstopRecursive(runway, initSpeed, startIndex=0):
    # NEGATIVE BASE CASES NEED TO GO FIRST
    if (
        startIndex >= len(runway)
        or startIndex < 0
        or initSpeed < 0
        or not runway[startIndex]
    ):
        return False
    # BASE CASE FOR  A STOPPING CONDITION
    if initSpeed == 0:
        return True
    # TRY ALL POSSIBLE PATHS
    for adjustedSpeed in [initSpeed - 1, initSpeed, initSpeed + 1]:
        # RECURRENCE RELATION: IF YOU CAN STOP FROM ANY OF THE SUBPROBLEMS
        # YOU CAN STOP FROM THE MAIN PROBLEM
        if CanstopRecursive(runway, adjustedSpeed, startIndex + adjustedSpeed):
            return True
    return False
