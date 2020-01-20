"""
Структуры для создания агентов
"""
from dataclasses import dataclass
from typing import Callable, List, Optional


@dataclass
class State:
    """
    Состояние окружающей среды, в кторой может действовать агент

    Должно определяться в конкретной задаче
    """
    pass


@dataclass
class Action:
    """
    Действие, которое может сделать агент
    """
    pass


@dataclass
class Sucessor:
    """
    Состояние state, которое может притворить в жизнь агент,
    сделав действие action
    """
    action: Action  # action to do
    state: State  # result state


@dataclass
class Problem:
    """
    Задача, которую должен решить агент
    """

    initial_state: State
    """ Состояние окружающей среды на момент начала работы агента """

    goalFunction: Callable[[State], bool]
    """
    Функция проверки достажения цели задачи.
    Возвращает true, если цель достигнута
    """

    sucessorFunction: Callable[[State], List[Sucessor]]
    """
    Функция получения всех действий и состояний, которыe может достич агент
    из состояния state
    """


@dataclass
class ProblemWithKnownTarget(Problem):
    """
    Задача, которую должен решить агент
    """

    target_state: State
    """ Состояние окружающей среды на момент начала работы агента """

    def isGoalReachedForState(self, state: State) -> bool:
        return state == self.target_state


@dataclass
class Solution:
    """
    Описание решения задачи агентом
    """

    actions: list
    """ Последовательность действий, которые должен выполенить агент """

    depth: int
    """ Кол-во действий, которые должен выполенить агент """

    path_cost: int
    """ Стоимость решения """


@dataclass
class Node:
    """
    Узел в дереве решений агента
    """

    state: State
    """ Состояние окружающей среды, которое было достигнуто в узлe """

    parent_node: Optional[object]  # object is Node
    """ Родительский узел """

    action: Optional[Action]
    """ Действие, нужное для достижение этого узла из родительского """

    path_cost: int
    """ Стоимость достижения этого узла из корневого """

    depth: int
    """ Глубина этого узла """

    @property
    def solution(self) -> Solution:
        """ Получение решения для достижения этого узла из корневого """
        actions = []
        node = self
        while node is not None:
            actions.append(node.action)
            node = node.parent_node

        return Solution(path_cost=self.path_cost,
                        depth=self.depth,
                        actions=list(reversed(actions)))

    @property
    def state_path(self) -> Solution:
        """ Получение решения для достижения этого узла из корневого """
        result = []
        node = self
        while node is not None:
            result.append(str(node.state))
            node = node.parent_node

        return result
