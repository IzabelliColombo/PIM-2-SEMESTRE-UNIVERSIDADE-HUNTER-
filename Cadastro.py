import json
import os

# Nome do arquivo para salvar as dúvidas
ARQUIVO_DUVIDAS = "duvidas_forum.json"

def carregar_duvidas():
    """Carrega as dúvidas do arquivo JSON"""
    try:
        if os.path.exists(ARQUIVO_DUVIDAS):
            with open(ARQUIVO_DUVIDAS, 'r', encoding='utf-8') as f:
                return json.load(f)
        return []
    except:
        return []

def salvar_duvidas(duvidas):
    """Salva as dúvidas no arquivo JSON"""
    try:
        with open(ARQUIVO_DUVIDAS, 'w', encoding='utf-8') as f:
            json.dump(duvidas, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False

while True:
    print('\033[34m===== SISTEMA ACADÊMICO INTEGRADO =====\033[0m')
    tipo = input("Você é Aluno ou Professor? ").strip().lower()

    # Carrega as dúvidas do arquivo
    duvidas = carregar_duvidas()

    # ------------------- PROFESSOR -------------------
    if tipo == "professor":
        print("\n\033[33m--- Cadastro de Professor ---\033[0m")
        nome = input("Digite seu nome: ")
        materia = input("Digite a disciplina que leciona: ")
        email = input("Digite seu e-mail: ")
        telefone = input("Digite seu telefone: ")

        print(f"\n\033[32mCadastro do Professor {nome} realizado com sucesso!\033[0m")

        # Menu do Professor - FÓRUM POR ÚLTIMO
        while True:
            print("\n\033[36m--- MENU DO PROFESSOR ---\033[0m")
            print("1 - Visualizar turmas")
            print("2 - Fórum de Dúvidas")
            print("3 - Sair")
            
            opcao_prof = input("\nEscolha uma opção: ").strip()
            
            if opcao_prof == "1":
                print(f"\n\033[35m--- TURMAS DO PROFESSOR {nome} ---\033[0m")
                print(f"Disciplina: {materia}")
                print("Turmas atribuídas:")
                print("- Turma A: Segunda e Quarta - 19h às 22h")
                print("- Turma B: Terça e Quinta - 19h às 22h")
                print("- Turma C: Sábado - 8h às 12h")
                
            elif opcao_prof == "2":
                # SUBMENU DO FÓRUM
                while True:
                    print("\n\033[35m--- FÓRUM DE DÚVIDAS ---\033[0m")
                    print("1 - Visualizar dúvidas pendentes")
                    print("2 - Responder dúvidas")
                    print("3 - Visualizar todas as dúvidas")
                    print("4 - Apagar dúvidas respondidas")
                    print("5 - Voltar ao menu anterior")
                    
                    opcao_forum = input("\nEscolha uma opção: ").strip()
                    
                    if opcao_forum == "1":
                        print("\n\033[35m--- DÚVIDAS PENDENTES ---\033[0m")
                        duvidas_pendentes = [d for d in duvidas if not d['respondida']]
                        
                        if not duvidas_pendentes:
                            print("Nenhuma dúvida pendente.")
                        else:
                            for i, duvida in enumerate(duvidas_pendentes, 1):
                                print(f"{i} - [{duvida['materia']}] {duvida['aluno']}: {duvida['pergunta']}")
                                
                    elif opcao_forum == "2":
                        print("\n\033[35m--- RESPONDER DÚVIDAS ---\033[0m")
                        duvidas_pendentes = [d for d in duvidas if not d['respondida']]
                        
                        if not duvidas_pendentes:
                            print("Nenhuma dúvida pendente para responder.")
                        else:
                            for i, duvida in enumerate(duvidas_pendentes, 1):
                                print(f"{i} - [{duvida['materia']}] {duvida['aluno']}: {duvida['pergunta']}")
                            
                            escolha = input("\nDigite o número da dúvida que deseja responder: ").strip()
                            
                            if escolha.isdigit() and 1 <= int(escolha) <= len(duvidas_pendentes):
                                resposta = input("Digite sua resposta: ")
                                duvida_index = duvidas.index(duvidas_pendentes[int(escolha)-1])
                                duvidas[duvida_index]['resposta'] = resposta
                                duvidas[duvida_index]['professor'] = nome
                                duvidas[duvida_index]['respondida'] = True
                                
                                # SALVA AS ALTERAÇÕES NO ARQUIVO
                                if salvar_duvidas(duvidas):
                                    print("\033[32mResposta enviada e salva com sucesso!\033[0m")
                                    
                                    # Pergunta se deseja apagar a dúvida após responder
                                    apagar = input("Deseja apagar esta dúvida do fórum? (s/n): ").strip().lower()
                                    if apagar == 's':
                                        duvida_apagada = duvidas.pop(duvida_index)
                                        if salvar_duvidas(duvidas):
                                            print("\033[32mDúvida apagada com sucesso!\033[0m")
                                        else:
                                            print("\033[33mErro ao apagar a dúvida.\033[0m")
                                else:
                                    print("\033[33mResposta enviada, mas houve um erro ao salvar.\033[0m")
                            else:
                                print("\033[31mOpção inválida!\033[0m")
                                
                    elif opcao_forum == "3":
                        print("\n\033[35m--- TODAS AS DÚVIDAS ---\033[0m")
                        if not duvidas:
                            print("Nenhuma dúvida cadastrada.")
                        else:
                            for i, duvida in enumerate(duvidas, 1):
                                status = "✓ Respondida" if duvida['respondida'] else "⏳ Pendente"
                                print(f"\n{i} - [{duvida['materia']}] {duvida['aluno']} - {status}")
                                print(f"   Pergunta: {duvida['pergunta']}")
                                if duvida['respondida']:
                                    print(f"   Resposta ({duvida['professor']}): {duvida['resposta']}")
                                    
                    elif opcao_forum == "4":
                        print("\n\033[35m--- APAGAR DÚVIDAS RESPONDIDAS ---\033[0m")
                        duvidas_respondidas = [d for d in duvidas if d['respondida']]
                        
                        if not duvidas_respondidas:
                            print("Nenhuma dúvida respondida para apagar.")
                        else:
                            print("Dúvidas respondidas encontradas:")
                            for i, duvida in enumerate(duvidas_respondidas, 1):
                                print(f"{i} - [{duvida['materia']}] {duvida['aluno']}: {duvida['pergunta'][:50]}...")
                            
                            print("\nOpções:")
                            print("1 - Apagar dúvida específica")
                            print("2 - Apagar TODAS as dúvidas respondidas")
                            print("3 - Cancelar")
                            
                            opcao_apagar = input("\nEscolha uma opção: ").strip()
                            
                            if opcao_apagar == "1":
                                escolha = input("Digite o número da dúvida que deseja apagar: ").strip()
                                if escolha.isdigit() and 1 <= int(escolha) <= len(duvidas_respondidas):
                                    duvida_apagar = duvidas_respondidas[int(escolha)-1]
                                    duvidas.remove(duvida_apagar)
                                    if salvar_duvidas(duvidas):
                                        print("\033[32mDúvida apagada com sucesso!\033[0m")
                                    else:
                                        print("\033[33mErro ao salvar as alterações.\033[0m")
                                else:
                                    print("\033[31mOpção inválida!\033[0m")
                                    
                            elif opcao_apagar == "2":
                                confirmacao = input("Tem certeza que deseja apagar TODAS as dúvidas respondidas? (s/n): ").strip().lower()
                                if confirmacao == 's':
                                    # Mantém apenas as dúvidas não respondidas
                                    duvidas = [d for d in duvidas if not d['respondida']]
                                    if salvar_duvidas(duvidas):
                                        print(f"\033[32mTodas as dúvidas respondidas foram apagadas! {len(duvidas_respondidas)} dúvidas removidas.\033[0m")
                                    else:
                                        print("\033[33mErro ao salvar as alterações.\033[0m")
                                else:
                                    print("Operação cancelada.")
                                    
                            elif opcao_apagar == "3":
                                print("Operação cancelada.")
                            else:
                                print("\033[31mOpção inválida!\033[0m")
                                    
                    elif opcao_forum == "5":
                        break
                    else:
                        print("\033[31mOpção inválida!\033[0m")
                            
            elif opcao_prof == "3":
                print("\033[32mSaindo do sistema...\033[0m")
                break
            else:
                print("\033[31mOpção inválida!\033[0m")

    # ------------------- ALUNO -------------------
    elif tipo == "aluno":
        print("\n\033[33m--- Cadastro de Aluno ---\033[0m")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        ra = input("Digite seu RA: ")

        print("\n\033[36mCursos disponíveis:\033[0m")
        print("1 - ADS (Análise e Desenvolvimento de Sistemas)")
        print("2 - Engenharia de Software")
        print("3 - Ciência da Computação")

        opcao = input("Digite o número do seu curso: ").strip()

        if opcao == "1":
            curso = "ADS"
            materias = ["Lógica de Programação", "Banco de Dados I", "Python para Iniciantes"]
            turmas = [
                {"Código": "ADS01", "Matéria": "Lógica de Programação", "Horário": "Segunda e Quarta - 19h às 22h", "Sala": "Lab 1"},
                {"Código": "ADS02", "Matéria": "Banco de Dados I", "Horário": "Terça e Quinta - 19h às 22h", "Sala": "Lab 2"},
                {"Código": "ADS03", "Matéria": "Python para Iniciantes", "Horário": "Sábado - 8h às 12h", "Sala": "Lab 3"}
            ]
        elif opcao == "2":
            curso = "Engenharia de Software"
            materias = ["Análise de Requisitos", "Modelagem de Sistemas", "Gestão de Projetos Ágeis"]
            turmas = [
                {"Código": "ES01", "Matéria": "Análise de Requisitos", "Horário": "Segunda e Quarta - 19h às 22h", "Sala": "Sala 201"},
                {"Código": "ES02", "Matéria": "Modelagem de Sistemas", "Horário": "Terça e Quinta - 19h às 22h", "Sala": "Sala 202"},
                {"Código": "ES03", "Matéria": "Gestão de Projetos Ágeis", "Horário": "Sábado - 8h às 12h", "Sala": "Sala 203"}
            ]
        elif opcao == "3":
            curso = "Ciência da Computação"
            materias = ["Algoritmos Avançados", "Inteligência Artificial", "Computação Gráfica"]
            turmas = [
                {"Código": "CC01", "Matéria": "Algoritmos Avançados", "Horário": "Segunda e Quarta - 19h às 22h", "Sala": "Lab 5"},
                {"Código": "CC02", "Matéria": "Inteligência Artificial", "Horário": "Terça e Quinta - 19h às 22h", "Sala": "Lab 6"},
                {"Código": "CC03", "Matéria": "Computação Gráfica", "Horário": "Sábado - 8h às 12h", "Sala": "Lab 7"}
            ]
        else:
            print("\033[31mOpção de curso inválida!\033[0m")
            continue

        email = input("Digite seu e-mail: ")
        telefone = input("Digite seu telefone: ")

        print(f"\n\033[32mCadastro do Aluno {nome} ({curso}) realizado com sucesso!\033[0m")

        # VISUALIZAÇÃO DE TURMAS PRIMEIRO
        print("\n\033[36m--- TURMAS DISPONÍVEIS ---\033[0m")
        for i, turma in enumerate(turmas, 1):
            print(f"{i} - {turma['Código']} | {turma['Matéria']}")

        escolha = input("\nDigite o número da turma que deseja visualizar: ").strip()

        if escolha.isdigit() and 1 <= int(escolha) <= len(turmas):
            turma_selecionada = turmas[int(escolha) - 1]
            print("\n\033[35m--- DETALHES DA TURMA ---\033[0m")
            print(f"Código: {turma_selecionada['Código']}")
            print(f"Matéria: {turma_selecionada['Matéria']}")
            print(f"Horário: {turma_selecionada['Horário']}")
            print(f"Sala: {turma_selecionada['Sala']}")
        else:
            print("\033[31mOpção de turma inválida!\033[0m")

        # Menu do Aluno - FÓRUM POR ÚLTIMO
        while True:
            print("\n\033[36m--- MENU DO ALUNO ---\033[0m")
            print("1 - Visualizar minhas turmas")
            print("2 - Fórum de Dúvidas")
            print("3 - Sair")
            
            opcao_aluno = input("\nEscolha uma opção: ").strip()
            
            if opcao_aluno == "1":
                print("\n\033[35m--- MINHAS TURMAS ---\033[0m")
                print(f"Aluno: {nome}")
                print(f"Curso: {curso}")
                print(f"RA: {ra}")
                print("\nTurmas matriculadas:")
                for turma in turmas:
                    print(f"- {turma['Código']}: {turma['Matéria']}")
                    print(f"  Horário: {turma['Horário']}")
                    print(f"  Sala: {turma['Sala']}\n")
                    
            elif opcao_aluno == "2":
                # SUBMENU DO FÓRUM
                while True:
                    print("\n\033[35m--- FÓRUM DE DÚVIDAS ---\033[0m")
                    print("1 - Fazer uma pergunta")
                    print("2 - Visualizar minhas dúvidas")
                    print("3 - Visualizar todas as dúvidas do fórum")
                    print("4 - Voltar ao menu anterior")
                    
                    opcao_forum = input("\nEscolha uma opção: ").strip()
                    
                    if opcao_forum == "1":
                        print("\n\033[35m--- FAZER PERGUNTA ---\033[0m")
                        print("Matérias disponíveis:")
                        for i, materia in enumerate(materias, 1):
                            print(f"{i} - {materia}")
                        
                        escolha_materia = input("\nDigite o número da matéria: ").strip()
                        
                        if escolha_materia.isdigit() and 1 <= int(escolha_materia) <= len(materias):
                            pergunta = input("Digite sua dúvida: ")
                            
                            nova_duvida = {
                                'aluno': nome,
                                'ra': ra,
                                'materia': materias[int(escolha_materia)-1],
                                'pergunta': pergunta,
                                'respondida': False,
                                'resposta': '',
                                'professor': ''
                            }
                            
                            duvidas.append(nova_duvida)
                            # SALVA A NOVA DÚVIDA NO ARQUIVO
                            if salvar_duvidas(duvidas):
                                print("\033[32mDúvida enviada e salva com sucesso! Aguarde a resposta do professor.\033[0m")
                            else:
                                print("\033[33mDúvida enviada, mas houve um erro ao salvar.\033[0m")
                        else:
                            print("\033[31mOpção de matéria inválida!\033[0m")
                            
                    elif opcao_forum == "2":
                        print("\n\033[35m--- MINHAS DÚVIDAS ---\033[0m")
                        minhas_duvidas = [d for d in duvidas if d['aluno'] == nome]
                        
                        if not minhas_duvidas:
                            print("Você ainda não fez nenhuma pergunta.")
                        else:
                            for i, duvida in enumerate(minhas_duvidas, 1):
                                status = "✓ Respondida" if duvida['respondida'] else "⏳ Aguardando resposta"
                                print(f"\n{i} - [{duvida['materia']}] - {status}")
                                print(f"   Pergunta: {duvida['pergunta']}")
                                if duvida['respondida']:
                                    print(f"   Resposta ({duvida['professor']}): {duvida['resposta']}")
                                    
                    elif opcao_forum == "3":
                        print("\n\033[35m--- TODAS AS DÚVIDAS DO FÓRUM ---\033[0m")
                        if not duvidas:
                            print("Nenhuma dúvida cadastrada no fórum.")
                        else:
                            for i, duvida in enumerate(duvidas, 1):
                                status = "✓ Respondida" if duvida['respondida'] else "⏳ Pendente"
                                print(f"\n{i} - {duvida['aluno']} [{duvida['materia']}] - {status}")
                                print(f"   Pergunta: {duvida['pergunta']}")
                                if duvida['respondida']:
                                    print(f"   Resposta ({duvida['professor']}): {duvida['resposta']}")
                                    
                    elif opcao_forum == "4":
                        break
                    else:
                        print("\033[31mOpção inválida!\033[0m")
                            
            elif opcao_aluno == "3":
                print("\033[32mSaindo do sistema...\033[0m")
                break
            else:
                print("\033[31mOpção inválida!\033[0m")

    # ------------------- ERRO -------------------
    else:
        print("\n\033[31mOpção inválida! Digite 'Aluno' ou 'Professor'.\033[0m")
    
    # Pergunta se deseja continuar no sistema
    continuar = input("\nDeseja voltar ao menu principal? (s/n): ").strip().lower()
    if continuar != 's':
        print("\033[34mObrigado por usar o Sistema Acadêmico Integrado!\033[0m")
        break