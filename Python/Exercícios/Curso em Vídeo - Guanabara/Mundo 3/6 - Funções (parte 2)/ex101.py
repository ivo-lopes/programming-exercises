def voto(ano):
    from datetime import date
    condicao = date.today().year - ano
    if condicao < 16:
        return f'Você tem {condicao} anos: NÃO VOTA'
    elif 16 <= condicao < 18 or condicao >= 65:
        return f'Você tem {condicao} anos: VOTO OPCIONAL'
    else:
        return f'Você tem {condicao} anos: VOTO OBRIGATÓRIO'

idade = int(input('Digite seu ano de nascimento: '))
print(voto(idade))