def canStopRecursiveWithMemo(runway, initSpeed, startIndex=0, memo=None):
    # Only done the first time to initialize the memo
    if memo == None:
        memo = {}
    # First check if we have already result in memo
    if startIndex in memo and initSpeed in memo[startIndex]:
        return memo[startIndex][initSpeed]
    # NEGATIVE BASE CASES NEED TO GO FIRST
    if (
        startIndex >= len(runway)
        or startIndex < 0
        or initSpeed < 0
        or not runway[startIndex]
    ):
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


runway = [True, False, True, True, False]
initSpeed = 2
startIndex = 0
print(canStopRecursiveWithMemo(runway, initSpeed, startIndex))
