titulo =""
hecha =  ""
tareas = ["Estudiar Python","Hacer ejercicio","Leer paginas"]
def diccio_agenda(titulo,tareas,hecha):
 for titulo in tareas:
    titulo = titulo + tareas
 if hecha == True:
   return True
 else: 
    return False
 if __name__ == "__main__" :
    diccio_agenda("titulo", "tareas","hecha")