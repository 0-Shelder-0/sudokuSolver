from math import sqrt
from typing import List

EMPTY_VALUE = 0


def convert_to_text(matrix: List[List[int]]) -> str:
    text = ''
    for line in matrix:
        for item in line:
            text += str(item)

    return text


def convert_to_matrix(text: str) -> List[List[int]] | None:
    float_size = sqrt(len(text))
    if float_size != int(float_size):
        return None

    size = int(float_size)
    matrix = []
    for line in range(size):
        matrix.append([])
        for item in range(size):
            value = int(text[line * size + item])
            matrix[line].append(value)

    return matrix
