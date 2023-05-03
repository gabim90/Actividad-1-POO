import csv

class email:
    __idcuenta= ''
    __tipodom= ''
    __dominio= ''
    __contrasena= ''

    def __init__(self,idcuen, dom, tipdom,con):
        self.__idcuenta = idcuen
        self.__dominio = dom
        self.__tipodom = tipdom
        self.__contrasena = con
 
    def getDominio(self):
        return self.__dominio
    
    def crearCuenta(self):
        nombre = input('Ingrese su nombre:') 
        print('Estimado',nombre,'le enviaremos mensajes a la direccion',
               self.__idcuenta + '@' + self.__dominio + '.' + self.__tipodom)
        
    def modificarContraseña(self):
        conNueva = input ('Ingrese su contraseña actual:')
        if conNueva == self.__contrasena:
            self.__contrasena == input ('Ingrese nueva contraseña:')
        else:
            print ('Contraseña Incorrecta')
            self.modificarContraseña()
    
class manejadorEmail:

    def __init__(self):
        self.__listaEmail = []

    def agregarEmail(self,unEmail):
        self.__listaEmail.append(unEmail)

    def testEmail(self):
        archivo = open('Correo.csv')
        reader = csv.reader(archivo,delimiter=',')
        for fila in reader:
            idcuen = fila[0]
            dom = fila[1]
            tipdom = fila[2]
            con = fila[3]
            unEmail = email(idcuen,dom,tipdom,con)
            self.agregarEmail(unEmail)
        archivo.close()

    def controlDom(self,dom,canti):
        i = 0
        for i in range(len(self.__listaEmail)):
            if(self.__listaEmail[i].getDominio() == dom):
                canti = canti + 1
        return(canti)