#Oudahya Ismaïl
# INFO-F103 : PROJET 3  hachage
# 10/05/2020

import timeit
import random
from hashtable import*
from hashers import*
"""
Dans les teste qui réalise la vitesse de chaque insert/delete , je teste en répétition avec un certain nombre 
et je repete cela 10 fois. 
"""
"""
Fonction random_char permettant de crée un random avec (y) lettre 
pour pouvoir tester beaucoup plus facilements les insert/delete
"""
def random_char(y) :
	random.seed()
	ascii_string='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	return ''.join(random.choice(ascii_string) for x in range(y))

a=random_char(5),random_char(5)
b=random_char(5),random_char(5)
c=random_char(5),random_char(5)
d=random_char(5),random_char(5)
e=random_char(6),random_char(6)
f=random_char(6),random_char(6)
g=random_char(5),random_char(5)
"""
cette suite de fonction me permet 
de récuperer le load_factor pour pouvoir calculer 
le sondage pour le rapports.
"""
def alphaKR() :
	ht = HashTableChaining(11,HasherKR())
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	return ht.load_factor()
def alphaCRC32() :
	ht = HashTableChaining(11,HasherCrc32())
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	return ht.load_factor()
def alphaDJB2() :
	ht = HashTableChaining(11,HasherDjb2())
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	return ht.load_factor()
def alphaDoubleKR_CRC32() :
	ht = HashTableDouble(11, DoubleHasher(HasherKR(), HasherCrc32()))
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	return ht.load_factor()
def alphaDoubleDJB2_CRC32(): 
	ht = HashTableDouble(11, DoubleHasher(HasherDjb2(), HasherCrc32()))
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	return ht.load_factor()
def alphaDoubleDJB2_KR() :
	ht = HashTableDouble(11, DoubleHasher(HasherDjb2(), HasherKR()))
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	return ht.load_factor()
alpha0=alphaKR()
alpha1=alphaCRC32()
alpha2=alphaDJB2()
alpha3=alphaDoubleKR_CRC32()
alpha4=alphaDoubleDJB2_CRC32()
alpha5=alphaDoubleDJB2_KR()



x4='''
from hashers import HasherKR
from hashtable import HashTableChaining
'''

#simple hachage KR
testcode4 = '''
def testK() :	
	ht= HashTableChaining(11,HasherKR())
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
'''
testcode_delete4 = '''
def testK() :	
	ht= HashTableChaining(11,HasherKR())
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	ht.delete(b[0],b[1])
	ht.delete(c[0],c[1])
	ht.delete('ok','ok')
'''
times3=timeit.repeat(stmt=testcode4,setup=x4,number=10000,repeat=10)
times3_delete=timeit.repeat(stmt=testcode_delete4,setup=x4,number=10000,repeat=10)

#simple hachage CRC32

x5='''
from hashers import HasherCrc32
from hashtable import HashTableChaining
'''

testcode5 = '''
def testK() :	
	ht= HashTableChaining(11,HasherCrc32())
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	ht.delete(b[0],b[1])
	ht.delete(c[0],c[1])
	ht.delete('ok','ok')
'''

times4=timeit.repeat(stmt=testcode5,setup=x5,number=10000,repeat=10)

# simple hachage DJB2
x6='''
from hashers import HasherDjb2
from hashtable import HashTableChaining
'''

testcode6 = '''
def testK() :	
	ht= HashTableChaining(11,HasherDjb2())
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	ht.delete(b[0],b[1])
	ht.delete(c[0],c[1])
	ht.delete('ok','ok')
'''


times5=timeit.repeat(stmt=testcode6,setup=x6,number=10000,repeat=10)


# double hachage KR et CRC32

x7='''
from hashers import HasherKR,HasherCrc32,DoubleHasher
from hashtable import HashTableDouble
'''

testcode7='''
def testK() :
	ht = HashTableDouble(12, DoubleHasher(HasherKR(), HasherCrc32()))
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	ht.delete(b[0],b[1])
	ht.delete(c[0],c[1])
	ht.delete('ok','ok')
'''

times6 = timeit.repeat(stmt=testcode7,setup=x7,number=10000,repeat=10)

# double hachage DJB2 et CRC32
x8='''
from hashers import HasherDjb2,HasherCrc32,DoubleHasher
from hashtable import HashTableDouble
'''

testcode8='''
def testK() :
	ht = HashTableDouble(12, DoubleHasher(HasherDjb2(), HasherCrc32()))
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	ht.delete(b[0],b[1])
	ht.delete(c[0],c[1])
	ht.delete('ok','ok')
'''

times7 = timeit.repeat(stmt=testcode8,setup=x8,number=10000,repeat=10)


# double hachage DJB2 et KR
x9='''
from hashers import HasherDjb2,HasherKR,DoubleHasher
from hashtable import HashTableDouble
'''

testcode9='''
def testK() :
	ht = HashTableDouble(11, DoubleHasher(HasherDjb2(), HasherKR()))
	ht.insert(a[0],a[1])
	ht.insert(b[0],b[1])
	ht.insert(c[0],c[1])
	ht.insert(d[0],d[1])
	ht.insert(e[0],e[1])
	ht.insert(f[0],f[1])
	ht.insert(g[0],g[1])
	ht.delete(b[0],b[1])
	ht.delete(c[0],c[1])
	ht.delete('ok','ok')
'''
times8= timeit.repeat(stmt=testcode9,setup=x9,number=10000,repeat=10)