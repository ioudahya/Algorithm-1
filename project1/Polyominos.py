"""
Nom : Oudahya
Prénom : Ismaïl
N°matricule : 000479390
INFO-F103

Ce projet consiste à utiliser le backtracking 
pour résoudre le problème de polyominos , on cherche à trouver une solution 
optimal pour mettre toute les pièces dans un seul tableau , 
on doit donc trouver comment construire la tableau , une manière de les faires rentrées 
et sans oublier les différentes manière de rotation pour les pièces.
"""
import sys

class Ma_matrice:
	"""Classe contenant une matrice sous forme de liste de listes et des méthodes qui performent
	des opérations sur la matrice."""

	def __init__(self, liste):
		"""Input: liste de listes contenant la matrice 
		Doit contenir la variable self.matrice = liste 
		La matrice doit être recentrée lors de l'initialisation de l'objet en utilisant translation_haut_gauche(self)"""
		self.matrice = liste

	def colonne(self, col_index):
		""" Input: col_index est un int
		Output = colonne col_index de self.matrice sous forme de liste"""
		liste_colonnes=[]
		for i in range(len(self.matrice)) :
			new_list=[]
			for j in range(len(self.matrice)) :
				new_list.append(self.matrice[j][i])
			liste_colonnes.append(new_list)
		return liste_colonnes[col_index]

	def rotation_horaire(self):
		"""Output = objet de la classe Ma_matrice dont la matrice est la rotation horaire de 
		90 degrés de self.matrice. La nouvelle matrice doit également être translatée en haut à 
		gauche en utilisant translation_haut_gauche(self).
		Attention, self.matrice reste inchangée."""
		rotation=[]
		for x in zip(*self.matrice) :
			rotation.append(list(x)[::-1])
		return Ma_matrice(rotation)

	def reflexion_axe_horizontal(self):
		"""Output = objet de la classe Ma_matrice dont la matrice est la réflexion sur l'axe horiontal  
		de self.matrice. La nouvelle matrice doit également être translatée en haut à 
		gauche en utilisant translation_haut_gauche(self).
		Attention, self.matrice reste inchangée."""
		reflexion=[]
		for i in range(len(self.matrice)-1,-1,-1) :
			reflexion.append(self.matrice[i])
		return Ma_matrice(reflexion)

	def translation_haut(self, n):
		"""Fonction interne qui translate circulairement vers le haut self.matrice par n lignes
		Pas de output"""
		for i in range(len(self.matrice)) :
			for j in range(len(self.matrice)) :
				if self.matrice[i][j] == 1 :
					self.matrice[i-n][j] = self.matrice[i][j]
					self.matrice[i][j] = 0

	def translation_gauche(self, n):
		"""Fonction interne qui translate circulairement vers la gauche self.matrice par n colonnes
		Pas de output"""
		for i in range(len(self.matrice)) :
			for j in range(len(self.matrice)) :
				if self.matrice[i][j] == 1 :
					self.matrice[i][j-n] = self.matrice[i][j]
					self.matrice[i][j] = 0

	def translation_haut_gauche(self):
		"""Fonction interne qui recentre self.matrice de telle manière que ni la première colonne
		ni la première ligne ne contiennent que des 0. 
		Cette opération est nécessaire pour ne pas avoir en double certaines variantes d'une pièce 
		après rotations/réflexions dans la classe Piece.
		Pas de output"""
		"""
		cette fonction fait appel à translation haut et translation gauche 
		on cherche à itérer si la colonne ou la ligne ne vaut que des 0 et on translate
		sinon on ne fait rien , au risque de voir la piece disparaitre
		"""
		logic=False
		count_transla_gauche=0
		while not logic :
			if 1 not in self.colonne(count_transla_gauche) and not logic:
				count_transla_gauche+=1
			else :
				logic=True 
		self.translation_gauche(count_transla_gauche)


		count_transla_haut=0
		logic_haut=False
		for i in range(len(self.matrice)) :
			if 1 not in self.matrice[i] and not logic_haut:
				count_transla_haut+=1
			else :
				logic_haut=True
		self.translation_haut(count_transla_haut)
		


