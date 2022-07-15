questions = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '6', 'c': '4', 'd': '10'},
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Qual a capital de São Paulo? ',
        'respostas': {'a': 'SP', 'b': 'RJ', 'c': 'MA', 'd': 'BH'},
        'resposta_certa': 'a',
    },
    'Pergunta 3': {
        'pergunta': 'Em que ano terminou a WW2? ',
        'respostas': {'a': '2000', 'b': '450', 'c': 1890, 'd': '1945'},
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Composição química da água? ',
        'respostas': {'a': 'O2', 'b': 'H20', 'c': 'CO2', 'd': 'N2'},
        'resposta_certa': 'b',
    }
}
right_answer = 0
for qk, qv in questions.items():
    print(f"{qk}: {qv['pergunta']}")
    print('Answers: ')
    for rk, rv in qv['respostas'].items():
        print(f'[{rk}] - {rv}')

    answer_user = input('Your answer: ')
    print()
    if answer_user == qv['resposta_certa']:
        right_answer += 1
print(f'You got {right_answer}/{len(questions)} questions right!')
print(f'Your question correct percentage was {right_answer / len(questions) * 100}%')