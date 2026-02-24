from diccio_agenda import hecha, tareas, titulo

def marcar_hechas (tareas,titulo):
    if tareas == titulo:
        hecha = True
    else:
        print("No hecha")

if __name__ =="__main__":
    marcar_hechas(tareas,titulo)