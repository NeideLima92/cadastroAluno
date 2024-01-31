from tkinter import *
from tkinter import ttk
from tkinter import messagebox

matrícula_atual=1
index=0

def atualizarTabela () -> None:
    for linha in tabela.get_children():
        tabela.delete(linha)
    for aluno in alunos:
        tabela.insert("",END, values=(aluno["matricula"],
                                            aluno["nome"],
                                            aluno["idade"],
                                            aluno["curso"],
                                            aluno["novato"],))



alunos=[
    {
    "matricula":1,
    "nome": "Neide Lima",
    "idade": 18,
    "curso":"Pyton",
    "novato":False
    }
]
def adicionarAluno() -> None:
    global matrícula_atual
    matrícula_atual+=1
    nome= txtNome.get()
    idade= int(txtIdade.get())
    curso = comboCursos.get()
    novato= opcao.get()

    aluno={
        "matricula":matrícula_atual,
        "nome": nome,
        "idade": idade,
        "curso": curso,
        "novato": novato,

    }
    messagebox.showinfo("Sucesso!","Aluno adicionado com sucesso!")
    alunos.append(aluno)
    limparCampos()
    atualizarTabela()

def limparCampos()-> None:
    txtMatrícula.config(state=NORMAL)
    txtMatrícula.delete(0,END)
    txtMatrícula.config(state=DISABLED)
    txtNome.delete(0, END)
    txtIdade.delete(0, END)
    comboCursos.set("")
    opcao.set(False)

def preencherCampos(event) -> None:
    linhaSelecionada=tabela.selection()
    global index
    index = tabela.index(linhaSelecionada)
    aluno=alunos[index]
    limparCampos()
    txtMatrícula.config(state=NORMAL)
    txtMatrícula.insert(END, str(aluno["matricula"]))
    txtMatrícula.config(state=DISABLED)
    txtNome.insert(END, aluno["nome"])
    txtIdade.insert(END, str(aluno["idade"]))
    comboCursos.set(aluno["curso"])


def editarAluno() -> None:

    nome = txtNome.get()
    idade = int(txtIdade.get())
    curso = comboCursos.get()
    novato = opcao.get()

    opcaoSelecionada = messagebox.askyesno("Confirmação de alteração!","Deseja Alterar Os dados!")
    if opcaoSelecionada:
        aluno = alunos[index]
        aluno["nome"] = nome
        aluno["idade"] = idade
        aluno["curso"] = curso
        aluno["novato"] = novato
        messagebox.showinfo("Sucesso!", "Dados alterados com sucesso!")
    limparCampos()
    atualizarTabela()

def deletarAluno () -> None:
    opcaoSelecionada = messagebox.askyesno("Confirmação de alteração!","Deseja remover os dados!")
    if opcaoSelecionada:
        alunos.remove(alunos[index])
        messagebox.showinfo("Sucesso!", "Dados removidos com sucesso!")
    limparCampos()
    atualizarTabela()


janela = Tk()

janela.title("Alunos - Infinity")

labelAnuncio= Label(janela, text="Alunos - Infinity", font="Calibri 16 bold", fg="Indigo")
labelAnuncio.grid(row=0, column=0)

labelMatricula= Label(janela, text="Matrícula:",font="Calibri 14 bold", fg="black")
labelMatricula.grid(row=1, column=0,sticky=W)
txtMatrícula = Entry(janela, font="Calibri 14", fg="black", state=DISABLED)
txtMatrícula.grid(row=1, column=1,sticky=W)

labelNome = Label(janela, text="Nome:",font="Calibri 14 bold", fg="black")
labelNome.grid(row=2, column=0,sticky=W)
txtNome = Entry(janela, font="Calibri 14", fg="black")
txtNome.grid(row=2, column=1, sticky=W)

labelIdade = Label(janela, text="Idade:",font="Calibri 14 bold", fg="black")
labelIdade.grid(row=3, column=0,sticky=W)
txtIdade = Entry(janela, font="Calibri 14", fg="black")
txtIdade.grid(row=3, column=1,sticky=W)

labelCurso = Label(janela, text="Curso:", font="Calibri 14 bold", fg="Black")
labelCurso.grid(row=4, column=0, sticky=W)

cursos = ["JavaScript", "Pyton", "React", "NodeJs"]

comboCursos = ttk.Combobox(janela, font="Calibri 14 bold", values=cursos, width=18)
comboCursos.grid(row=4, column=1, sticky=W)

labelNovato = Label(janela, text="Novo aluno?", font="Calibri 14 bold", fg="Black")
labelNovato.grid(row=5, column=0, sticky=W)

opcao=BooleanVar(value=False)
checkNovato = ttk.Checkbutton(janela, text="Marcar apenas para novos alunos", variable=opcao)
checkNovato.grid(row=5, column=1, sticky=W)

btnAdicionar= Button(janela, text="Adicionar", font="Calibri 12 bold", fg="Black",
                     background="PaleGoldenrod",width=10, command=adicionarAluno)
btnAdicionar.grid(row=6, column=0)

btnEditar= Button(janela, text="Editar", font="Calibri 12 bold", fg="Black",
                     background="PaleGoldenrod", width=10, command=editarAluno)
btnEditar.grid(row=6, column=1)

btnExcluir= Button(janela, text="Excluir", font="Calibri 12 bold", fg="Black",
                     background="PaleGoldenrod",width=10, command=deletarAluno)
btnExcluir.grid(row=6, column=2)

colunas=["Matricula", "Nome", "Idade", "Curso", "Novato?"]
tabela = ttk.Treeview(janela, columns=colunas, show="headings")
for coluna in colunas:
    tabela.heading(coluna, text=coluna)
    tabela.column(coluna, width=110)
tabela.grid(row=7, columnspan=3)
atualizarTabela()
tabela.bind("<ButtonRelease-1>",preencherCampos)
janela.mainloop()