class Piece:
	"""Classe définissant un polyomino, contenant son nom et la liste de matrices pour 
	toutes ses variantes dues à des rotations et réflexions."""

	def __init__(self, nom, variante):
		""" Input: nom = 1 caractère ASCII sous forme de string
				   variante = objet de classe Ma_matrice.
		Toutes ses rotations/réflexions différentes doivent être ajoutées dans la
		liste self.liste_variantes"""
		self.nom = nom
		self.liste_variantes= [variante]

	def ajout_variante(self, nouvelle_variante):
		"""Ajoute l'objet nouvelle_variante de la classe Ma_matrice à la liste self.liste_variantes
		si elle n'y est pas encore.
		Pas de output"""
		if nouvelle_variante not in self.liste_variantes :
			self.liste_variantes.append(nouvelle_variante)

class Tableau:
	"""Classe définissant un tableau"""

	def __init__(self, dimensions, liste_pieces):
		"""Input: dimensions = tuple de 2 integers contenant la hauteur = dimensions[0] et la largeur du tableau = dimensions[1]
				  liste_pieces = liste d'objets de la classe piece
			Les variables suivantes doivent être contenues dans la classe:
			- liste_pieces
			- hauteur = hauteur du tableau
			- largeur = largeur du tableau
			- tableau = matrice sous forme de liste de listes de strings de longueur 1.
			Lorsque le tableau est initialisé, il est vide et ne contient que des espaces. 
			- Pos_pieces = liste de même longueur que liste_pieces. 
			Si pièce i n'est pas placée sur le tableau, Pos_pieces[i] = []
			Si pièce i est placée sur le tableau, Pos_pieces[i] = [x,y] où x et y sont les coordonnées 
			sur le tableau du coin en haut à gauche de la sous matrice de la variante ajoutée de la pièce
			"""
		self.liste_pieces=liste_pieces
		self.change_dimension(dimensions)
		self.Pos_pieces=[ [] for i in range(len(liste_pieces))]		

	def change_dimension(self,dimensions):
		"""
		fonction définissant les dimensions pour la construction du tableau , elle est appelé sur le __init__ 
		"""
		self.hauteur = dimensions[0]
		self.largeur = dimensions[1]
		self.tableau=[[" " for j in range(self.largeur)] for i in range(self.hauteur)] 

	def ajouter_piece(self, index_piece, num_var, pos):
		"""Ajoute si possible le polyomino self.liste_pieces[index_piece] à variante liste_variantes[num_var]
		dont le coin en haut à gauche de la matrice se trouve à la position pos (= liste de 2 integers) du tableau.
		Tenez en compte le fait que certaines matrices de pièces peuvent contenir des lignes ou colonnes vides en bas ou à droite. 
		Si l'ajout est possible, cette méthode modifie les variables:
		- self.Pos_pieces[index_piece] = pos
		- self.tableau[i][j] = nom_piece là où la pièce est placée sur le tableau 
		Output = True si la pièce a été ajoutée, False si l'ajout n'était pas possible"""
		flag=True
		mat = self.liste_pieces[index_piece].liste_variantes[num_var].matrice
		name = self.liste_pieces[index_piece].nom
	
		x = pos[0]
		y = pos[1]
		liste_pos = []
		for i in range(len(mat)) :
			for j in range(len(mat[i])) :
				if x+i < self.hauteur and y+j < self.largeur:
					if self.tableau[x+i][y+j] == " " :	
						if mat[i][j] == 1 :
							liste_pos.append([x+i,y+j])
					else :
						if mat[i][j] == 1 :
							flag = False
							break
				else : 
					if mat[i][j] == 1 :
						flag = False
						break
		if flag :
			self.Pos_pieces[index_piece]=pos
			for position in liste_pos:
				x = position[0]
				y = position[1]
				self.tableau[x][y] = name

		return flag		

	def enlever_piece(self, index_piece):
		"""Enlève la pièce à la position index_piece dans self.liste_piece du tableau. 
		Cette méthode modifie les variables:
		- self.Pos_pieces[index_piece] = [] 
		- self.tableau[i][j] = " " là où était la pièce
		Si la pièce n'est pas sur le tableau, cette fonction ne fait rien.
		Pas de output"""
		name = self.liste_pieces[index_piece].nom
		pos = self.Pos_pieces[index_piece]

		if pos != []:
			for i in range(pos[0],self.hauteur):
				for j in range(pos[1],self.largeur):
					if self.tableau[i][j] == name:
						self.tableau[i][j] = " "

	def imprimer(self):
		"""Imprime le tableau
		Pas de output"""
		print(" " + "-" * self.largeur + " ")
		for i in range(self.hauteur):
			content = ''
			for j in range(self.largeur):
				content += self.tableau[i][j]
			print("|" + content + "|")
		print(" " + "-" * self.largeur + " ")

	def backtracking(self, profondeur):
		"""Fonction de backtracking qui essaie de placer les pièces sur le tableau
		profondeur est un integer qui indique la profondeur dans le backtracking qui dans ce cas 
		correspond à l'index de la pièce à ajouter à ce niveau du backtracking
		Output = True si une solution trouvée
		"""

		if (profondeur == len(self.liste_pieces)) : #condition d'arrêt si self.solutionT = True et que profondeur vaut 5 on trouve une solution
			self.sol[self.i] = False
			self.solutionT = True
			self.ListeSolution.append(self.copy()) # copie du tableau que j'ajoute dans ListeSolution pour pouvoir le return 
			return self.solutionT #return True si solution trouver

		else :
			if profondeur == 0:
				self.ListeSolution = []
				self.solutionT = False
				max_it = 50 #max itération sinon boucle infini au cas ou 
				add_taille = 0 # pour ajouter la taille si on trouve pas de solution 
				while not self.solutionT  and add_taille < max_it: # j'ai suivi un peu le canevas de celui des dames
					liste_tailles = possibles_factorisations(taille_totale_pieces(self.liste_pieces) + add_taille)
					self.sol = [True]* (len(liste_tailles))
					self.i = 0

					for taille in liste_tailles:
						if taille[0] > taille[1]: 
							taille = (taille[1] ,taille[0])
						self.change_dimension(taille) #appel de la fonction avec les dimensions
						self.prebacktracking(profondeur) # appel la fonction qui test pour ajouter et retire si pas possible
						self.i += 1
					add_taille += 1
			else:
				self.prebacktracking(profondeur)# appel la fonction qui test pour ajouter et retire si pas possible
		return self.solutionT 
		
	def prebacktracking(self,profondeur):
		"""
		fonction appelé lors de la fonction backtrack parcours et test les différentes variantes possible
		dans le tableau , ajoute si c'est bon et continue le backtrack en itération du parametre du backtrack 
		si pas trouver on enleve la piece
		"""
		for it in range(len(self.liste_pieces[profondeur].liste_variantes)):
			for x in range(self.hauteur):
				for y in range(self.largeur):
					if (self.ajouter_piece(profondeur,it,[x,y])) and self.sol[self.i]:
						self.backtracking(profondeur+1)
						self.enlever_piece(profondeur)
					if not self.sol[self.i] :
						break

	def copy(self):
		"""
		fonction qui fait une copie du tableau si la solution a été trouver
		et renvoie l'ensemble de la copie du tableau
		"""
		res = Tableau((self.hauteur, self.largeur ), self.liste_pieces)
		copie_tableau = [[" " for j in range(self.largeur)] for i in range(self.hauteur)] 
		for i in range(self.hauteur):
			for j in range(self.largeur):
				copie_tableau[i][j] = self.tableau[i][j]
		res.tableau = copie_tableau
		return res

	def __lt__(self,other):
		# pour renvoyer les tableaux bien trié
		return self.hauteur < other.hauteur
	def __gt__(self,other):
		# pour renvoyer les tableaux bien trié
		return self.hauteur > other.hauteur

