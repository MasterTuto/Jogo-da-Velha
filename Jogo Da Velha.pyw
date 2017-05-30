# -*- coding: utf-8 -*-

import Tkinter as tk
import tkMessageBox

pontos1 = 0
pontos2 = 0
janela = tk.Tk()
vez = "O"

class Comeco():
	def __init__(self):
		pass

	def salvar_nome_dos_jogadores(self):
		if self.num == 0:
			self.j1['text'] = "Jogador 2 (X): "
			self.lista.append(self.j1e.get())
			self.j1e.delete("0", 'end')
			self.num += 1
		elif self.num == 1:
			self.lista.append(self.j1e.get())
			self.j1e.destroy()
			self.j1.destroy()
			self.botao.destroy()
			botoes(self.lista)

	def nome_dos_jogadores(self):
		lista = []
		num = 0
		j1 = tk.Label(janela, text="Jogador 1 (O): ")
		j1e = tk.Entry(janela)
		j1e.grid(row=1, column=2)
		j1.grid(row=1, column=1)
		
		self.j1e = j1e
		self.j1 = j1
		self.num = num
		self.lista = lista

		botao = tk.Button(janela, text="Enviar", command=self.salvar_nome_dos_jogadores)
		botao.grid(row=1, column=3)

		self.botao = botao



instancia_de_comeco = Comeco()
instancia_de_comeco.nome_dos_jogadores()

def marcar(botao, lista_de_entries, users, vez_de):
	global vez
	
	if users[0] == '':
		users[0] = "Jogador 1"

	if users[1] == '':
		users[1] = "Jogador 2"

	if lista_de_entries[botao].cget('text') == '   ':
		if vez == "O":
			vez_de['text'] = "Vez de "+users[1]
		elif vez == "X":
			vez_de['text'] = "Vez de "+users[0]
		lista_de_entries[botao].configure(text=vez)
		if vez == "O":
			vez = "X"
		elif vez == "X":
			vez = "O"
	else:
		tkMessageBox.showwarning("Atenção!", "Já subescrito!")

	verificar(lista_de_entries, users[0], users[1])

def verificar(lista_de_entries, jogador1, jogador2):
	def acertou(jogador1, jogador2, x_or_o):
		global pontos1, pontos2
		if x_or_o == "X":
			pontos2 += 1
			tkMessageBox.showwarning("Vencedor", "{} ganhou!".format(jogador2))
			lista_de_entries[10].configure(text="{}: {} ponto(s)".format(jogador2, str(pontos2)))
		elif x_or_o == "O":
			pontos1 += 1
			tkMessageBox.showwarning("Vencedor", "{} ganhou!".format(jogador1))
			lista_de_entries[9].configure(text="{}: {} ponto(s)".format(jogador1, str(pontos1)))
		elif x_or_o == "velha":
			tkMessageBox.showerror("Erro", "Deu velha!")

		for i in range(0, len(lista_de_entries)):
			if i < 9:
				lista_de_entries[i].configure(state="disable")

	a1 = lista_de_entries[0].cget("text")
	a2 = lista_de_entries[1].cget("text")
	a3 = lista_de_entries[2].cget("text")
	b1 = lista_de_entries[3].cget("text")
	b2 = lista_de_entries[4].cget("text")
	b3 = lista_de_entries[5].cget("text")
	c1 = lista_de_entries[6].cget("text")
	c2 = lista_de_entries[7].cget("text")
	c3 = lista_de_entries[8].cget("text")

	if a1 == a2 == a3 == "X" or a1 == a2 == a3 == "O":
		if a1 == a2 == a3 == "X":
			acertou(jogador1, jogador2, "X")
		elif a1 == a2 == a3 == "O":
			acertou(jogador1, jogador2, "O")

	elif b1 == b2 == b3 == "X" or b1 == b2 == b3 == "O":
		if b1 == b2 == b3 == "X":
			acertou(jogador1, jogador2, "X")
		elif b1 == b2 == b3 == "O":
			acertou(jogador1, jogador2, "O")

	elif c1 == c2 == c3 == "X" or c1 == c2 == c3 == "O":
		if c1 == c2 == c3 == "X":
			acertou(jogador1, jogador2, "X")
		elif c1 == c2 == c3 == "O":
			acertou(jogador1, jogador2, "O")

	elif a1 == b1 == c1 == "X" or a1 == b1 == c1 == "O":
		if a1 == b1 == c1 == "X":
			acertou(jogador1, jogador2, "X")
		elif a1 == b1 == c1 == "O":
			acertou(jogador1, jogador2, "O")

	elif a2 == b2 == c2 == "X" or a2 == b2 == c2 == "O":
		if a2 == b2 == c2 == "X":
			acertou(jogador1, jogador2, "X")
		elif a2 == b2 == c2 == "O":
			acertou(jogador1, jogador2, "O")

	elif a3 == b3 == c3 == "X" or a3 == b3 == c3 == "O":
		if a3 == b3 == c3 == "X":
			acertou(jogador1, jogador2, "X")
		elif a3 == b3 == c3 == "O":
			acertou(jogador1, jogador2, "O")

	elif a1 == b2 == c3 == "X" or a1 == b2 == c3 == "O":
		if a1 == b2 == c3 == "X":
			acertou(jogador1, jogador2, "X")
		elif a1 == b2 == c3 == "O":
			acertou(jogador1, jogador2, "O")

	elif a3 == b2 == c1 == "X" or a3 == b2 == c1 == "O":
		if a3 == b2 == c1 == "X":
			acertou(jogador1, jogador2, "X")
		elif a3 == b2 == c1 == "O":
			acertou(jogador1, jogador2, "O")

	testes = [a1, a2, a3, b1, b2, b3, c1, c2, c3]
	velha = 0
	for i in testes:
		if i != "   ":
			velha += 1
	if velha == 9:
		acertou(jogador1, jogador2, "velha")


	
