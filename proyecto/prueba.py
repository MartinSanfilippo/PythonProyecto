class Cliente:
    def __init__(self, nombre:str, telefono: int, direccion, email:str, cuit:int):
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
        self.cuit = cuit
    
    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(f"El numero de telefono fue cambiado a: {self.telefono}")    
    
    def actualizar_direccion (self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"La direccion a sido modificada a: {self.direccion}")
    
    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"El email fue cambiado a: {self.email}")   

    def __str__(self):
        return (f"Cliente: {self.nombre}\n"
                f"Teléfono: {self.telefono}\n"
                f"Dirección: {self.direccion}\n"
                f"Correo Electrónico: {self.email}\n"
                f"Cuit: {self.cuit}")
                