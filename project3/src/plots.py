#Oudahya Ismaïl
# INFO-F103 : PROJET 3  hachage
# 10/05/2020

import matplotlib.pyplot as plt 
from timer import *
from hashers import*
from hashtable import*




def HashTableChaining_collision_KR() :
	"""
	Fonction prenant un random de 5/6 lettre avec une table de 11 élements vide
	et l'envoie dans la fonction insert de KR
	la fonction return le nombre de collision
	"""
	ht= HashTableChaining(11,HasherKR())
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(5),random_char(5))
	return ht.get_count_collision()


def HashTableChaining_collision_CRC32() :
	"""
	Fonction prenant un random de 5/6 lettre avec une table de 11 élements vide
	et l'envoie dans la fonction insert de CRC32
	la fonction return le nombre de collision
	"""
	ht= HashTableChaining(11,HasherCrc32())
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(5),random_char(5))
	return ht.get_count_collision()
	

def HashTableChaining_collision_DJB2() :
	"""
	Fonction prenant un random de 5/6 lettre avec une table de 11 élements vide
	et l'envoie dans la fonction insert de DJB2
	la fonction return le nombre de collision
	"""
	ht= HashTableChaining(11,HasherDjb2())
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(5),random_char(5))
	return ht.get_count_collision()

def get_collision_chaining() :
	"""
	fonction faisant appel aux fonction précédentes ,
	elle construit le graphique comprenant légende , titre
	contenue et enregistre le graphique en .png
	"""
	new_list=[]
	new_list1=[]
	new_list2=[]
	for i in range(5) :
			new_list1.append(HashTableChaining_collision_CRC32())
			new_list.append(HashTableChaining_collision_KR())
			new_list2.append(HashTableChaining_collision_DJB2())
	CRC32=plt.plot(new_list1,"go")
	KR=plt.plot(new_list,"d")
	DJB2=plt.plot(new_list2,"s")
	plt.title('Collision chaining CRC32,KR,DJB2')
	plt.xlabel('Nombre de répétition')
	plt.ylabel('Nombre de collision')
	plt.legend([CRC32[0],KR[0],DJB2[0]],['Collision CRC32','Collision KR','Collision DJB2'])
	plt.grid(True)  
	plt.savefig('get_collision_chaining.png') 
	
def HashTableDouble_collision_KR_DJB2() :
	"""
	Fonction prenant un random de 5/6 lettre avec une table de 11 élements vide
	et l'envoie dans la fonction insert dans le douche hachage KR et DJB2
	la fonction return le nombre de collision
	"""
	ht = HashTableDouble(11,DoubleHasher(HasherDjb2(), HasherKR()))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(5),random_char(5))
	return ht.get_count_collision()
	

def HashTableDouble_collision_KR_CRC32() :
	"""
	Fonction prenant un random de 5/6 lettre avec une table de 11 élements vide
	et l'envoie dans la fonction insert dans le douche hachage KR et CRC32
	la fonction return le nombre de collision
	"""
	ht = HashTableDouble(11,DoubleHasher(HasherCrc32(), HasherKR()))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(5),random_char(5))
	return ht.get_count_collision()
	
def HashTableDouble_collision_DJB2_CRC32() :
	"""
	Fonction prenant un random de 5/6 lettre avec une table de 11 élements vide
	et l'envoie dans la fonction insert dans le douche hachage DJB2 et CRC32
	la fonction return le nombre de collision
	"""
	ht = HashTableDouble(11,DoubleHasher(HasherDjb2(), HasherCrc32()))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(5),random_char(5))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(6),random_char(6))
	ht.insert(random_char(5),random_char(5))
	return ht.get_count_collision()

def get_collision_doublehash() :
	"""
	fonction faisant appel aux fonction précédentes ,
	elle construit le graphique comprenant légende , titre
	contenue et enregistre le graphique en .png
	"""
	new_list5=[]
	new_list3=[]
	new_list4=[]
	for i in range(5) :
			new_list3.append(HashTableDouble_collision_KR_DJB2())
			new_list4.append(HashTableDouble_collision_KR_CRC32())
			new_list5.append(HashTableDouble_collision_DJB2_CRC32())
	KR_CRC321=plt.plot(new_list4,"go")
	KR_DJB21=plt.plot(new_list3,"d")
	DJB2_CRC321=plt.plot(new_list5,"s")
	plt.title('Collision Double Hachage KR_CRC32,KR_CRC32,DJB2_CRC32')
	plt.xlabel('Nombre de répétition')
	plt.ylabel('Nombre de collision')
	plt.legend([KR_CRC321[0],KR_DJB21[0],DJB2_CRC321[0]],['Collision KR_CRC32','Collision KR_DJB2','Collision DJB2_CRC32'])
	plt.grid(True) 
	plt.savefig('get_collision_doublehash.png')

	


