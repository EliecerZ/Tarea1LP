import re

def ofecha(fecha): #revisa el string y lo devuelve con el formato dd/mm/aaaas
    busqueda=re.findall('[^\d]',fecha)
    print busqueda
    f=fecha.strip().split(busqueda[0])
    if busqueda[0]!=busqueda[1]:
        sep=f[1].strip().split(busqueda[1])
        f[1]=sep[0]
        f.append(sep[1])
    string="/".join(f)
    return string

def separamiles(mil):
    l1=[] #chica
    lg=[] #grande
    n=len(mil)
    while n!=0:
        return None





suertex=open("suertex.txt","r")

print ofecha('12-12!1234')


