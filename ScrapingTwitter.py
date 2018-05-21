# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import urllib.request
import os
class Twitter:
	def __init__(self,url):
		self.base = urllib.request.urlopen(url)
		self.soup = bs(self.base,'lxml')
		self.url = url
		self.arroba = '@'+self.soup.find('b',class_='u-linkComplex-target').text
	@property
	def getdsc(self):
		self.dsc = self.soup.find('p',class_='ProfileHeaderCard-bio u-dir')
		return self.dsc.text
	@property
	def info(self):
		self.dic = {}
		self.dic['tweets'] = self.soup.find('span',class_='ProfileNav-value').get('data-count')
		self.dic['following'] = self.soup.find_all('span',class_='ProfileNav-value')[1].get('data-count')
		self.dic['followers'] = self.soup.find_all('span',class_='ProfileNav-value')[2].get('data-count')
		self.dic['likes'] = self.soup.find_all('span',class_='ProfileNav-value')[3].get('data-count')
		self.dic['created'] = self.soup.find('span',class_='ProfileHeaderCard-joinDateText js-tooltip u-dir').get('title')
		return self.dic
	def save_info(self):
		try:
			os.mkdir(f'{self.arroba}')
		except FileExistsError:
			return print(f"As informações do perfil {self.arroba} já foram coletadas e salvas!")
		with open(f'{self.arroba}/{self.arroba}.txt','w') as file:
			file.write(f"Perfil-->{self.arroba} \n  Horário e data de criação--> {self.info['created']} \n  Nº de Seguidores--> {self.info['followers']} \n  Seguindo--> {self.info['following']} pessoas \n  Nº de tweets--> {self.info['tweets']} \n  Curtiu--> {self.info['likes']} tweets \n  Descrição--> {self.getdsc}")
		perfil = self.soup.find('img',class_='ProfileAvatar-image')
		capa = self.soup.find('div',class_='ProfileCanopy-headerBg').img
		urllib.request.urlretrieve(perfil.get('src'),f'{self.arroba}/foto-perfil.jpg')
		urllib.request.urlretrieve(capa.get('src'),f'{self.arroba}/capa.jpg')
		return print("Informações salvas!")

marcelo = Twitter('https://twitter.com/MarceloM12')
marcelo.save_info()
