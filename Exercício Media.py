


control = True

while(control == True):
    nome = input("Digite seu nome: ")
    turma = input("Digite sua turma: ")
    matricula = int(input("Digite sua matrícula: "))

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    media = (n1+n2+n3+n4) / 4

    if(media >= 7):
        print("Parabéns, você foi aprovado! ", media)
    if(media <= 6.9):
        print("Você ficou em recuperação! ", media)
    if(media <=5):
        print("Reprovado! Favor remarcar prova Final. ", media)

    control2 = input("Deseja continuar com o formulário de notas dos alunos? S/N\n R.:")
    if(control2.upper() == "S"):
        control = True
    else:
        control = False
