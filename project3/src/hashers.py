#Oudahya Ismaïl
# INFO-F103 : PROJET 3  hachage
# 10/05/2020

class HasherDjb2:
	"""
	Algorithme djb2 de Daniel J. Bernstein
	"""
	def hash_key(self,string) :
		hashe = 5381
		for c in string : 
			hashe = ((hashe << 5) + hashe) + ord(c)
		res = hashe & 0xFFFFFFFF
		return res

class HasherCrc32:
	"""
	Algorithme CRC-32
	"""
	def __init__(self) :
		"""
		Ouverte du texte dans le constructeur pour prendre moins de temps
		d'execution
		"""
		self.fichier = open('crc.txt','r')
		self.ensemble = []
		for i in self.fichier :
			self.ensemble.append(i)

	def hash_key(self,string) :
		hashe = 0xFFFFFFFF
		for c in string : 
			idx = (hashe ^ ord(c)) & 0xFF
			i = int(self.ensemble[idx],16)
			hashe = (hashe >> 8) ^ i
		res = hashe ^ 0xFFFFFFFF
		return res

class HasherKR:
	"""
	Algorithme de Kernighan & Ritchie
	"""
	def hash_key(self,string) :
		hashe = 0
		for c in string : 
			hashe = hashe + ord(c)
		return hashe


class DoubleHasher :
	"""
	Classe utilisant le double hachage
	"""
	def __init__(self,Constru1,Constru2) :
		self.Constru1 = Constru1
		self.Constru2 = Constru2

	def hash_key(self,k,i) :
		hk1 = (2*self.Constru1.hash_key(k)+3)
		hk2 = (3*self.Constru2.hash_key(k)+1)
		return  hk1+hk2*i
