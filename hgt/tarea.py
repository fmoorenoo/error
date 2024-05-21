class Tarea:
    def __init__(self, id:int, tarea:str, estado:bool) -> None:
        self.id     = id
        self.tarea  = tarea
        self.estado = estado

    # Métodos CRUD
    def read(self) -> str:
        return self.id, self.tarea, self.estado

    def update(self):
        pass

    def delete(self):
        pass