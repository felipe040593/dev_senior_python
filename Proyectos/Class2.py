def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
inputUsuario = input("Ingrese el primer número: ")

isFloat = is_float(inputUsuario)

if not isFloat:
    inputUsuario = input("El número no es valido, ingresa el primer número nuevamente: ")
    
numero1 = float(inputUsuario)

numero2 = float(input("Ingresa el segundo número: "))

