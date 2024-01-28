# two string s, t, same length


def next(char1, char2):
    if char1 == "z" and char2 == "a":
        return True

    if ord(char1) + 1 == ord(char2):
        return True

    return False


def solution(s, t):
    for i in range(len(s)):
        if not next(s[i], t[i]):
            return False

    return True
