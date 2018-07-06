# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
from tkinter import *
from PIL import Image
import urllib.request
import os
class scraping(object):
	def __init__(self):
		self.tela = Tk()
		self.tela.title('Scraping Twitter')
		self.tela.geometry('400x400+400+200')
		self.tela.resizable(False,False)
		self.tela['bg'] = '#61f2cf'
		self.framelink = Frame(self.tela)
		self.framelink.pack()
		self.alert = Label(self.tela,fg='red',bg='#61f2cf',font=('Ubuntu Condensed',12))
		self.alert.pack()
		self.lblink = Label(self.framelink,text='Link',font=('Ubuntu Condensed',12),padx = 25)
		self.lblink.pack(side=LEFT)
		self.frameimg = Frame(self.tela,pady = 10,bg='#61f2cf')
		self.frameimg.pack()
		self.link = Entry(self.framelink,width=40)
		self.link.focus_force()
		self.link.insert(END,'https://twitter.com/')
		self.link.bind('<Return>',self.handle)
		self.link.pack(side=LEFT)
		self.tela.mainloop()
	@property
	def get_tweets(self):
		try:
			self.tweets = self.soup.find('a',class_="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-nav")
			return self.tweets.get('title')
		except:
			return 'Não tem nenhum tweet'
	@property
	def get_following(self):
		try:
			self.fl = self.soup.find('li',class_='ProfileNav-item ProfileNav-item--following')
			self.following = self.fl.find('a',class_="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor").get('title').split()
			return str(self.following[1].replace('s','S')) + ' ' + str(self.following[0]) + ' pessoas'
		except:
			return 'Não segue nenhum perfil'
	@property 
	def get_followers(self):
		try:
			self.flo = self.soup.find('li',class_='ProfileNav-item ProfileNav-item--followers')
			self.followers = self.flo.find('a',class_="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor").get('title')
			return self.followers
		except:
			return 'Não possui seguidores'
	@property
	def get_photos(self):
		try:
			self.ph = self.soup.find('a',class_='PhotoRail-headingWithCount js-nav')
			if self.ph.text.strip() == '0 Foto ou vídeo':
				return 'Não possui fotos/vídeos'
			return ' '* 15 + self.ph.text.lstrip()
		except:
			pass
	def handle(self,event):
		try:
			self.site = urllib.request.urlopen(self.link.get()).read()
			self.soup = bs(self.site,'lxml')
			try:
				if self.soup.find('input',value="app/pages/profile/highline_landing") != None:
					self.download()
				else:
					raise	
			except:
				raise 
		except Exception as e:
			self.alert['text'] = 'Perfil Inválido!.Formato de entrada : https://twitter.com/perfil'
			print(e)
	def download(self):
		try:
			img = self.soup.find('img',class_='ProfileAvatar-image ').get('src')
			urllib.request.urlretrieve(img,'img.png')
		except:
			urllib.request.urlretrieve('https://abs.twimg.com/a/1527200258/img/t1/highline/empty_state/owner_empty_avatar.png','img.png')
		finally:
			self.handle_image()
	def handle_image(self):
		image = Image.open('img.png')
		new_img = image.resize((150,150))
		new_img.save('perfil.gif')
		self.photo = PhotoImage(file='perfil.gif')
		self.save = self.photo
		self.organize()
	def organize(self):
		self.alert.pack_forget()
		self.lblink.pack_forget()
		self.link.pack_forget()
		self.framelink.pack_forget()
		self.tela.title(f'Perfil-@{self.soup.find("b",class_="u-linkComplex-target").text}')
		self.lb = Label(self.frameimg,image=self.photo,bg='#61f2cf')
		self.lb.pack()
		os.system('rm img.png')
		os.system('rm perfil.gif')
		self.frameinfo = Frame(self.tela,bg='#61f2cf')
		self.frameinfo.pack()

		lista = [self.get_following,self.get_followers,self.get_photos,self.get_tweets]
		for i in lista:
			self.lbi = Label(self.frameinfo,text=i,font=('Ubuntu Condensed',12),fg='#4c4c4c',bg='#61f2cf')
			self.lbi.pack()
		self.framebt = Frame(self.tela,pady=30,bg='#61f2cf')
		self.framebt.pack(side=BOTTOM)
		self.again = Button(self.framebt,text='Scrapar denovo',width=13,bg='#61f2cf',borderwidth=0,command=self.dnv,font=('Ubuntu Condensed',12),fg='black')
		self.again.pack()
	def dnv(self):
		self.tela.destroy()
		scraping()
