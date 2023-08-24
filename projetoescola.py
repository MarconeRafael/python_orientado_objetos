"""Crie um programa que peça o nome, a turma e as notas dos alunos e gere um relatório com os alunos aprovados, em recuperação ou reprovados e também a média de cada turma."""

turma  = input("Digite sua turma: ")

Anotas = []
Dnotas = []
Cnotas = []
Dnotas = []
Anomes = []
Bnomes = []
Cnomes = []
Dnomes = []
while True:
    if turma = 'a'.lower:
        nome = input("Digite seu nome completo: ")
        Anomes.append(nome)
        nota1 = float(input("Digite sua 1º nota: "))
        nota2 = float(input("Digite sua 2º nota: "))
        nota3 = float(input("Digite sua 3º nota: "))
        nota4 = float(input("Digite sua 4º nota: "))
        soma = nota1 + nota2 + nota3 + nota4
        media = soma/4
        Anotas.append(media)
    elif turma = 'b'.lower:
        nome = input("Digite seu nome completo: ")
        nota1 = float(input("Digite sua 1º nota: "))
        Bnomes.append(nome)
        nota2 = float(input("Digite sua 2º nota: "))
        nota3 = float(input("Digite sua 3º nota: "))
        nota4 = float(input("Digite sua 4º nota: "))
        soma = nota1 + nota2 + nota3 + nota4
        media = soma/4
        Bnotas.append(media)
    elif turma = 'c'.lower:
        nome = input("Digite seu nome completo: ")
        Cnomes.append(nome)
        nota1 = float(input("Digite sua 1º nota: "))
        nota2 = float(input("Digite sua 2º nota: "))
        nota3 = float(input("Digite sua 3º nota: "))
        nota4 = float(input("Digite sua 4º nota: "))
        soma = nota1 + nota2 + nota3 + nota4
        media = soma/4
        Cnotas.append(media)
    elif turma = 'd'.lower:
        nome = input("Digite seu nome completo: ")
        Dnomes.append(nome)
        nota1 = float(input("Digite sua 1º nota: "))
        nota2 = float(input("Digite sua 2º nota: "))
        nota3 = float(input("Digite sua 3º nota: "))
        nota4 = float(input("Digite sua 4º nota: "))
        soma = nota1 + nota2 + nota3 + nota4
        media = soma/4
        Dnotas.append(media)
    else:
        print("Turma inválida.")
As = sum(Anotas)
Bs = sum(Dnotas)
Cs = sum(Cnotas)
ds = sum(Dnotas)
Al = len(Anotas)
Bl = len(Dnotas)
Cl = len(Cnotas)
Dl = len(Dnotas)
mediaA = As/Al
mediaB = Bs/Bl
mediaC = Cs/Cl
mediaD = Ds/Dl
soma = nota1 + nota2 + nota3 + nota4
media = soma/4
print("O aluno {}, da turma {} ficou com a média {}".format(nome, turma, media))