def lire_fichier(nom_fichier):
	""" Input = string étant le nom du fichier
	Output = liste d'objets de classe Piece représentant les polyominos 
	contenus dans le fichier"""
	"""
	récupere le nom du fichier grâce a sys et renvoie la suite de cette manière ci
	ex : [Piece('a',Ma_matrice([suite de matrice])), etc...]
	"""
	liste_contenue=[]
	fichier = open(nom_fichier,"r")
	for line in fichier :
		liste_contenue.append(line.strip())
	fichier.close()
	lettre_file=[]
	matrix_file=[]
	i=1 
	while i  != len(liste_contenue) :
		j=0
		x=j+int(liste_contenue[0][2])
		suite_de_matrice=[]
		if liste_contenue[i] in 'a,b,c,d,e,f,g,h,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z' :
			lettre_file.append(liste_contenue[i])
			while j != x :
				i+=1
				suite_de_matrice.append([liste_contenue[i]])
				j+=1
			ensemble_matrice = trouver_matrice(suite_de_matrice)
		matrix_file.append(ensemble_matrice)

		i+=1
	ensemble_piece=[]
	for i in range(int(liste_contenue[0][0])) :
		ensemble_piece.append(Piece(lettre_file[i],Ma_matrice(matrix_file[i])))
	return ensemble_piece

