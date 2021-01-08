from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from storageManager.jsonMode import *
class DropDatabase(Instruccion):
    def __init__(self, id, tipo, existe, opcion, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.id = id
        self.opcion = opcion
        self.existe = existe

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        bandera = False
        listaBD = showDatabases()
        for bd in listaBD:
            if bd == self.id:
                bandera = True
                break

        #LA BD se encontro
        if self.existe and bandera:
            print(f"La Base de Datos: {self.id} ha sido eliminada")
            arbol.consola.append(f"Se encontro la base de datos: {self.id} ha sido eliminada")
            dropDatabase(self.id)
            arbol.eliminarBD(self.id)
        elif self.existe and not bandera:
            arbol.consola.append(f"La Base de datos: {self.id} no existe")
        elif not self.existe and bandera:
            arbol.consola.append(f"La Base de Datos: {self.id} ha sido eliminada")
            dropDatabase(self.id)
            arbol.eliminarBD(self.id)
        elif not self.existe and not bandera:
            error = Exception("XX000", "Semantico", "Error Base de Datos no existe", self.linea, self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())

    def traducir(self, tabla, controlador, arbol):
        codigo = 'DropDatabase.DropDatabase("' + self.id + '", None, ' + str(self.existe) + ', ' + str(self.opcion) + ', "'
        codigo += self.strGram + '", ' + str(self.linea) + ', ' + str(self.columna) + ').ejecutar(tabla, arbol)\n'
        #print(codigo)
        return None
