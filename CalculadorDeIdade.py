def idade(data_nascimento):
    from datetime import datetime
    ano_nascimento = int(data_nascimento[6:10])
    mes_nascimento = int(data_nascimento[3:5])
    dia_nascimento = int(data_nascimento[0:2])
    ano_atual      = datetime.today().date().year
    mes_atual      = datetime.today().date().month
    dia_atual      = datetime.today().date().day
    resultadoIdade = ano_atual - ano_nascimento
    if mes_nascimento > mes_atual:
        resultadoIdade = resultadoIdade - 1
    if mes_nascimento == mes_atual and dia_nascimento > dia_atual:
        resultadoIdade = resultadoIdade + 1
    return resultadoIdade

resp = 'SIM'

while resp == 'SIM':
    ida = input("Digite a data da idade que seja calcular, exemplo '23/11/2004' : ")
    print('-' * 20)
    print(f'O resultado é {idade(ida)} anos')
    print('-' * 20)
    resp = input('Deseja calcular outra idade [sim][não]: ').upper()
    print()