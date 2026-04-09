Turma = int(input('Quantos alunos tem na sala?'))

contador = 0
aprovados = 0

while contador < Turma:
    Nota = float(input(f'Digite a nota de cada aluno {contador +1}:' ))
    
    if Nota >= 6.0:
        aprovados = aprovados +1

    contador = contador +1

print(f'Total de alunos aprovados {aprovados}')
