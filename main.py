alunos = {
    "001": {"nome": "Henrique", "Idade": 21, "curso": "Sistemas de Informação", "notas": [8, 7, 9]},
    "002": {"nome": "Ana", "Idade": 22, "curso": "Engenharia de Software", "notas": [6, 5, 7]},
    "003": {"nome": "Maria", "Idade": 20, "curso": "Ciência da Computação", "notas": [9, 10, 8]},
    "004": {"nome": "João", "Idade": 23, "curso": "Redes de Computadores", "notas": [5, 5, 6]},
    "005": {"nome": "Pedro", "Idade": 21, "curso": "Banco de Dados", "notas": [3, 4, 4]},
}

# Pedir ID do aluno
id_aluno = input("Digite o ID do aluno (ex: 001, 002): ")

# Verificar se o ID existe
if id_aluno in alunos:
    aluno = alunos[id_aluno]
    notas = aluno["notas"]
    media = sum(notas) / len(notas)

    # Verificar situação com if/else
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Exibir informações completas
    print("\n=== Dados do Aluno ===")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['Idade']}")
    print(f"Curso: {aluno['curso']}")
    print(f"Notas: {notas}")
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
else:
    print("Aluno não encontrado. Verifique o ID e tente novamente.")
