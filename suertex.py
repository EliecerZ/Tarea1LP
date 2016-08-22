import re
'''''''''
ofecha(fecha)
    Transforma los caracteres de separacion de fecha
    a los correspondientes "/"
'''''''''
def ofecha(fecha):
    return re.sub('[^\d]','/',fecha)

'''''''''
separamiles(numero)
    Inserta puntos de separacion cada 3 digitos en un
    numero sin dichos puntoss.
'''''''''

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

'''''''''
html_nproy(text, archivo)
    Transoforma el texto dentro de la funcion nproy
    a codigo tipo html.
'''''''''

def html_nproy(text,archivo):
    archivo.write('<!DOCTYPE HTML>\n<head>')
    archivo.write('<title>'+text+'</title>\n</head>\n')
    return None

'''''''''
reem_html(patron, string)
    Aplicando la funcion sub de expresiones regulares
    se procede a cambiar el patron enn el string por
    su formato en html
'''''''''
def reem_html(patron, string):
    if patron==(r"\\titulo{.+}"):
        titulo=re.findall("{.+}",string)
        titulo=titulo[0].strip("}").strip("{")
        return re.sub(patron,"<h1>"+titulo+"</h1>\n",string) ####comprobar si se salta 1 o 2 lineas


#######################

su=open("suertex.txt","r")
ou=open("output.html","w")
fecha='(^.|\s|{|})([0-2][0-9]|3[01])([^\w\s])(0?[0-9]|1[0-2])([^\w\s])[0-9][0-9][0-9][0-9](^.|\s|}|{)' #search para fecha
miles='(^.|\s)(\d+)(^.|\s)'

aplis=False
aplio=False
sepa=re.compile(r'\\separamiles{}')
ofe=re.compile(r'\\ofecha{}')
np=re.compile(r'\\nproy{.+}')
for linea in su:
    if (sepa.match(linea))!=None:
        aplis=True
    elif (ofe.match(linea))!=None:
        aplio=True
    elif (np.match(linea))!=None:
        st=(np.match(linea)).group()
        text=re.findall("{.+}",st)
        text=text[0]
        text=text.strip("{").strip("}")
        break

html_nproy(text,ou)

ou.write('<body>')
fc=re.compile(r"\\fc{.+}")
fn=re.compile(r"\\fn{.+}")
tlo=re.compile(r"\\titulo{.+}")
ini=re.compile(r"\\inicio{lista_(punteada|enumerada)}")
fin=re.compile(r"\\fin{lista_(punteada|enumerada)}")
item=re.compile(r"\\item{.+}")

for linea in su:
    if (tlo.match(linea)!=None):
        t=((tlo.match(linea)).group()) #idealmente, el comando titulo
        f=re.findall(r"\\fc{[^}]*}",t) #lista con coincidencias de fc
        if f != []:
            text = fc.findall("{.+}")
            for comando in text:
                title=reem_html(r"\\fc{[^}]*}",)
        #no encontramos nada:
        title=reem_html(r"\\titulo{.+}", t)
        ou.write(title)
    if aplis: ####corregir expresion regular
        fec=re.search(fecha, linea)
        if fec != None:
            fec=(fec.group()).strip("}")
            fec=re.sub(fecha, ofecha(fec), linea)
            print fec
    if aplio:
        mil=re.search(miles, linea)
        if mil != None:

print ofecha('21;12!2014')
print separamiles('1234567')
su.close()