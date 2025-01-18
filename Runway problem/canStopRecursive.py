def CanstopRecursive(runway, initSpeed, startIndex=0):
    if not check_input(runway, initSpeed, startIndex):
        return False
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
