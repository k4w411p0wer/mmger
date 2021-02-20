class Jumps(dict):
    def __missing__(self, key):
        self[key] = []
        return self[key]


def solution(filename):
    with open(filename) as file:
        _, d = map(int, file.readline().split())
        jumps = Jumps()
        for line in file:
            athletes_number, *attempts = map(int, line.split())
            jumps[athletes_number].append(max(attempts))
    best_average = []
    for attempts in jumps.values():
        if len(attempts) > d:
            best_average.append(sum(attempts)/len(attempts))
    print(round(max(best_average) - min(best_average), 2))


# solution('27-in.txt')
solution('27-A.txt')
solution('27-B.txt')
