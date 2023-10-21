from ast import List
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # available current courses
        current_courses = set([x[1] for x in relations])

        # available previous courses
        previous_courses = set(x[0] for x in relations)

        # root courses = courses not in previous_courses + courses without prerequisites (stand alone courses)
        roots = [x for x in current_courses if x not in previous_courses] + [
            x
            for x in range(1, n + 1)
            if x not in current_courses and x not in previous_courses
        ]

        # course graph: cause: pre-requisites
        graph = defaultdict(list)

        # create graph
        for relation in relations:
            graph[relation[1]].append(relation[0])

        costs_memo = defaultdict(int)

        def max_cost(courses):
            same_level_costs = []
            for course in courses:
                # if the cost is already calculated, use the recorded cost
                if course in costs_memo:
                    same_level_costs.append(costs_memo[course])
                # cost not in costs_memo (no results yet)
                elif course in graph:
                    costs_memo[course] = time[course - 1] + max_cost(graph[course])
                    same_level_costs.append(costs_memo[course])
                # course not in graph
                else:
                    costs_memo[course] = time[course - 1]
                    same_level_costs.append(costs_memo[course])

            return max(same_level_costs)

        return max_cost(roots)
