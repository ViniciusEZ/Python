from typing import List
from copy import deepcopy

stack: List[List[str]] = []
stack.append(['A'])
stack.append(['B'])
stack.append(['C'])

print('FOR: ')
for item in stack[::-1]:
    print(item)

stack_copy = deepcopy(stack)

print('\nWHILE: ')
while stack_copy:
    item2 = stack_copy.pop()
    item2 += ['Manipulei']
    print(item2)

print(f'\nYour stack: {stack}')


# top_item = stack.pop()
# top_item = stack.pop()
# top_item = stack.pop()

# print(stack, top_item)