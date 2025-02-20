def canStopRecursiveWithMemo(runway, initSpeed, startIndex=0, memo=None):
    if not check_input(runway, initSpeed, startIndex):
        return False
    # Only done the first time to initialize the memo
    if memo == None:
        memo = {}
    # First check if we have already result in memo
    if startIndex in memo and initSpeed in memo[startIndex]:
        return memo[startIndex][initSpeed]
    # NEGATIVE BASE CASES NEED TO GO FIRST
    negative_conditions = (
        startIndex >= len(runway)
        or startIndex < 0
        or initSpeed < 0
        or initSpeed > maxSpeed
        or not runway[startIndex]
    )
    if negative_conditions:
        InsertIntoMemo(memo, startIndex, initSpeed, False)
        return False
    # BASE CASE FOR  A STOPPING CONDITION
    if initSpeed == 0:
        InsertIntoMemo(memo, startIndex, initSpeed, True)
        return True
    # Try all possible paths
    for adjustedSpeed in [initSpeed - 1, initSpeed, initSpeed + 1]:
        # Recurrence relation: if you can stop from any of the subproblems
        # you can stop from the main problem
        if canStopRecursiveWithMemo(
            runway, adjustedSpeed, startIndex + adjustedSpeed, memo
        ):
            InsertIntoMemo(memo, startIndex, initSpeed, True)
            return True
    InsertIntoMemo(memo, startIndex, initSpeed, False)
    return False


def InsertIntoMemo(memo, startIndex, initSpeed, result):
    if startIndex not in memo:
        memo[startIndex] = {}
    memo[startIndex][initSpeed] = result


def check_input(runway, initSpeed, startIndex):
    if not isinstance(runway, list) or runway == None or runway == []:
        return False
    for i in runway:
        if not isinstance(i, bool):
            return False
    if not isinstance(initSpeed, int) or not isinstance(startIndex, int):
        return False
    return True
