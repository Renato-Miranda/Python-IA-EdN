import json
import os
from datetime import datetime

# funções para carregar e salvar tarefa:
def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json', 'r') as arquivo:
            return json.load(arquivo)
    else: 
        return []

def salvar_terefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

def gerar_id(tarefas):
    if tarefas:
        ultimo_id = tarefas[-1]['id']
        return ultimo_id
    else:
        return 1
    
def adicionar_tarefa(tarefas):
    print('\nAdicionar Nova Tarefa')
    titulo = input("Título: ")
    descricao = input("Descrição: ")
    data_input = input("Data de conclusão (dd/mm/aaaa): ")
    try:
        data_obj = datetime.strptime(data_input, '%d/%m/%Y')
        data = data_obj.strftime('%d/%m/%Y')
        if data_obj.date() < datetime.now().date():
            print("Data de conclusão não pode ser no passado.")
            return
    except ValueError:
        print("Data em formato inválido. Utilize dd/mm/aaaa.")
        return
    
    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'data': data,
        'concluida': False
    }

    tarefas.append(tarefa)
    salvar_terefas(tarefas)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    print("\nTarefas Pendentes: ")
    tarefas_pendentes = [t for t in tarefas if not t['concluida']]
    tarefas_pendentes = sorted(tarefas_pendentes, key=lambda X: datetime.strptime(X['data'], '%d/%m/%Y'))
    for tarefa in tarefas_pendentes:
        print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Data: {tarefa['data']}")

    print("\nTarefas Concluídas:")
    tarefas_concluidas = [t for t in tarefas if t['concluida']]
    tarefas_concluidas = sorted(tarefas_concluidas, key=lambda X: datetime.strptime(X['data'], '%d/%m/%Y'))
    for tarefa in tarefas_concluidas:
        print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Data:{tarefa['data']}")

def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser concluída: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['concluida']:
                    print("A tarefa já está concluída.")
                else:
                    tarefa['concluida'] = True
                    salvar_terefas(tarefas)
                    print("Tarefa concluída com sucesso!")
                return
            print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido.")

def remover_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa a ser revmovida: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                tarefas.remove(tarefa)
                salvar_terefas(tarefas)
                print("Tarefa removida com sucesso!")
                return
        print("Tarefa não encontrada.")
    except ValueError:
        print("ID inválido")

def pesquisar_tarefas(tarefas):
    termo = input("Digite o termo de pesquisa: ").lower()
    resultados = [t for t in tarefas if termo in t['titulo'].lower() or termo in t['descricao'].lower()]
    if resultados:
        print(f"\nTarefas que contêm '{termo}'")
        for tarefa in resultados:
            status = "Concluída" if tarefa['concluida'] else "Pendente"
            print(f"ID: {tarefa['id']}, Título: {tarefa['titulo']}, Status: {status}, Data: {tarefa['data']}")
    else: 
        print("Nenhuma tarefa encontrada com o termo especificado.")

def ordenar_tarefas(tarefas):
    tarefas.sort(key=lambda X: datetime.strptime(X['data'], '%d/%m/%Y'))
    salvar_terefas(tarefas)
    print("Tarefas ordenas por data de conclusão com sucesso!")

def menu():
    print("\n==== Gerenciador de Tarefas Avançado ====")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Concluir Tarefa")
    print("4. Remover Tarefa")
    print("5. Pesquisar Tarefas")
    print("6. Ordenar Tarefas por Data")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            remover_tarefa(tarefas)
        elif opcao == '5':
            pesquisar_tarefas(tarefas)
        elif opcao == '6':
            ordenar_tarefas(tarefas)
        elif opcao == '7':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

