"""
Задание 3.10 из книги Искусственный интеллектю Современный подход.
Стюард Рассел, Питер Норвиг

Задача игры в 8

Условая задачи: есть поле 3 на 3, в нем 8 карточек с чисталми от 1 до 8,
расставленных в
определенном порядке (начальное состояние). Числа можно передвигать на одну
состеднюю позицию, если она пустая. Задача в поиске решения перевода поля к
целевому состоянию
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
from structures.base import State, Action, Problem, Sucessor
from structures.searches.tree import TreeSearchInterface, WideSearchMixin, \
    SimpleExpandMixin
from copy import deepcopy

# from time import sleep

import logging
logging.basicConfig(format='"%(asctime)s:%(levelname)s:%(name)s:%(message)s"',
                    level=logging.INFO)
LOG = logging.getLogger('3.10')


@dataclass
class Card():
    """ Карточка с номером """

    number: int


@dataclass
class State8(State):
    """ состояние - поле 3 на 3 """
    field: Dict[Tuple[int, int], Card]

    pass


@dataclass
class Action8(Action):
    """ Действие, который может делать агент в этой задаче """

    direction: Tuple[int, int]
    """
    Направление перестановки карточки.
    1, 0 - вправо
    0. 1 - вверх
    -1. 0 - влево
    0, -1 вниз
    """
    POSIBLE_DIRECTIONS = (
        (1, 0),  # вправо
        (-1, 0),  # влево
        (0, 1),  # вверх
        (0, -1),  # вниз
    )

    payload: Card  # what to sail
    """ То, что переставляется """


class Problem8(Problem):
    """
        Задача нахождения оптимального набора действий для игры в 8
    """
    def __init__(self, initial_state: State8, target_state: State8):
        self.initial_state = initial_state
        self.target_state = target_state

    def isGoalReachedForState(self, state: State8) -> bool:
        return state == self.target_state

    @staticmethod
    def _findEmptyPosition(state):
        for i in range(3):
            for j in range(3):
                if state.field[i, j] is None:
                    return i, j
        raise Exception('No Empty Position')

    def sucessorFunction(self, state: State8) -> List[Sucessor]:
        result = []
        empty_position = self._findEmptyPosition(state)
        for direction in Action8.POSIBLE_DIRECTIONS:
            new_empty_position = tuple(
                map(sum, zip(empty_position,  direction))
            )
            if new_empty_position in state.field:
                new_state = deepcopy(state)
                card = new_state.field[new_empty_position]
                new_state.field[empty_position] = card
                new_state.field[new_empty_position] = None
                result.append(Sucessor(
                    state=new_state,
                    action=Action8(
                        direction=direction,
                        payload=card
                    )
                ))
        return result


# class TreeSearch(TreeSearchInterface, WideSearchMixin, SimpleExpandMixin):
class TreeSearch(WideSearchMixin, SimpleExpandMixin, TreeSearchInterface):
    pass


initial_state = State8(field={
    (0, 0): Card(number=1),
    (0, 1): Card(number=2),
    (0, 2): Card(number=3),
    (1, 0): Card(number=4),
    (1, 1): Card(number=5),
    (1, 2): Card(number=6),
    (2, 0): Card(number=7),
    (2, 1): Card(number=8),
    (2, 2): None,
})

target_state = State8(field={
    (0, 0): Card(number=1),
    (0, 1): Card(number=2),
    (0, 2): None,
    (1, 0): Card(number=4),
    (1, 1): Card(number=5),
    (1, 2): Card(number=3),
    (2, 0): Card(number=7),
    (2, 1): Card(number=8),
    (2, 2): Card(number=6),
})


p = Problem8(initial_state=initial_state, target_state=target_state)
ts = TreeSearch(problem=p, logger=LOG)

print(ts.solution)
