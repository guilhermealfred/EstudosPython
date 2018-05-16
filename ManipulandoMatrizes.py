def recebe_matriz():
	global num_linhas
	try:
		num_linhas = int(input('Quantas linhas?:'))
		matriz = []
		for i in range(num_linhas):
			matriz.append([int(i) for i in input().split()])
		return matriz
	except:
		print("DIGITA DIREITO")
		return recebe_matriz()
def separa(lista,a):
	saida = []
	while len(lista) >= a:
		saida.append(lista[:a])
		lista = lista[a:]
	return saida
def verticais(matriz):
	verts = []
	aux,x=0,0 
	while x < num_linhas:
		for i in matriz:
			verts.append(i[aux])
		x+=1
		aux+=1
	return separa(verts,len(matriz[0]))
def diagonais(matriz):
	j,s = 0,len(matriz)-1
	diagonal1,diagonal2 = [],[]
	try:
		for i in matriz: 
			diagonal1.append(i[j])
			diagonal2.append(i[s])
			s-=1
			j+=1
		return diagonal1,diagonal2
	except IndexError:
		pass
def quadrado_magico(matriz):
	try:
		comp = sum(matriz[0])
		verts = verticais(matriz)
		digs = diagonais(matriz)
		valid = [True for i in matriz if sum(i) == comp and True for i in verts if sum(i) == comp and True for i in digs if sum(i)==comp]
		if num_linhas >=2:
			if len(valid) == (len(matriz)*len(matriz[0]))*2:
				print('#---------------------------------------------#')
				for i in matriz:
					for j in i:
						print(j,end=' ')
					print("")
				return print("Forma um quadrado magico")
			else:
				raise IndexError
		else:
				raise IndexError
	except IndexError:
		print('#---------------------------------------------#')
		for i in matriz:
			for j in i:
				print(j,end=' ')
			print("")
		return print("Não forma um quadrado magico!")
#matriz = [[1,14,15,4],[12,7,6,9],[8,11,10,5],[13,2,3,16]]
matriz = [[2,7,6],[9,5,1],[4,3,8]]
#matriz = [[22,47,16,41,10,35,4],[5,23,48,17,42,11,29],[6,24,49,18,36,12],[13,31,7,25,43,19,37],[38,14,32,1,26,44,20],[21,39,8,33,2,27,45],[46,15,40,9,34,3,28]]
quadrado_magico(recebe_matriz())
