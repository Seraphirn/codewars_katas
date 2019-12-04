from dataclasses import dataclass


@dataclass
class Coast:
    missionaries: int
    kannibals: int
    boats: int = 0


@dataclass
class State:
    left: Coast
    right: Coast


# @dataclass
# class Node:
#     state: Coast
#     parent_node: Node
#     action: Node

KANNIBALS_COUNT = 3
MISSIONARIES_COUNT = 3


state_space = []

for k_in_left in range(KANNIBALS_COUNT + 1):  # 0..KANNIBALS_COUNT
    for m_in_left in range(MISSIONARIES_COUNT + 1):  # 0..MISSIONARIES_COUNT
        k_in_right = KANNIBALS_COUNT - k_in_left
        m_in_right = MISSIONARIES_COUNT - m_in_left
        if (m_in_right >= k_in_right or m_in_right == 0) \
                and (m_in_left >= k_in_left or m_in_left == 0):
            state_space.append(
                State(
                    left=Coast(missionaries=m_in_left,
                               kannibals=k_in_left,
                               boats=1),
                    right=Coast(missionaries=m_in_right,
                                kannibals=k_in_right,
                                boats=0)
                )
            )
            state_space.append(
                State(
                    left=Coast(missionaries=m_in_left,
                               kannibals=k_in_left,
                               boats=0),
                    right=Coast(missionaries=m_in_right,
                                kannibals=k_in_right,
                                boats=1)
                )
            )

print(len(state_space))


# initial_state = states[0]

# def goalFunction(node):
#     return node.state == State(right=Coast(missionaries=3, kannibals=3) left=Coast(missionaries=0, kannibals=0)

# def treeSearch(goalFunction=goalFunction, fringe=[])
