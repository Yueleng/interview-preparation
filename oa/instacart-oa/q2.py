def solution(stationsA, stationsB, stationsC, origin, destination):
    A = 0
    if origin in stationsA:
        A += 1

    if destination in stationsA:
        A += 1

    B = 0
    if origin in stationsB:
        B += 1
    if destination in stationsB:
        B += 1

    C = 0
    if origin in stationsC:
        C += 1
    if destination in stationsC:
        C += 1

    if A == 2 or B == 2 or (A == 1 and B == 1):
        return "AB"

    if C == 2 or (B == 1 and C == 1):
        return "BC"

    if A == 1 and C == 1:
        return "ABC"

    return "NO"
