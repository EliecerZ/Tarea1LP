import re

def ofecha(string):
    return re.sub('[^\d]','/',string)

def separamiles(numero): #12,345,678
    numero=numero[::-1]
    lista= re.findall("\d{3}", numero)
    reem="".join(lista)
    if len(reem)!=len(numero):
        string=numero.replace(reem,"")
        lista.append(string)
    fin = ".".join(lista)
    fin=fin[::-1]
    return fin


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
print separamiles('10000000000000000')