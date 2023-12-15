import tarefas
import tkinter as tk
from tkinter import simpledialog, messagebox


def adicionar():
    titulo = simpledialog.askstring("Adicionar Tarefa", "Digite o título da tarefa:")
    prazo = simpledialog.askstring("Adicionar Tarefa", "Digite o prazo da tarefa (dd/mm/aaaa):")
    resultado = tarefas.adicionar_tarefa(titulo, prazo)
    messagebox.showinfo("Resultado", resultado)


def alterar():
    indice = simpledialog.askinteger("Alterar Tarefa", "Digite o índice da tarefa que deseja alterar:")
    novo_titulo = simpledialog.askstring("Alterar Tarefa", "Digite o novo título da tarefa:")
    novo_prazo = simpledialog.askstring("Alterar Tarefa", "Digite o novo prazo da tarefa (dd/mm/aaaa):")
    resultado = tarefas.alterar_tarefa(indice, novo_titulo, novo_prazo)
    messagebox.showinfo("Resultado", resultado)


def listar():
    lista = tarefas.listar_tarefas()
    messagebox.showinfo("Lista de Tarefas", lista)


def deletar():
    indice = simpledialog.askinteger("Deletar Tarefa", "Digite o índice da tarefa que deseja deletar:")
    resultado = tarefas.deletar_tarefa(indice)
    messagebox.showinfo("Resultado", resultado)


def menu():
    root = tk.Tk()
    root.withdraw()

    opcoes = {
        1: adicionar,
        2: alterar,
        3: listar,
        4: deletar,
        5: exit
    }

    while True:
        escolha = simpledialog.askinteger("Menu",
                                          "Escolha uma opção:\n1. Adicionar Tarefa\n2. Alterar Tarefa\n3. Listar Tarefas\n4. Deletar Tarefa\n5. Sair")
        if escolha in opcoes:
            opcoes[escolha]()
        else:
            messagebox.showwarning("Opção inválida", "Escolha uma opção válida.")


if __name__ == "__main__":
    menu()
