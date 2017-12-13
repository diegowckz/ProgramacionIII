#rap them
#tapeth
#apth
#wrap/try
#sap tray
#87ap9th
#apothecary
#aleht   x
#happy them x
#tarpth  x
#apt  x
#peth  x
#tarreth  x
#ddpdg  x

import re

patron = '[a-z1-9]||[1-9a-z]||[a-z]\w'
palabras = ['rap them' , 'tapeth' , 'apth' , 'wrap/try' , 'sap try' , '87ap9th' , 'apothecary']
patron1 = '[.AA]\S'
palabras1 = ['aleht' , 'happy them' , 'tarpth' , 'apt' , 'peth' , 'tarreth' , 'ddpdg']


for palabra in palabras:
    if re.search(patron, palabra):
                print("La palabra " + palabra + " cumple.")

    else:
                print("La palabra " + palabra + " no cumple.")

for palabra1 in palabras1:
    if re.search(patron1, palabra1):
                print("La palabra " + palabra1 + " cumple.")

    else:
                print("La palabra " + palabra1 + " no cumple.")