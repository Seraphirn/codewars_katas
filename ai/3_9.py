# Задание 3.9 из книги Искусственный интеллектю Современный подход.
# Стюард Рассел, Питер Норвиг
from dataclasses import dataclass
from typing import Callable, List, Optional

from time import sleep

import logging
logging.basicConfig(format='"%(asctime)s:%(levelname)s:%(name)s:%(message)s"',
                    level=logging.INFO)
LOG = logging.getLogger('39')


@dataclass
class Coast:
    missionaries: int = 0
    kannibals: int = 0
    boats: int = 0

    def __add__(self, other: object):
        return Coast(
            missionaries=self.missionaries+other.missionaries,
            kannibals=self.kannibals+other.kannibals,
            boats=self.boats+other.boats,
        )

    def __sub__(self, other: object):
        return Coast(
            missionaries=self.missionaries-other.missionaries,
            kannibals=self.kannibals-other.kannibals,
            boats=self.boats-other.boats,
        )

    def __neg__(self):
        return Coast(
            missionaries=-self.missionaries,
            kannibals=-self.kannibals,
            boats=-self.boats,
        )


@dataclass
class State:
    left: Coast
    right: Coast


@dataclass
class Action:
    direction: int  # 1 sail from right to left, -1 sail from left to right
    payload: State  # what to sail

    @property
    def diff(self):
        return Coast(
            missionaries=self.payload.missionaries*self.direction,
            kannibals=self.payload.kannibals*self.direction,
            boats=self.payload.boats*self.direction,
        )


@dataclass
class Sucessor:
    action: Action  # action to do
    state: State  # result state


@dataclass
class Problem:
    initial_state: State
    goalFunction: Callable[[State], bool]
    sucessorFunction: Callable[[State], List[Sucessor]]


@dataclass
class Solution:
    actions: list
    depth: int
    path_cost: int


@dataclass
class Node:
    state: Coast
    parent_node: Optional[object]  # object is Node
    action: Optional[Action]
    path_cost: int
    depth: int

    def getSolution(self) -> Solution:
        actions = []
        node = self
        while node is not None:
            actions.append(node.action)
            node = node.parent_node

        return Solution(path_cost=self.path_cost,
                        depth=self.depth,
                        actions=list(reversed(actions)))


class MissionariesAliveProblem(Problem):
    """
        Задача переправки n мессионеров и m канибалов с одного берега на другой

        Условая задачи: лодка может перевести одного или двух человек.
        Нельзя допустить, чтобы был съеден хотя бы одни мессионер. Если группа
        канибалов на одном береге превосходит по числеднности группу
        мессионеров, то они их убивают и едят.

    """
    def __init__(self, kannibals: int = 3, missionaries: int = 3):
        self.state_space = []
        self.kannibals = kannibals
        self.missionaries = missionaries

        self.initial_state = State(
            left=Coast(missionaries=missionaries, kannibals=kannibals,
                       boats=1),
            right=Coast(missionaries=0, kannibals=0)
        )

        # 0..KANNIBALS_COUNT
        for k_in_left in range(kannibals + 1):
            # 0..MISSIONARIES_COUNT
            for m_in_left in range(missionaries + 1):
                k_in_right = kannibals - k_in_left
                m_in_right = missionaries - m_in_left
                if (m_in_right >= k_in_right or m_in_right == 0) \
                        and (m_in_left >= k_in_left or m_in_left == 0):
                    self.state_space.append(
                        State(
                            left=Coast(missionaries=m_in_left,
                                       kannibals=k_in_left,
                                       boats=1),
                            right=Coast(missionaries=m_in_right,
                                        kannibals=k_in_right,
                                        boats=0)
                        )
                    )
                    self.state_space.append(
                        State(
                            left=Coast(missionaries=m_in_left,
                                       kannibals=k_in_left,
                                       boats=0),
                            right=Coast(missionaries=m_in_right,
                                        kannibals=k_in_right,
                                        boats=1)
                        )
                    )

    def isGoalReachedForState(self, state: State) -> bool:
        return (state.left.missionaries == 0
                and state.left.kannibals == 0
                and state.right.missionaries == 3
                and state.right.kannibals == 3)

    def sucessorFunction(self, state: State) -> List[Sucessor]:
        direction = 1 if state.right.boats == 1 else -1

        actions = [
            Action(direction=direction, payload=Coast(missionaries=2,
                                                      boats=1)),
            Action(direction=direction, payload=Coast(missionaries=1,
                                                      kannibals=1, boats=1)),
            Action(direction=direction, payload=Coast(kannibals=2, boats=1)),
            Action(direction=direction, payload=Coast(kannibals=1, boats=1)),
            Action(direction=direction, payload=Coast(missionaries=1,
                                                      boats=1)),
        ]

        possible_sucessors = [
            Sucessor(
                action=a,
                state=State(
                   left=state.left + a.diff,
                   right=state.right - a.diff,
                )
            )
            for a in actions
        ]
        return [
            s for s in possible_sucessors if s.state in self.state_space
        ]


class TreeSearch():
    def __init__(self, problem: Problem, fringe: list = []):
        self.problem = problem
        self.fringe = fringe

    def getSolution(self) -> Solution:
        self.fringe.append(
            Node(
                state=self.problem.initial_state,
                parent_node=None,
                action=None,
                path_cost=0,
                depth=0
            )
        )
        while True:
            if not self.fringe:
                raise Exception('No solution')
            node = self.fringe.pop(0)
            if self.problem.isGoalReachedForState(node.state):
                return node.getSolution()  # solution
            self.fringe += self._expand(node)

    def _expand(self, node: Node):
        LOG.info(f'Exp: {node.state}, dep={node.depth}')
        # sleep(0.1)
        result = []
        sucessors = self.problem.sucessorFunction(node.state)
        for s in sucessors:
            result.append(
                Node(
                    state=s.state,
                    parent_node=node,
                    action=s.action,
                    path_cost=node.path_cost + 1,
                    depth=node.path_cost + 1
                )
            )
        return result


p = MissionariesAliveProblem(kannibals=3, missionaries=3)
ts = TreeSearch(problem=p)

print(ts.getSolution())
