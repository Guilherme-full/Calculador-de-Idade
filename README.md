# Projeto Calculador de Idade (Guilherme Xavier Souza)

## Clonar Repositório
```
git clone https://github.com/Guilherme-full/Calculador-de-Idade.git
```

|          | Linux | macOS | Windows |
|   :---   | :---: | :---: | :---:   |
| Chromium <!-- GEN:chromium-version -->93.0.4543.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| WebKit <!-- GEN:webkit-version -->14.2<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |
| Firefox <!-- GEN:firefox-version -->89.0<!-- GEN:stop --> | :white_check_mark: | :white_check_mark: | :white_check_mark: |

## Descrição

Projeto realizado em Python, utilizando a biblioteca datetime , no qual o projeto consiste em um calculador de idade,
a partir da data de nascimento que é inserida.


## Bibliotecas 

```
from  datetime import datetime
```

Função
```
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
```

## Corpo Principal do Programa
```
resp = 'SIM'

while resp == 'SIM':
    ida = input("Digite a data da idade que seja calcular, exemplo '23/11/2004' : ")
    print('-' * 20)
    print(f'O resultado é {idade(ida)} anos')
    print('-' * 20)
    resp = input('Deseja calcular outra idade [sim][não]: ').upper()
    print()
```

## Ferramenta e Linguagem
<img align="center"  alt="Python" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></img>
<img align="center"  alt="Pycharm" heigth= "40" width ="60" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pycharm/pycharm-original.svg"></img>

