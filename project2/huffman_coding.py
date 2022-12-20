"""
Nom,prénom : Oudahya Ismaïl
N° matricule : 000479390
INFO-F103

Résumer : 

Ce projet consiste à crée un arbre Huffman avec le langage python
nous devons crée un arbre avec une suite de liste de caractère suivant de leur nombre correspondant,
ensuite pouvoir les compresser en bytes grace au parcourt de l'arbre --> 0 pour gauche et 1 pour droite 
pour ensuite les décompresser en binaire
"""
class HuffmanTree:
	"""Classe représentant un arbre binaire"""

	def __init__(self, freq, char=None, left=None, right=None):
		"""
		:param freq: le score du nœud
		:param char: le symbole qui lui est associé
		:param left: le fils gauche du nœud
		:param right: le fils droit du nœud
		"""
		self.freq = freq
		self.char = char
		self.left = left
		self.right = right


def get_frequencies(text):
	"""
	:param text: un str qu'on veut compresser
	:return: une liste de tuples qui contiennent un caractère en premier position et
	sa frequence d'apparition dans text en second
	"""
	file=open(text,'r')
	fichier=[]
	liste_de_lettre=[]
	lettre_nb=[]
	for i in file :
		fichier.append(i)
		for element in i :
			if element not in liste_de_lettre :
				liste_de_lettre.append(element)
	for i in liste_de_lettre:
		counter=0
		for j in fichier : 
			for x in j :
				if i == x:
					counter+=1
		lettre_nb.append((i,counter))
	lettre_nb.sort(key=lambda nombre:nombre[1])
	return lettre_nb

def tri_bubble(list_trier) :
	"""
	la fonction qui permet de trier en utilisant le tri bulle données dans le cours
	d'algorithme , tout type de trie aurait marché mais j'ai opter pour celui la 
	car il a une complexité min de o(n) et max o(n^2)
	"""
	flag = True
	num = len(list_trier)-1
	while num > 0 and flag :
		flag = False
		for i in range(num) :
			if isinstance(list_trier[i],tuple) and isinstance(list_trier[i+1],tuple):
				if list_trier[i][1]> list_trier[i+1][1] :
					flag = True
					list_trier[i],list_trier[i+1] = list_trier[i+1],list_trier[i]
			if isinstance(list_trier[i],HuffmanTree) and isinstance(list_trier[i+1],HuffmanTree) :
				if list_trier[i].freq > list_trier[i+1].freq :
					flag=True
					list_trier[i],list_trier[i+1] = list_trier[i+1],list_trier[i]
			if isinstance(list_trier[i],tuple) and isinstance(list_trier[i+1],HuffmanTree) :
				if list_trier[i][1] > list_trier[i+1].freq :
					flag= True
					list_trier[i],list_trier[i+1] = list_trier[i+1],list_trier[i]
			if isinstance(list_trier[i],HuffmanTree) and isinstance(list_trier[i+1],tuple) :
				if list_trier[i].freq > list_trier[i+1][1] :
					flag=True
					list_trier[i],list_trier[i+1] = list_trier[i+1],list_trier[i]
		num=num-1
	return list_trier


def build(freq_list) :
	"""
	construit l'arbre , vérifie si c'est un tuple ou un objet de la classe
	et construit.
	et supprime les élements qui ont servit à construire pour les rajoute à nouveau 
	dans la liste.
	"""
	if (type(freq_list[0]) is tuple and type(freq_list[1]) is HuffmanTree) :
		freq_1=freq_list[0]
		freq_2=freq_list[1]
		node = HuffmanTree(freq_1[1]+freq_2.freq,(str(freq_1[0])),freq_1,freq_2)
		freq_list.append(node)
	if (type(freq_list[1]) is tuple and type(freq_list[0]) is HuffmanTree) :
		freq_1=freq_list[0]
		freq_2=freq_list[1]
		node = HuffmanTree(freq_1.freq+freq_2[1],(str(freq_2[0])),freq_1,freq_2)
		freq_list.append(node)
 
	if (type(freq_list[0]) is HuffmanTree and type(freq_list[1]) is HuffmanTree) or (type(freq_list[1]) is HuffmanTree and type(freq_list[0]) is HuffmanTree):
		freq_1=freq_list[0]
		freq_2=freq_list[1]
		node = HuffmanTree(freq_1.freq + freq_2.freq,None,freq_1,freq_2)
		freq_list.append(node)

	if (type(freq_list[0]) is tuple and type(freq_list[1]) is tuple) or (type(freq_list[1]) is tuple and type(freq_list[0]) is tuple):
		freq_1=freq_list[0]
		freq_2=freq_list[1]		
		node = HuffmanTree(freq_1[1] + freq_2[1],(str(freq_1[0])+str(freq_2[0])),freq_1,freq_2)
		freq_list.append(node)	
	freq_list.remove(freq_1)
	freq_list.remove(freq_2)	
	return freq_list
def build_huffman_tree(freq_list):
	"""
	:param freq_list: la liste des fréquences
	:return: une instance de HuffmanTree (l'arbre de huffman que vous avez construit)
	la fonction fait appelle à tri_bulle qui trie la liste en utilisant le tri par bulle
	et apelle la fonction build qui construit la totalité de l'arbre.
	je return donc une instance de la classe HuffmanTree qui contient l'arbre
	"""
	while len(freq_list) > 1 :
		tri_freq_list=tri_bubble(freq_list)
		resultat=build(tri_freq_list)
	for arbre in resultat : 
		return arbre

