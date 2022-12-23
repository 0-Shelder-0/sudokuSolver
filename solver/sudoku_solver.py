import math
from typing import List, Set


def get_solution(initial_solution: List[List[int]]) -> List[List[int]]:
    if not check_solution(initial_solution):
        return initial_solution

    solution = initial_solution.copy()
    empty_cells = get_empty_cells(solution)
    (solution, success) = solve(solution, empty_cells)

    if not success:
        return initial_solution

    return solution


def solve(solution: List[List[int]], empty_cells: list[tuple[int, int]], index: int = 0, value: int = 0) -> tuple[List[List[int]], bool]:
    if index > len(empty_cells):
        return solution, False

    if index > 0:
        (x, y) = empty_cells[index - 1]
        solution[x][y] = value

    if index == len(empty_cells):
        return solution, check_solution(solution)

    (x, y) = empty_cells[index]
    possible_values = get_possible_values(solution, x, y)
    for val in possible_values:
        (solution, solved) = solve(solution, empty_cells, index + 1, val)
        if solved:
            return solution, solved
        else:
            solution[x][y] = 0

    return solution, False


def get_empty_cells(matrix: List[List[int]]) -> list[tuple[int, int]]:
    empty_cells = []
    size = len(matrix)

    for x in range(size):
        for y in range(size):
            if matrix[x][y] == 0:
                empty_cells.append((x, y))

    return empty_cells


def check_solution(solution: List[List[int]]) -> bool:
    return check_columns(solution) and check_rows(solution) and check_sections(solution)


def check_columns(solution: List[List[int]]) -> bool:
    size = len(solution)

    for y in range(size):
        values = []
        for x in range(size):
            if values.__contains__(solution[x][y]):
                return False
            if solution[x][y] != 0:
                values.append(solution[x][y])

    return True


def check_rows(solution: List[List[int]]) -> bool:
    size = len(solution)

    for x in range(size):
        values = []
        for y in range(size):
            if values.__contains__(solution[x][y]):
                return False
            if solution[x][y] != 0:
                values.append(solution[x][y])

    return True


def check_sections(solution: List[List[int]]) -> bool:
    section_size = int(math.sqrt(len(solution)))

    for sx in range(section_size):
        for sy in range(section_size):
            values = []
            min_x = sx * section_size
            max_x = sx * section_size + section_size

            min_y = sy * section_size
            max_y = sy * section_size + section_size

            for x in range(min_x, max_x):
                for y in range(min_y, max_y):
                    if values.__contains__(solution[x][y]):
                        return False
                    if solution[x][y] != 0:
                        values.append(solution[x][y])

    return True


def get_possible_values(matrix: List[List[int]], x: int, y: int) -> Set[int]:
    size = len(matrix)
    all_possible_values = set([x + 1 for x in range(size)])

    values = set()
    values = get_possible_from_column(matrix, x, values)
    values = get_possible_from_row(matrix, y, values)
    values = get_possible_from_section(matrix, x, y, values)

    return all_possible_values.difference(values)


def get_possible_from_column(matrix: List[List[int]], x: int, values: set) -> Set[int]:
    size = len(matrix)
    for y in range(size):
        values.add(matrix[x][y])

    return values


def get_possible_from_row(matrix: List[List[int]], y: int, values: set) -> Set[int]:
    size = len(matrix)
    for x in range(size):
        values.add(matrix[x][y])

    return values


def get_possible_from_section(matrix: List[List[int]], x: int, y: int, values: set) -> Set[int]:
    section_size = int(math.sqrt(len(matrix)))
    section_x = int(x / section_size)
    min_x = section_x * section_size
    max_x = section_x * section_size + section_size

    section_y = int(y / section_size)
    min_y = section_y * section_size
    max_y = section_y * section_size + section_size

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            values.add(matrix[x][y])

    return values
