from math import sqrt
from typing import List

MATRIX_EMPTY_VALUE = ''
STRING_EMPTY_VALUE = '0'


def convert_to_text(matrix: List[List[str]]) -> str:
    text = ''
    for line in matrix:
        for item in line:
            if item is None or item == MATRIX_EMPTY_VALUE:
                text += STRING_EMPTY_VALUE
            else:
                text += item

    return text


def convert_to_matrix(text: str) -> List[List[str]] | None:
    float_size = sqrt(len(text))
    if float_size != int(float_size):
        return None

    size = int(float_size)
    matrix = []
    for line in range(size):
        matrix.append([])
        for item in range(size):
            value = text[line * size + item]
            if value == STRING_EMPTY_VALUE:
                value = MATRIX_EMPTY_VALUE
            matrix[line].append(value)

    return matrix
