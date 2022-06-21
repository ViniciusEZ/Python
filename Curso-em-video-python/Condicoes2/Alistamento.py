from datetime import date

atual = date.today().year
nasc = int(input("Digite seu ano de nascimento: "))
ida = atual - nasc
print(f"\nQuem nasceu em {nasc} tem {ida} anos em {atual}")


if ida == 18:
    print("\nEstá na hora de se alistar!")
elif ida > 18:
    print(f"\nPassou do tempo de prazo do alistamento! tempo passado: {ida - 18} ano(s)")
else:
    print(f"\nFaltam cerca de {18 - ida} anos para você se alistar!")
