from proyecto.prueba import Cliente

def main():
    cliente1 = Cliente("Martin", 114123456, "Av.Avenida 123", "hola@hotmail.com", 2324877987)
    print(cliente1)
    cliente1.actualizar_telefono(123456789)
    cliente1.actualizar_direccion("Avenida 1245")
    cliente1.actualizar_email("holahola@gmail.com")
    print(f"El cliente a sido actualizado a:\n {cliente1}")

if __name__ == "__main__":
   main()

