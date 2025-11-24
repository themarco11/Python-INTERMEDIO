from usuario import Usuario

class administrador(Usuario): 
    def __init__(self, nombre: str, correo: str, permisos: list[str]):
        super().__init__(nombre, correo)
        self.permisos = permisos

        def mostrar_info(self) -> str:
            return f"Administrador: {self.nombre}, correo: {self.correo}, permisos: {','.join(self.permisos)}"