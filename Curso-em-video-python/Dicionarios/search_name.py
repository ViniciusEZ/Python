import re
from typing import List, Dict

pessoas: List[Dict[str, str]] = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Moreira'},
    {'nome': 'Elaine', 'sobrenome': 'Figueiredo'},
    {'nome': 'Helena', 'sobrenome': 'Oliveira'},
    {'nome': 'vivian', 'sobrenome': 'Silva'},
    {'nome': 'Fabrício', 'sobrenome': 'Costa'},
    {'nome': 'Eduardo', 'sobrenome': 'Vieira'},
    {'nome': 'Lívia', 'sobrenome': 'Madeira'},
    {'nome': 'João', 'sobrenome': 'Barbosa'},
    {'nome': 'Dania', 'sobrenome': 'Maia'},
]


def search_person(pessoas: List[Dict[str, str]], searched_name: str) -> Dict[str, str]:
    for person in pessoas:
        name, last_name = person.values()

        if searched_name == f'{name} {last_name}':
            return person

        regex = re.compile(fr'{name}\s+{last_name}', flags=re.I)
        if regex.search(searched_name):
            return person

    return {}


if __name__ == '__main__':
    person_1 = search_person(pessoas, 'Luiz miranda')
    person_2 = search_person(pessoas, 'João Barbosa')
    print(person_1)
    print(person_2)
