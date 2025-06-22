# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
if __name__ == "__main__":
    records = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = []
    for i in records:
        scores.append(i[1])

    scores = [score for _, score in records]
    unique_scores = sorted(set(scores))
    second_lowest = unique_scores[1]
    result = []

    result = sorted(name for name, score in records if score == second_lowest)

    for i in result:
        print(i)
