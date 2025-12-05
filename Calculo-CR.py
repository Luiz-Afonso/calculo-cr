# mensagem inicial 
print("Esse é um programa que ajuda você a calcular o seu Coeficiente de Rendimento Acadêmico.")

# declaração de variáveis acumuladoras necessárias para o cálculo do CRA
soma_media_ponderada = 0
carga_horaria_total = 0

# variável que guarda a quantidade de matérias, fornecida pelo usuário
qtd_materia = int(input("Quantas matérias você tem? "))

# laço de repetição que vai se repetir de acordo com a quantidade de metérias do usuário
for i in range(qtd_materia):

    # variável que vai receber, do usuário, as cargas horárias de cada matéria
    carga_horaria = int(input(f"Digite a carga horária da {i+1}ª matéria: "))

    # variável que vai receber, do usuário, as médias de cada matéria
    media = float(input(f"Digite a média da {i+1}ª matéria: "))

    # atribuição dos valores das variáveis acumuladoras, necessária para o cálculo do CRA
    soma_media_ponderada += media * carga_horaria
    carga_horaria_total += carga_horaria

# variável que guarda a informação do período atual do usuário, fornecida pelo usuário
primeiro_periodo = (input("Esse é o seu primeiro período? (S/N) ").upper())

# estrutura condicinal que definirá o cálculo correto a ser utilizado, de acordo com a informação do período atual do usuário
if(primeiro_periodo == 'S'):

    # variável que guarda o resultado do novo CRA, caso seja o primeiro período do usuário
    novo_cra = soma_media_ponderada / carga_horaria_total

else:

    # variável que guarda o CRA antigo, fornecido pelo usuário
    cra_antigo = float(input("Digite o seu CR antigo: "))

    # variável que guarda o resultado do novo CRA, caso não seja o primeiro período do usuário
    novo_cra = ((soma_media_ponderada / carga_horaria_total) + cra_antigo) / 2
    
# mensagem final informando o novo CRA do usuário
print(f"CR atual: {round(novo_cra, 2)}")