def trouver_matrice(liste) :
	"""
	cette fonction permet de transformer les élements dans le fichier texte (str) en (int)
	tout en supprimant les espaces entre chaque nombre
	"""
	entier_matrice=[]
	for line in liste : 
		for i in line :
			sous_liste=[]
			for element in i :
				if element == "0" or element =="1" :
					sous_liste.append(int(element))
		entier_matrice.append(sous_liste)
	return entier_matrice

def taille_totale_pieces(liste_pieces):
	""" Input = liste d'objet de classe Piece
	Output = somme de la taille de chaque pièce"""
	count = 0
	for piece in liste_pieces : 
		for x in piece.liste_variantes[0].matrice : #parcours l'objet piece pour récuperer les pièces "1"
			for y in x : 
				count += y
	return count

def possibles_factorisations(nb):
	"""Input: nb est un int
	Output = liste de tuples de taille 2 contenant toutes les factorisations possibles en 
	2 facteurs de nb. Attention à ne pas les répéter 2 fois."""
	"""
	cette fonction permet de factoriser un nombre 
	qui est la somme de la taille des pieces totale "1" et on reçoit 
	un ensemble de factorisation par 2 polynomes 
	qui sont des choix pour la construction du tableau
	"""
	liste_nombre_factoriser = decomposition_factoriser(nb)
	facto = new_facon_factorisation(liste_nombre_factoriser)
	return facto

def trouver_liste_solutions(nom_fichier):
	"""Fonction principale qui trouve la liste des solutions.
	Output = liste d'objets de la classe Tableau qui contiennent les différentes solutions"""
	"""
	renvoie la solution en output triées 
	en appelant le fichier,le backtrack, la rotation horaire , la classe piece et la classe tableau
	"""
	diff_solu=lire_fichier(nom_fichier)
	for piece in diff_solu :
		matrice= piece.liste_variantes[0]
		for i in range(4) :
			matrice = matrice.rotation_horaire()
			#matrice = matrice.reflexion_axe_horizontal()
			piece.ajout_variante(matrice)
	tableau = Tableau([0,0],diff_solu)
	solution = tableau.backtracking(0)
	liste_solution = tableau.ListeSolution
	liste_solution.sort()
	return liste_solution

def new_facon_factorisation(listee) :
	"""
	fonction qui est appelé pour la factorisation 
	on recupère les 2 polynomes en faisant attention 
	à ne pas les dupliquer en inversant les 2 polynomes
	ex : (2,10) et (10,2)
	"""
	new_list=[]
	deux_liste=[]
	solu=[]
	while len(listee) != 0 :
		for i in range(1) :
			new_list.append(listee[i])
		multiple=1
		multiple_1=1
		del listee[0]
		for i in listee : 
			multiple = multiple * i
		for i in new_list : 
			multiple_1 = multiple_1 *i
		if (multiple_1,multiple) and (multiple,multiple_1) not in solu : 
			solu.append((multiple_1,multiple))

	return solu

def decomposition_factoriser(nombre) :
	"""
	cette fonction permet de décomposer le nombre 
	de la somme des pieces 
	pour pouvoir récuperer une factorisation
	ex : 16 --> renvoie [2,2,2,2]
	"""
	composant=[]
	count=2 
	while nombre > 1 :
		while nombre%count == 0 :
			composant.append(count)
			nombre=nombre//count
		count=count+1
	return composant

if __name__ == '__main__':
	test_fichier = sys.argv[1]
	
	liste_solution=trouver_liste_solutions(test_fichier)
	for tableau in liste_solution : 
		tableau.imprimer()