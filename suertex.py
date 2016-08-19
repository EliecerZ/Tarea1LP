import re

def ofecha(string):
    return re.sub('[^\d]','/',string)

def separamiles(numero):
    ptos=(len(numero)-1)/3 #si el numero 1000, retorna 1, si es 1000000 devuelve 2
    i=1
    while ptos>0:




def sep(archivo):
    print "Comprobando sintaxis de funciones \separamiles{} y \ofecha"
    sm=False
    of=False
    patron=re.compile(r'\\separamiles{}')
    pat=re.compile('ofecha{}')
    for linea in archivo:
        #print linea
        if (patron.match(linea))!=None:
            sm=True
        elif (pat.match(linea))!=None:
            of=True

    return

#######################

su=open("suertex.txt","r")
sep(su)
fecha='(^.|\s)([0-2][0-9]|3[01]).(0?[0-9]|1[0-2]).[0-9][0-9][0-9][0-9](^.|\s)' #search para fecha
miles='(^.|\s)(\d+)(^.|\s)'
su.close()

print ofecha('21;12!2014')
print separamiles('12345678')
raw_input("Cualquier tecla para salir:\n")
exit()