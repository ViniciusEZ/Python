from collections import namedtuple
from typing import List

# def fatorial(n: int) -> int:
#     # Caso base
#     if n == 1:
#         return 1
#     # Caso recursivo
#     return n * fatorial(n - 1)
#
#
# if __name__ == '__main__':
#     fat5 = fatorial(5)
#     print(fat5)

Box = namedtuple('Box', 'tem_chave')


def find_key(boxes: List[Box], index: int = 0) -> Box:
    # Caso Base
    if len(boxes) <= index:
        return Box(False)
    box = boxes[index]
    #  Case base
    if box.tem_chave:
        return box
    # Caso recursivo
    index += 1
    return find_key(boxes, index)


if __name__ == '__main__':
    boxes: List[Box] = [
        Box(False), Box(False), Box(False), Box(False),
        Box(False), Box(False), Box(False), Box(False),
        Box(False), Box(True), Box(False), Box(False)
    ]

    print(find_key(boxes))
