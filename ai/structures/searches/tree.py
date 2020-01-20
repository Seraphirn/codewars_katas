from ..base import Problem, Solution, Node, ProblemWithKnownTarget
# from time import sleep


class WideTreeSearch():

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
            node = self._popNodeFromFringeToExpand()
            if self.problem.isGoalReachedForState(node.state):
                return node.solution
            self.fringe += self._expand(node)

    def _popNodeFromFringeToExpand(self):
        return self.fringe.pop(0)

    def _expand(self, node: Node):
        self.logger.info(f'Expand: \n{node.state}, dep={node.depth}')
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


class DepthTreeSearch(WideTreeSearch):
    def _popNodeFromFringeToExpand(self):
        return self.fringe.pop()


class LimitedDepthTreeSearch(DepthTreeSearch):
    def __init__(self, max_depth: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_depth = max_depth

    def _expand(self, node: Node):
        return super()._expand(node) if node.depth < self.max_depth else []


class TwoWayWideTreeSearch(WideTreeSearch):
    def __init__(self,
                 problem: ProblemWithKnownTarget,
                 target_fringe: list = [],
                 *args, **kwargs):
        super().__init__(problem, *args, **kwargs)
        self.target_fringe = target_fringe

    def _popNodeFromTargetFringeToExpand(self):
        return self.target_fringe.pop(0)

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
        self.target_fringe.append(
            Node(
                state=self.problem.target_state,
                parent_node=None,
                action=None,
                path_cost=0,
                depth=0
            )
        )
        # import pdb; pdb.set_trace()
        while True:
            if not self.fringe or not self.target_fringe:
                raise Exception('No solution')
            node = self._popNodeFromFringeToExpand()
            node2 = self._popNodeFromTargetFringeToExpand()

            for tmpnode in self.fringe:
                for tmpnode2 in self.target_fringe:
                    if tmpnode.state == tmpnode2.state:
                        return '\n\n'.join(reversed(tmpnode.state_path)) \
                            + '\n\n' \
                            + '\n\n'.join(tmpnode2.state_path)

            # states1 = set(n.state for n in self.fringe)
            # states2 = set(n.state for n in self.target_fringe)
            # istates = states1.intersection(states2)
            # if istates:
            #     state = istates.pop()
            #     return

            self.fringe += self._expand(node)
            self.target_fringe += self._expand(node2)
