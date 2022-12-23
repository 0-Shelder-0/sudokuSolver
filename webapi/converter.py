from math import sqrt
from typing import List


def convert_to_text(matrix: List[List[str]]) -> str:
    text = ''
    for line in matrix:
        for item in line:
            if item is None or item == '':
                text += '0'
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
            matrix[line].append(text[line * size + item])

    return matrix
