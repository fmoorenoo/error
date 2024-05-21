from tarea import Tarea

class ListaTareas:
    LIMITCHAR = "|&&|"

    def __init__(self):
        self.tareas = []

    def agregar(self, tarea:Tarea):
        self.tareas.append(tarea)

    def read(self):
        result = ""
        for tarea in self.tareas:
            result += tarea
            if tarea != self.tareas[-1]:
                result += self.LIMITCHAR
        return result
    
    def load(self, data:str):
        tareas = data.split(self.LIMITCHAR)
        for tarea in tareas:
            self.tareas.append(tarea)
    
    def update(self, tarea:Tarea, id:int, tarea:str, estado:bool):
        for a in self.tareas:
            if a == tarea:
                a.update(id, tarea, estado)
                break

    # def delete(self, tarea:Tarea, id:int, tarea:str, estado:bool):
    #     for a in self.tare:
    #         if a == alumno:
    #             a.delete()
    #             break

    # def __str__(self):
    #     return self.read()
    
    # def __len__(self):
    #     return  self.alumnos.__len__()
    
    # def __getitem__(self, index):
    #     return self.alumnos[index]
    
    # def __setitem__(self, index, value):
    #     self.alumnos[index] = value

    # def __delitem__(self, index):
    #     del self.alumnos[index]

    # def __iter__(self):
    #     return self.alumnos.__iter__()
    
    # def __next__(self):
    #     return self.alumnos.__next__()
    
    # def __contains__(self, item):
    #     return item in self.alumnos
    
    # def __eq__(self, other):
    #     return self.alumnos == other.alumnos
    
    # def __ne__(self, other):
    #     return self.alumnos != other.alumnos