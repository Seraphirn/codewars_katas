def snail(array):
    steps = ((0, 1), (1, 0), (0, -1), (-1, 0))
    step_position = 0
    step = steps[step_position]

    visited_cells = []
    position = (0, 0)
    result = []
    m = len(array)
    n = len(array[0])

    while True:
        x, y = position
        try:
            result.append(array[position[0]][position[1]])
            visited_cells.append(position)
        except Exception:
            break

        next_position = (x + step[0], y + step[1])
        if (next_position[0] == n) or (next_position[0] == -1) \
                or (next_position[1] == m) or (next_position[1] == -1)\
                or next_position in visited_cells:
            step_position = (step_position + 1) % len(steps)
            step = steps[step_position]
            next_position = (x + step[0], y + step[1])

        if next_position in visited_cells:
            break
        else:
            position = next_position
    return result



snail(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