def convert_bin_string_to_bytes(compressed_text):
	"""
	:param compressed_text: str composé uniquement de "0" et "1"
	:return: bytes
	"""
	padding = len(compressed_text) % 8
	if padding != 0:
		padding = 8 - padding

	byte_list = list()
	compressed_text += "0" * padding
	for i in range(0, len(compressed_text), 8):
		byte = compressed_text[i:i + 8]
		byte_list.append(int(byte, 2))
	return bytes(byte_list)

def translator_arbre_binaire(huffman_tree,text,alist_binaire,adico_binaire) :
	"""
	:parametre huffman_tree : l'arbre de huffman pour compresser le texte
	:text qui est un texte à compresser
	: alist_binaire : parametre ou sont stocker les "0" et "1"
	: adico_binaire : dictionnaire possédant comme clef et valeur --> {a: 0001} de toute lettre
	"""
	if isinstance(huffman_tree,HuffmanTree) :
		alist_binaire.append(0)
		temp=translator_arbre_binaire(huffman_tree.left,text,alist_binaire,adico_binaire)
		if temp != [] :
			adico_binaire[temp[0]] = temp[1:]
		alist_binaire.pop()

		alist_binaire.append(1)
		temp = translator_arbre_binaire(huffman_tree.right,text,alist_binaire,adico_binaire)
		if temp != [] :
			adico_binaire[temp[0]] = temp[1:]
		alist_binaire.pop()
	else :
		for character in text :
			if character == huffman_tree[0] :
				return [character]+alist_binaire
	return []

def compress(huffman_tree, text):
	"""
	:param huffman_tree: un arbre de huffman pouvant servir à compresser text
	:param text: le texte à compresser
	:return: un objet de type bytes, résultant de la compression
	"""
	alist_binaire=[]
	adico_binaire={}
	bits=""
	translator_arbre_binaire(huffman_tree,text,alist_binaire,adico_binaire)
	resultat_binaire=[]
	for character in text :
		resultat_binaire+= adico_binaire[character]
	for i in resultat_binaire :
		bits += str(i)
	return convert_bin_string_to_bytes(bits)

def convert_bytes_to_bin_string(compressed_binary):
	"""
	:param compressed_binary: un objet de type bytes
	:return: str composé uniquement de "0" et "1"
	"""
	compressed_text = ""
	for b in compressed_binary:
		compressed_text += f"{b:08b}"
	return compressed_text

def get_caractere(huffman_tree,compressed_binary,astring_binaire,i) :
	"""
	fonction servant à retrouver le caractère dans l'arbre grâce a une suite 
	de nombre "0" et "1" qui parcourt l'arbre 
	0 pour gauche et 1 pour droite.
	return le charactere trouver.
	"""
	while isinstance(huffman_tree,HuffmanTree) and i < len(compressed_binary):

		if compressed_binary[i] == '0' :
			huffman_tree=huffman_tree.left
		if compressed_binary[i] == '1' :
			huffman_tree=huffman_tree.right
		i+=1
	if (not isinstance(huffman_tree,HuffmanTree) ):
		return huffman_tree[0],i
	return '',len(compressed_binary)

def traduction_arbre_string(huffman_tree,compressed_binary,astring_binaire,i) :
	"""
	apelle la fonction get_caractere en reparcourant le tableau pour chaque lettre trouver
	jusqu'à ce que la variable compressed_binary ou sont stocker les 0 et 1 soit totalement
	utiliser et return l'ensemble de charactere en string
	"""
	i=0
	while i < len(compressed_binary) :
		car,i=get_caractere(huffman_tree,compressed_binary,astring_binaire,i)
		astring_binaire+=str(car)
	return astring_binaire

def decompress(huffman_tree, compressed_binary):
	"""
	:param huffman_tree: l'arbre de huffman correspondant au texte original
	:param compressed_binary: le texte compressé sous forme de bytes
	:return: un objet de type str qui, si tout se passe bien, devrait correspondre au texte original.
	fait appelle à la fonction traduction_arbre_string et return le tout le string traduit par l'arbre.
	"""
	astring_binaire=""
	texte_complet=traduction_arbre_string(huffman_tree,compressed_binary,astring_binaire,0)
	return texte_complet

def imprimer(huffman_tree,direction,regroupe,stock=None) :
	"""
	fonction servant à crée l'arbre de manière a avoir un bon
	visuel , je stock en fonction de ce qui est gauche ou droite 
	et si je tombe sur un noeud ou un fils je print.
	cette fonction est appelé dans print_huffman_tree
	"""
	if direction:
		stock.append(" gauche --> ")
	if direction == False :
		stock.append(" droite --> ")
	if isinstance(huffman_tree,HuffmanTree) :
		if direction is None :
			print(" racine  " + str(huffman_tree.freq))
		else :
			print("".join(stock) + str(huffman_tree.freq))
		imprimer(huffman_tree.left,True,regroupe,stock)
		stock.pop()
		imprimer(huffman_tree.right,False,regroupe,stock)
		stock.pop()
	else:
		print("".join(stock) + (str(huffman_tree)))

def print_huffman_tree(huffman_tree) :
	"""
	:param huffman_tree: un objet de type HuffmanTree
	:return: None
	"""
	stock=[]
	regroupe=[]
	imprimer(huffman_tree,None,regroupe,stock)




if __name__ == '__main__' :
	texte=get_frequencies('test.txt')
	file=open('test.txt','r')
	lst=""
	for i in file : 
		lst+=str(i)
	m=build_huffman_tree(texte)
	res=compress(m,lst)
	print(decompress(m,convert_bytes_to_bin_string(res)))

