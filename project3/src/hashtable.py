#Oudahya Ismaïl
# INFO-F103 : PROJET 3  hachage
# 10/05/2020

class HashTableChaining :
	"""
	Classe qui prends en compte le hachage simple.
	"""
	def __init__(self,m,Construct1) :
		"""
		Constructeur ayant comme paramètre m qui est la taille de la table
		et Construct1 qui est le constructeur à choisir entre KR / CRC32 et DJB2
		"""
		self.m = m
		self.Construct1 = Construct1
		self.liste=[None]*m
		self.count_collision=0  # pour compter le nombre de collisions survenu 

	def insert(self,key,value) :
		"""
		Fonction servant à insérer les valeurs grâces à leur clé sur la table
		Avec une succéssion de condition pour certaine particularité du haching.
		Renvoie un overflow si il se trouve en dehors de la taille de la table
		"""
		Clef = self.Construct1.hash_key(key)
		direction = Clef % self.m 
		if self.liste[direction] == None :
			self.liste[direction] = (key,value)

		else : 

			if self.liste[direction][0] == key : 
				self.liste[direction] = None
				self.liste[direction] = (key,value)

			else :
				if self.liste[direction] != None : 
					self.count_collision+=1
					regroupe=[self.liste[direction]]
					regroupe.append((key,value))
					self.liste[direction] = regroupe
				if direction > self.m :
					raise OverflowError

	def delete(self,key) :
		"""
		Fonction servant à retirer un élements de la table grâce à sa clef
		si la position se retrouve en dehors de la table , celle ci renvoie KeyError
		sinon si elle trouve l'élements , elle le suprime.
		"""
		Clef = self.Construct1.hash_key(key)
		direction = Clef % self.m
		if self.liste[direction] == None :
			raise KeyError
		else :
			if type(self.liste[direction]) is list :
				for j in self.liste[direction] :
					if j[0] == key :
						self.liste[direction].remove(j)
			else :
				self.liste.pop(direction)  

	def get(self,key) :
		"""
		Foncition sevant à return la valeur d'une clé situé dans la table
		si la position se retrouve en dehors de la table ou si elle ne trouve rien alors 
		elle return KeyError
		"""
		Clef = self.Construct1.hash_key(key)
		direction = Clef % self.m
		if self.liste[direction] == None :
			raise KeyError
		if direction > self.m :
			raise KeyError
		else : 
			return self.liste[direction][1]


	def load_factor(self) :
		"""
		Fonction servant à renvoyer le load factor
		"""
		alpha = HashTableChaining.size(self) / self.m
		return alpha

	def size(self) :
		"""
		Calcul le nombre d'élements introduit dans la table et renvoie se nombre
		"""
		count=0
		for i in self.liste :
			if i != None :
				if type(i) is list :
					for j in i :
						count+=1
				else :
					count+=1
		return count

	def get_count_collision(self) :
		"""
		fonction servant à renvoyer le nombre de collision perçu lors de l'insertion d'élements
		dans la table.
		"""
		return self.count_collision

class HashTableDouble() :
	"""
	Fonction qui prends en charge le double hachage
	"""
	def __init__(self,m,DoubleHasher) :
		"""
		En paramètre nous avons , la taille de la table, 
		l'appel de fonction servant à calculer la clé , ici on en aura besoin de 2 pour 
		utiliser le double hachage.
		"""
		self.m=m
		self.DoubleHasher=DoubleHasher
		self.liste=[None]*m
		self.i = 0
		self.count_collision=0 # compteur pour le nombre de collision


	def insert(self,key,value):
		"""
		Fonction servant à insérer les valeurs grâces à leur clé sur la table
		Avec une succéssion de condition pour certaine particularité du haching.
		Renvoie un overflow si il se trouve en dehors de la taille de la table
		Ici , on utilisera l'adressage direct
		"""

		Clef = self.DoubleHasher.Constru1.hash_key(key)
		Clef_dbhachage = self.DoubleHasher.hash_key(key,self.i)%self.m
		direction = Clef % self.m
		if self.liste[direction] == None : 
			self.liste[direction] = (key,value)
		else : 
			if self.liste[direction][0] == key : 
				self.liste[direction] = None
				self.liste[direction] = (key,value)
			else :
				self.count_collision+=1
				flag = True
				self.i=0
				while flag : 
					if self.i >= self.m :
						raise OverflowError
					if self.liste[self.i] == None : 
						self.liste[self.i] = (key,value)
						flag = False
					else : 
						if self.i < self.m :
							self.i +=1
						else : 
							flag=False
							raise OverflowError

	def delete(self,key) :
		"""
		Fonction servant à retirer un élements de la table grâce à sa clef
		si la position se retrouve en dehors de la table , celle ci renvoie KeyError
		sinon si elle trouve l'élements , elle le suprime.
		"""
		Clef = self.DoubleHasher.Constru1.hash_key(key)
		direction = Clef % self.m
		if self.liste[direction] == None :
			raise KeyError
		else :
			if type(self.liste[direction]) is list :
				for j in self.liste[direction] :
					if j[0] == key :
						self.liste[direction].remove(j)
			else :
				self.liste.pop(direction) 

	def get(self,key) :
		"""
		Foncition sevant à return la valeur d'une clé situé dans la table
		si la position se retrouve en dehors de la table ou si elle ne trouve rien alors 
		elle return KeyError
		"""
		Clef = self.DoubleHasher.Constru1.hash_key(key)
		direction = Clef % self.m
		flagou=True
		w=0
		while  flagou :
			if self.liste[w] == None : 
				if w <= self.m :
					w+=1
			if w == self.m :
				raise KeyError
			if self.liste[w] != None : 
				if self.liste[w][0] == key :
					flagou = False
					return self.liste[w][1]
				if self.liste[w][0] != key : 
					w+=1

	def load_factor(self) :
		"""
		Fonction servant à renvoyer le load factor
		"""
		alpha = HashTableDouble.size(self) / self.m 
		return alpha
	def size(self) :
		"""
		Calcul le nombre d'élements introduit dans la table et renvoie se nombre
		"""
		count = 0 
		for i in self.liste : 
			if i != None : 
				count += 1 
		return count

	def get_count_collision(self) :
		"""
		fonction servant à renvoyer le nombre de collision perçu lors de l'insertion d'élements
		dans la table.
		"""
		return self.count_collision









