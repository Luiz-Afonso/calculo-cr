print("Esse é um programa que ajuda você a calcular o seu Coeficiente de Rendimento.")

nota_cont=0
ch=0

qtd_materia=int(input("Quantas matérias você tem? "))

for i in range(qtd_materia):
    mat= int(input(f"Digite a carga horária da {i+1}ª matéria: "))
    nota= float(input(f"Digite a média da {i+1}ª matéria: "))
    nota_cont += nota*mat
    ch += mat

periodo=(input("Esse é o seu primeiro período? (S/N) ").upper())

if(periodo=="S"):
    calc = nota_cont / ch
else:
    cr_antigo=float(input("Digite o seu CR antigo: "))
    calc = ((nota_cont / ch)+cr_antigo)/2
    
print("CR atual:", round(calc,2))