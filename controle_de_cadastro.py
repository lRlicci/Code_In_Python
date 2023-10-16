class Aluno:
    def __init__(self, ra, nome, cpf, curso_id):
        self.ra = ra
        self.nome = nome
        self.cpf = cpf
        self.curso_id = curso_id

class Curso:
    def __init__(self, curso_id, nome):
        self.curso_id = curso_id
        self.nome = nome
        self.disciplinas = []

class Disciplina:
    def __init__(self, disciplina_id, nome):
        self.disciplina_id = disciplina_id
        self.nome = nome

alunos = [] 
cursos = []
disciplinas = []

def incluirAluno():
    ra = input("Digite o RA do aluno: ")
    nome = input("Digite o nome do aluno: ")
    cpf = input("Digite o CPF do aluno: ")
    curso_id = int(input("Digite o ID do curso do aluno: "))

    # Verifica se o curso existe
    curso_existente = False
    for curso in cursos:
        if curso.curso_id == curso_id:
            curso_existente = True
            break

    if curso_existente:
        aluno = Aluno(ra, nome, cpf, curso_id)
        alunos.append(aluno)
        print("Aluno cadastrado com sucesso.")
    else:
        print("Curso não encontrado.")

def alterarAluno():
    ra = input("Digite o RA do aluno que deseja alterar: ")
    aluno_encontrado = False

    for aluno in alunos:
        if aluno.ra == ra:
            novo_nome = input("Digite o novo nome do aluno: ")
            novo_cpf = input("Digite o novo CPF do aluno: ")
            aluno.nome = novo_nome
            aluno.cpf = novo_cpf
            aluno_encontrado = True
            print("Aluno alterado com sucesso.")
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")

def consultarAlunoRA():
    ra = input("Digite o RA do aluno que deseja consultar: ")
    aluno_encontrado = False

    for aluno in alunos:
        if aluno.ra == ra:
            print("RA:", aluno.ra)
            print("Nome:", aluno.nome)
            print("CPF:", aluno.cpf)

            for curso in cursos:
                if curso.curso_id == aluno.curso_id:
                    print("Curso:", curso.nome)
                    print("Disciplinas do Curso:")
                    for disciplina in curso.disciplinas:
                        print("  -", disciplina.nome)
                    break

            aluno_encontrado = True
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")

def relatorioAluno():
    for aluno in alunos:
        print("RA:", aluno.ra)
        print("Nome:", aluno.nome)
        print("CPF:", aluno.cpf)

        for curso in cursos:
            if curso.curso_id == aluno.curso_id:
                print("Curso:", curso.nome)
                print("Disciplinas do Curso:")
                for disciplina in curso.disciplinas:
                    print("  -", disciplina.nome)
                break

def excluirAluno():
    ra = input("Digite o RA do aluno que deseja excluir: ")
    aluno_encontrado = False

    for aluno in alunos:
        if aluno.ra == ra:
            alunos.remove(aluno)
            print("Aluno excluído com sucesso.")
            aluno_encontrado = True
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")

def incluirCurso():
    curso_id = int(input("Digite o ID do curso: "))
    nome = input("Digite o nome do curso: ")

    curso = Curso(curso_id, nome)
    cursos.append(curso)
    print("Curso cadastrado com sucesso.")

def alterarCurso():
    curso_id = int(input("Digite o ID do curso que deseja alterar: "))
    curso_encontrado = False

    for curso in cursos:
        if curso.curso_id == curso_id:
            novo_nome = input("Digite o novo nome do curso: ")
            curso.nome = novo_nome
            curso_encontrado = True
            print("Curso alterado com sucesso.")
            break

    if not curso_encontrado:
        print("Curso não encontrado.")

def consultarCursoID():
    curso_id = int(input("Digite o ID do curso que deseja consultar: "))
    curso_encontrado = False

    for curso in cursos:
        if curso.curso_id == curso_id:
            print("ID:", curso.curso_id)
            print("Nome:", curso.nome)
            print("Disciplinas do Curso:")
            for disciplina in curso.disciplinas:
                print("  -", disciplina.nome)
            curso_encontrado = True
            break

    if not curso_encontrado:
        print("Curso não encontrado.")

def relatorioCurso():
    for curso in cursos:
        print("==============================")
        print("ID:", curso.curso_id)
        print("Nome:", curso.nome)
        print("Disciplinas do Curso:")
        for disciplina in curso.disciplinas:
            print("  -", disciplina.nome)
        print("==============================")

def excluirCurso():
    curso_id = int(input("Digite o ID do curso que deseja excluir: "))
    curso_encontrado = False

    for curso in cursos:
        if curso.curso_id == curso_id:
            cursos.remove(curso)
            print("Curso excluído com sucesso.")
            curso_encontrado = True
            break

    if not curso_encontrado:
        print("Curso não encontrado.")

