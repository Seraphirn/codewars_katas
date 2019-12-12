from .base import Problem, Solution, Node

import logging
logging.basicConfig(format='"%(asctime)s:%(levelname)s:%(name)s:%(message)s"',
                    level=logging.INFO)
LOG = logging.getLogger('39')


class TreeSearch():
    def __init__(self, problem: Problem, fringe: list = [],
                 *, logger: object):
        self.problem = problem
        self.fringe = fringe
        self.logger = logger

    @property
    def solution(self) -> Solution:
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
                return node.solution
            self.fringe += self._expand(node)

    def _expand(self, node: Node):
        self.logger.info(f'Exp: {node.state}, dep={node.depth}')
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
