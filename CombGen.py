from itertools import combinations as comb

print "\n <<< GENERATORE DI COMBINAZIONI SENZA RIPETIZIONI >>>\n"

dic = {'1':'A','2':'B','3':'C','4':'D','5':'E','6':'F','7':'G','8':'H','9':'I','10':'J','11':'K','12':'L','13':'M','14':'N','15':'O','16':'P','17':'Q','18':'R','19':'S','20':'T','21':'U','22':'V','23':'W','24':'X','25':'Y','26':'Z'}

combinazioni = []

lun = input(" Scrivi il numero da considerare per generare le diverse combinazioni (max 13): ")

while lun > 13:
	print "\n <<< !!! NUMERO TROPPO ALTO !!! >>>\n"
	lun = input(" Scrivi il numero da generare da considerare per generare le diverse combinazioni (max 13): ")

#-------#

choice = raw_input("\n Indica come preferisci visualizzare le combinazioni:\n\t* con lettere (l)\n\t* con numeri (n)\n\t ")

while choice != 'l' and choice != 'n':
	print "\n\t### Input Errato ###\n"
	choice = raw_input(" Indica come preferisci visualizzare le combinazioni:\n\t* con lettere (l)\n\t* con numeri (n)\n\t ")

#-------#

for i in range(1,lun+1):
	for x in list(comb(range(1,lun+1),i)):
		combinazioni.append(x)

#-------#

if choice == "l":
	for element in combinazioni:
		if type(element) == int:
			lista = []
			index = combinazioni.index(element)
			del(combinazioni[index])
			lista.append(dic[str(element)])
			combinazioni.insert(index, lista)
		elif type(element) == tuple:
			lista = []
			index = combinazioni.index(element)
			del(combinazioni[index])
			for n in element:
				lista.append(dic[str(n)])
			combinazioni.insert(index, lista)

#-------#

combinazioni.sort()

for x in combinazioni:
	if choice == 'l':
		print " ".join(x)
	elif choice == 'n' and type(x) == tuple:
		for n in x:
			print n,
		print
	else:
		print x

#-------#

output = open('combinazioni.txt','w')
for x in combinazioni:
	if choice == 'l':
		output.write(" ".join(x))
		output.write("\n")
	elif choice == 'n' and type(x) == tuple:
		for n in x:
			output.write("%d " % n)
		output.write("\n")
	else:
		output.write(x)
output.close()

#-------#

print "\n I risultati sono stati stampati nel file \"combinazioni.txt\"."

print "\n END\n"
