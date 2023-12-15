tarefas = []  # Lista vazia para armazenar as tarefas

def adicionar_tarefa(titulo, prazo):
    if titulo and prazo:
        nova_tarefa = {'Título': titulo, 'Prazo': prazo, 'Status': 'Pendente'}
        tarefas.append(nova_tarefa)
        return "Tarefa adicionada com sucesso!"
    else:
        return "Erro ao adicionar a tarefa. Preencha o título e o prazo."


def alterar_tarefa(indice, novo_titulo, novo_prazo):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice]['Título'] = novo_titulo
        tarefas[indice]['Prazo'] = novo_prazo
        return "Tarefa alterada com sucesso!"
    else:
        return "Erro ao alterar a tarefa. Índice inválido."


def listar_tarefas():
    if not tarefas:
        return "Não há tarefas cadastradas."

    lista = "Lista de tarefas:\n"
    for i, tarefa in enumerate(tarefas):
        lista += f"Índice: {i}, Título: {tarefa['Título']}, Prazo: {tarefa['Prazo']}, Status: {tarefa['Status']}\n"
    return lista


def deletar_tarefa(indice):
    if indice >= 0 and indice < len(tarefas):
        del tarefas[indice]
        return "Tarefa deletada com sucesso!"
    else:
        return "Erro ao deletar a tarefa. Índice inválido."


def concluir_tarefa(indice):
    if indice >= 0 and indice < len(tarefas):
        tarefas[indice]['Status'] = 'Concluída'
        return "Tarefa marcada como concluída!"
    else:
        return "Erro ao concluir a tarefa. Índice inválido."


def salvar_tarefas():
    with open("tarefas.txt", "w") as arquivo:
        for tarefa in tarefas:
            arquivo.write(f"Título: {tarefa['Título']}, Prazo: {tarefa['Prazo']}, Status: {tarefa['Status']}\n")
        return "Tarefas salvas com sucesso!"
