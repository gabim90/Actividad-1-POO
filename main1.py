from actividad1 import email
from actividad1 import manejadorEmail

if __name__ == '__main__':
    idcuenta='alumno'
    tipodominio='gmail'
    dominio='com'
    contraseña='12345'
    usuario= email(idcuenta,dominio,tipodominio,contraseña)
    usuario.crearCuenta()
    usuario.modificarContraseña()
    otromail= input('Ingrese un mail')
    partes= otromail.split("@")
    partes2= partes[1].split(".")
    for i in range (len(partes2)):
        partes.append(partes2[i])
    partes.remove(partes[1])
    partes = email(partes[0], partes[1], partes[2],'13445')
    lista = manejadorEmail()
    lista.testEmail()
    m = 0
    dominio = input('Ingrese dominio: ')
    cant = lista.controlDom(dominio,m)
    print("La cantidad de dominios es igual a ",cant)
