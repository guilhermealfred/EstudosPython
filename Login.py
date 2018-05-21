# -*- coding: utf-8 -*-
from tkinter import *
import shelve
class program:
	def __init__(self,app):
		self.log = Label(app,text='Login')
		self.log.pack()
		self.user = Entry(app)
		self.user.pack()
		self.sen = Label(app,text='Senha')
		self.sen.pack()
		self.senha = Entry(app,show='*')
		self.senha.pack()
		self.entra = Button(app,text='Entrar',command=self.login)
		self.entra.pack(side= LEFT)
		self.novo = Button(app,text='Novo',command=self.novo)
		self.novo.pack(side=RIGHT)
		with shelve.open('users.db') as users:
			users['user'] = ''
			users['senha'] = ''
	def criar(self):
		with shelve.open('users.db') as users:
			if len(self.user.get()) > 0 and len(self.senha.get()) >0:
				if self.user.get() not in users['user']:
					users['user'] = self.user.get()
					users['senha'] = self.senha.get()
					self.result = Label(app,text='Usuário criado',fg='green')
					self.result.pack()
				else:
					self.result = Label(app,text='Usuário já existe',fg='red')
					self.result.pack()
			else:
				self.result = Label(app,text='Preencha todos campos')
				self.result.pack()
	def novo(self):
		self.log['fg'] = 'green'
		self.sen['fg'] = 'green'
		self.novo['text'] = 'Criar'
		self.novo['command'] = self.criar
	def login(self):
		with shelve.open('users.db') as users:
			if len(self.user.get()) > 0 and len(self.senha.get()) >0:
				if self.user.get() in users['user'] and self.senha.get() in users['senha']:
					self.result= Label(app,text=f'Bem vindo {self.user.get()}',fg='blue')
					self.result.pack()
				else:
					self.result = Label(app,text='Acesso negado',fg='red')
					self.result.pack()
			else:
				self.result = Label(app,text='Preencha todos os campos',fg='red')
				self.result.pack()
app = Tk()
app.geometry('200x200')
app.title('Login')
program(app)
app.mainloop()
