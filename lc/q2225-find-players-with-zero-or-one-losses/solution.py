from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss = {}

        for match in matches:
            winner = match[0]
            loser = match[1]

            if winner not in loss:
                loss[winner] = 0

            if loser not in loss:
                loss[loser] = 1
            else:
                loss[loser] += 1

        players = []
        for player in loss:
            players.append(player)

        players.sort()

        answer = [[], []]
        for player in players:
            if loss[player] == 0:
                answer[0].append(player)
            elif loss[player] == 1:
                answer[1].append(player)

        return answer
