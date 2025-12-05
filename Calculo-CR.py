print("Esse é um programa que ajuda você a calcular o seu Coeficiente de Rendimento.")

soma_media_ponderada = 0
carga_horaria_total = 0

qtd_materia = int(input("Quantas matérias você tem? "))

for i in range(qtd_materia):
    carga_horaria = int(input(f"Digite a carga horária da {i+1}ª matéria: "))
    media = float(input(f"Digite a média da {i+1}ª matéria: "))
    soma_media_ponderada += media * carga_horaria
    carga_horaria_total += carga_horaria

primeiro_periodo = (input("Esse é o seu primeiro período? (S/N) ").upper())

if(primeiro_periodo == 'S'):
    novo_cr = soma_media_ponderada / carga_horaria_total
else:
    cr_antigo = float(input("Digite o seu CR antigo: "))
    novo_cr = ((soma_media_ponderada / carga_horaria_total) + cr_antigo) / 2
    
print(f"CR atual: {round(novo_cr, 2)}")