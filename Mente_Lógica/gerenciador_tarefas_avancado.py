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
        