def incluirDisciplina():
    disciplina_id = int(input("Digite o ID da disciplina: "))
    nome = input("Digite o nome da disciplina: ")

    disciplina = Disciplina(disciplina_id, nome)
    disciplinas.append(disciplina)
    print("Disciplina cadastrada com sucesso.")

def alterarDisciplina():
    disciplina_id = int(input("Digite o ID da disciplina que deseja alterar: "))
    disciplina_encontrada = False

    for disciplina in disciplinas:
        if disciplina.disciplina_id == disciplina_id:
            novo_nome = input("Digite o novo nome da disciplina: ")
            disciplina.nome = novo_nome
            disciplina_encontrada = True
            print("Disciplina alterada com sucesso.")
            break

    if not disciplina_encontrada:
        print("Disciplina não encontrada.")

def consultarDisciplinaID():
    disciplina_id = int(input("Digite o ID da disciplina que deseja consultar: "))
    disciplina_encontrada = False

    for disciplina in disciplinas:
        if disciplina.disciplina_id == disciplina_id:
            print("ID:", disciplina.disciplina_id)
            print("Nome:", disciplina.nome)
            disciplina_encontrada = True
            break

    if not disciplina_encontrada:
        print("Disciplina não encontrada.")

def relatorioDisciplina():
    for disciplina in disciplinas:
        print("ID:", disciplina.disciplina_id)
        print("Nome:", disciplina.nome)

def excluirDisciplina():
    disciplina_id = int(input("Digite o ID da disciplina que deseja excluir: "))
    disciplina_encontrada = False

    for disciplina in disciplinas:
        if disciplina.disciplina_id == disciplina_id:
            disciplinas.remove(disciplina)
            print("Disciplina excluída com sucesso.")
            disciplina_encontrada = True
            break

    if not disciplina_encontrada:
        print("Disciplina não encontrada.")

def atribuirDisciplinaCurso():
    curso_id = int(input("Digite o ID do curso ao qual deseja atribuir a disciplina: "))
    disciplina_id = int(input("Digite o ID da disciplina que deseja atribuir ao curso: "))

    curso_encontrado = None
    disciplina_encontrada = None

    for curso in cursos:
        if curso.curso_id == curso_id:
            curso_encontrado = curso
            break

    for disciplina in disciplinas:
        if disciplina.disciplina_id == disciplina_id:
            disciplina_encontrada = disciplina
            break

    if curso_encontrado is not None and disciplina_encontrada is not None:
        curso_encontrado.disciplinas.append(disciplina_encontrada)
        print(f"Disciplina '{disciplina_encontrada.nome}' atribuída ao curso '{curso_encontrado.nome}' com sucesso.")
    else:
        print("Curso ou disciplina não encontrados.")

def menuPrincipal():
    while True:
        print("\nMenu Principal:")
        print("1. Cadastro de Alunos")
        print("2. Cadastro de Cursos")
        print("3. Cadastro de Disciplinas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nMenu de Cadastro de Alunos:")
            print("a. Incluir")
            print("b. Alterar")
            print("c. Consultar pelo RA")
            print("d. Relatório completo")
            print("e. Excluir")

            sub_opcao = input("Escolha uma opção: ")

            if sub_opcao == "a":
                incluirAluno()
            elif sub_opcao == "b":
                alterarAluno()
            elif sub_opcao == "c":
                consultarAlunoRA()
            elif sub_opcao == "d":
                relatorioAluno()
            elif sub_opcao == "e":
                excluirAluno()
            else:
                print("Opção inválida.")

        elif opcao == "2":
            print("\nMenu de Cadastro de Cursos:")
            print("a. Incluir")
            print("b. Alterar")
            print("c. Consultar pelo ID")
            print("d. Relatório completo")
            print("e. Excluir")

            sub_opcao = input("Escolha uma opção: ")

            if sub_opcao == "a":
                incluirCurso()
            elif sub_opcao == "b":
                alterarCurso()
            elif sub_opcao == "c":
                consultarCursoID()
            elif sub_opcao == "d":
                relatorioCurso()
            elif sub_opcao == "e":
                excluirCurso()
            else:
                print("Opção inválida.")

        elif opcao == "3":
            print("\nMenu de Cadastro de Disciplinas:")
            print("a. Incluir")
            print("b. Alterar")
            print("c. Consultar pelo ID")
            print("d. Relatório completo")
            print("e. Excluir")
            print("f. Atribuir a curso")

            sub_opcao = input("Escolha uma opção: ")

            if sub_opcao == "a":
                incluirDisciplina()
            elif sub_opcao == "b":
                alterarDisciplina()
            elif sub_opcao == "c":
                consultarDisciplinaID()
            elif sub_opcao == "d":
                relatorioDisciplina()
            elif sub_opcao == "e":
                excluirDisciplina()
            elif sub_opcao == "f":
                atribuirDisciplinaCurso()
            else:
                print("Opção inválida.")

        elif opcao == "4":
            break

        else:
            print("Opção inválida.")

menuPrincipal()