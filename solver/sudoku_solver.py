from solver.converter import convert_to_matrix, convert_to_str


def get_solution(initial_solution: str) -> str:
    matrix = convert_to_matrix(initial_solution)
    solution = solve(matrix)
    result = convert_to_str(solution)

    return result


def solve(matrix):
    # todo реализовать механизм решения
    return matrix
