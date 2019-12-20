"""
Задание 3.9 из книги Искусственный интеллектю Современный подход.
Стюард Рассел, Питер Норвиг

Задача переправки n мессионеров и m канибалов с одного берега на другой

Условая задачи: лодка может перевести одного или двух человек.
Нельзя допустить, чтобы был съеден хотя бы одни мессионер. Если группа
канибалов на одном береге превосходит по числеднности группу
мессионеров, то они их убивают и едят.
"""

from dataclasses import dataclass
from typing import List
from structures.base import State, Action, Problem, Sucessor
from structures.searches.tree import TreeSearchInterface, WideSearchMixin, \
    SimpleExpandMixin

# from time import sleep

import logging
logging.basicConfig(format='"%(asctime)s:%(levelname)s:%(name)s:%(message)s"',
                    level=logging.INFO)
LOG = logging.getLogger('39')


@dataclass
class Coast:
    """ Берег в задаче про людоедов и канибалов """

    missionaries: int = 0
    """ Кол-во мессионеров на берегу """

    kannibals: int = 0
    """ Кол-во каннибалов на берегу """

    boats: int = 0
    """ Кол-во лодок на берегу """

    def __add__(self, other: object):
        return Coast(
            missionaries=self.missionaries+other.missionaries,
            kannibals=self.kannibals+other.kannibals,
            boats=self.boats+other.boats,
        )

    def __neg__(self):
        return Coast(
            missionaries=-self.missionaries,
            kannibals=-self.kannibals,
            boats=-self.boats,
        )


@dataclass
class MKState(State):
    """ Модель мира в задаче """

    left: Coast
    """ Левый берег """

    right: Coast
    """ Правый берег """


@dataclass
class MKAction(Action):
    """ Действие, который может делать агент в этой задаче """

    direction: int  # 1 sail from right to left, -1 sail from left to right
    """
    Направление переправки людей.
    1 - С правого берега на левый
    -1 - С левого берега на правый
    """

    payload: MKState  # what to sail
    """ То, что переправляется с берега на берег """

    @property
    def left_coast_diff(self):
        """ Изменение состояния для левого берега """
        return Coast(
            missionaries=self.payload.missionaries*self.direction,
            kannibals=self.payload.kannibals*self.direction,
            boats=self.payload.boats*self.direction,
        )

    @property
    def right_coast_diff(self):
        """ Изменение состояния для правого берега """
        return -self.left_coast_diff


class MissionariesAliveProblem(Problem):
    """
    Задача переправки n мессионеров и m канибалов с одного берега на другой
    """
    def __init__(self, kannibals: int = 3, missionaries: int = 3):
        self.state_space = []
        self.kannibals = kannibals
        self.missionaries = missionaries

        self.initial_state = MKState(
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
                        MKState(
                            left=Coast(missionaries=m_in_left,
                                       kannibals=k_in_left,
                                       boats=1),
                            right=Coast(missionaries=m_in_right,
                                        kannibals=k_in_right,
                                        boats=0)
                        )
                    )
                    self.state_space.append(
                        MKState(
                            left=Coast(missionaries=m_in_left,
                                       kannibals=k_in_left,
                                       boats=0),
                            right=Coast(missionaries=m_in_right,
                                        kannibals=k_in_right,
                                        boats=1)
                        )
                    )

    def isGoalReachedForState(self, state: MKState) -> bool:
        return (state.left.missionaries == 0
                and state.left.kannibals == 0
                and state.right.missionaries == 3
                and state.right.kannibals == 3)

    def sucessorFunction(self, state: MKState) -> List[Sucessor]:
        direction = 1 if state.right.boats == 1 else -1

        actions = [
            MKAction(direction=direction, payload=Coast(missionaries=2,
                                                        boats=1)),
            MKAction(direction=direction, payload=Coast(missionaries=1,
                                                        kannibals=1, boats=1)),
            MKAction(direction=direction, payload=Coast(kannibals=2, boats=1)),
            MKAction(direction=direction, payload=Coast(kannibals=1, boats=1)),
            MKAction(direction=direction, payload=Coast(missionaries=1,
                                                        boats=1)),
        ]

        possible_sucessors = [
            Sucessor(
                action=a,
                state=MKState(
                   left=state.left + a.left_coast_diff,
                   right=state.right + a.right_coast_diff,
                )
            )
            for a in actions
        ]
        return [
            s for s in possible_sucessors if s.state in self.state_space
        ]


class TreeSearch(WideSearchMixin, SimpleExpandMixin, TreeSearchInterface, ):
    pass


p = MissionariesAliveProblem(kannibals=3, missionaries=3)
ts = TreeSearch(problem=p, logger=LOG)

print(ts.solution)