def botoes(lista):
	if lista[0] == '':
		lista[0] = "Jogador 1"

	if lista[1] == '':
		lista[1] = "Jogador 2"

	vez_de = tk.Label(janela, text="Vez de "+lista[0])
	vez_de.grid(row=1, column=4)
	
	users = lista

	A1 = tk.Button(janela, text="   ", command=lambda: marcar(0, lista_de_entries, users, vez_de))
	A1.grid(row=2, column=1)
	A2 = tk.Button(janela, text="   ", command=lambda: marcar(1, lista_de_entries, users, vez_de))
	A2.grid(row=2, column=2)
	A3 = tk.Button(janela, text="   ", command=lambda: marcar(2, lista_de_entries, users, vez_de))
	A3.grid(row=2, column=3)

	B1 = tk.Button(janela, text="   ", command=lambda: marcar(3, lista_de_entries, users, vez_de))
	B1.grid(row=3, column=1)
	B2 = tk.Button(janela, text="   ", command=lambda: marcar(4, lista_de_entries, users, vez_de))
	B2.grid(row=3, column=2)
	B3 = tk.Button(janela, text="   ", command=lambda: marcar(5, lista_de_entries, users, vez_de))
	B3.grid(row=3, column=3)

	C1 = tk.Button(janela, text="   ", command=lambda: marcar(6, lista_de_entries, users, vez_de))
	C1.grid(row=4, column=1)
	C2 = tk.Button(janela, text="   ", command=lambda: marcar(7, lista_de_entries, users, vez_de))
	C2.grid(row=4, column=2)
	C3 = tk.Button(janela, text="   ", command=lambda: marcar(8, lista_de_entries, users, vez_de))
	C3.grid(row=4, column=3)

	placar1 = tk.Label(janela, text="")
	placar1.grid(row=2, column=4)

	placar2 = tk.Label(janela, text="")
	placar2.grid(row=3, column=4)

	lista_de_entries = [A1, A2, A3, B1, B2, B3, C1, C2, C3, placar1, placar2]

	def resetar():
		for i in range(0, len(lista_de_entries)):
			if i < 9:
				lista_de_entries[i].configure(text="   ")
				lista_de_entries[i].configure(state="normal")

	reset = tk.Button(janela, text="Resetar", command=resetar)
	reset.grid(row=4, column=4)


janela.mainloop()
