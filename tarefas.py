# Lista para armazenar as tarefas
lista_de_tarefas = []

# Função para add nova tarefa à lista
def adicionar_tarefa(titulo, prazo):
    if titulo.strip() != "" and prazo.strip() != "":
        nova_tarefa = {'Título': titulo, 'Prazo': prazo, 'Status': 'Pendente'}
        lista_de_tarefas.append(nova_tarefa)
        return "Tarefa adicionada com sucesso!"
    else:
        return "Erro: Título e prazo são campos obrigatórios e devem ser preenchidos."

# Função alterar uma tarefa existente
def alterar_tarefa(indice, novo_titulo, novo_prazo):
    if indice >= 0 and indice < len(lista_de_tarefas):
        lista_de_tarefas[indice]['Título'] = novo_titulo
        lista_de_tarefas[indice]['Prazo'] = novo_prazo
        return "Tarefa alterada com sucesso!"
    else:
        return "Erro: Índice inválido para alteração."

# Função list tarefas
def listar_tarefas():
    lista_formatada = ""
    for indice, tarefa in enumerate(lista_de_tarefas):
        lista_formatada += f"Índice: {indice} - Título: {tarefa['Título']}, Prazo: {tarefa['Prazo']}, Status: {tarefa['Status']}\n"
    return lista_formatada

# Função del tarefa
def deletar_tarefa(indice):
    if indice >= 0 and indice < len(lista_de_tarefas):
        del lista_de_tarefas[indice]
        return "Tarefa deletada com sucesso!"
    else:
        return "Erro: Índice inválido para exclusão."