def CHAINING_HASH() :
	"""
	Fonction faisant appel aux autres fonction qui calcule le temps d'éxecution 
	et en fait un graphique , celui ci correspond à un graphique de  chainaige simple KR/CRC32/DJB2
	il contient légende , contenue , titre et enregistre en .png
	"""
	KR = plt.plot(times3)
	CRC32 = plt.plot(times4)
	DJB2 = plt.plot(times5)
	plt.title('Temps chaining KR,CRC32,DJB2 (insert&delete)')
	plt.xlabel('Nombre de répétition')
	plt.ylabel('time(µs)')
	plt.legend([KR[0],CRC32[0],DJB2[0]],['Hasheur KR ','Hasheur CRC32','Hasheur DJB2'])
	plt.savefig('CHAINING_HASH.png')

	

def DOUBLE_CHAINING_KR_CRC32() :
	"""
	Fonction faisant appel aux autres fonction qui calcule le temps d'éxecution 
	et en fait un graphique , celui ci correspond à un graphique de double chainaige KR et CRC32
	il contient légende , contenue , titre et enregistre en .png
	"""
	KR = plt.plot(times6)
	KR_CHAINING = plt.plot(times3)
	CRC32_CHAINING = plt.plot(times4)
	DJB2_CHAINING = plt.plot(times5)
	print("Double hash KR_CRC32",alpha3)
	plt.title('Temps Double hachage KR_CRC32|chainage KR,CRC32,DJB2 (insert&delete)')
	plt.xlabel('Nombre de répétition')
	plt.ylabel('time(µs)')
	plt.legend([KR[0],KR_CHAINING[0],CRC32_CHAINING[0],DJB2_CHAINING[0]],['Double Hasheur KR et KR ','Chaining KR','Chaining CRC32','Chaining DJB2'])
	plt.grid(True)
	plt.savefig('DOUBLE_CHAINING_KR_CRC32.png')

	
def DOUBLE_CHAINING_DJB2_CRC32() :
	"""
	Fonction faisant appel aux autres fonction qui calcule le temps d'éxecution 
	et en fait un graphique , celui ci correspond à un graphique de double chainaige DJB2 et CRC32
	il contient légende , contenue , titre et enregistre en .png
	"""
	DJB2_CRC32_COLLISION = plt.plot(times7)
	KR_CHAINING = plt.plot(times3)
	CRC32_CHAINING = plt.plot(times4)
	DJB2_CHAINING = plt.plot(times5)
	plt.title('Temps Double hasheur DJB2_CRC32|KR,CRC32,DJB2 (insert&delete)')
	plt.xlabel('Nombre de répétition')
	plt.ylabel('time(µs)')
	plt.legend([DJB2_CRC32_COLLISION[0],KR_CHAINING[0],CRC32_CHAINING[0],DJB2_CHAINING[0]],['Double Hasheur DJB2 et CRC32','Chaining KR','Chaining CRC32','Chaining DJB2'])
	plt.grid(True)
	plt.savefig('DOUBLE_CHAINING_DJB2_CRC32.png')
	
def DOUBLE_CHAINING_DJB2_KR() :
	"""
	Fonction faisant appel aux autres fonction qui calcule le temps d'éxecution 
	et en fait un graphique , celui ci correspond à un graphique de double chainaige DJB2 et KR
	il contient légende , contenue , titre et enregistre en .png
	"""
	DJB2 = plt.plot(times8)
	KR_CHAINING = plt.plot(times3)
	CRC32_CHAINING = plt.plot(times4)
	DJB2_CHAINING = plt.plot(times5)
	plt.title('Temps Double hasheur DJB2_KR|chaining KR,CRC32,DJB2 (insert&delete)')
	plt.xlabel('Nombre de répétition')
	plt.ylabel('time(µs)')
	plt.legend([DJB2[0],KR_CHAINING[0],CRC32_CHAINING[0],DJB2_CHAINING[0]],['Double Hasheur DJB2 et KR','Chaining KR','Chaining CRC32','Chaining DJB2'])
	plt.grid(True)
	plt.savefig('DOUBLE_CHAINING_DJB2_KR.png')


# appel des fonctions qui renvoient les graphiques
if __name__ == "__main__" :
	get_collision_chaining()   
	get_collision_doublehash()
	CHAINING_HASH()
	DOUBLE_CHAINING_KR_CRC32()
	DOUBLE_CHAINING_DJB2_CRC32()
	DOUBLE_CHAINING_DJB2_KR()
