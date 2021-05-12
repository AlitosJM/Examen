def es_simetrico(n: int = 1) -> bool:
    '''
    La función recibe un número entero n y retorna bool verdadero
    si la suma de la primera mitad de la cifra es iggual a la segunda mitad. E
    Entrada n es una cifra par y  debera estar
    acotada en el rango 10<=n<=10,000,000 \n
    :param n:
    :return bool:
    '''

    # Estas excepciones revisan que el dato sea tipo entero y que este dentro del rango determinado
    if type(n) is not int:
        raise TypeError("Error de tipo, solo enteros")
    if n < 10 or n > 10E6:
        raise ValueError("Número debe ser 10<= n <= 10,000,000")

    mi_numero = str(n)  # El número n se convierte a cadena para poder manejarlo como una lista o array
    len_num = len(mi_numero)
    resto = len_num % 2  # Se determina la longitud de la lista es par(0) o impar (1)
    r = False

    # Si la cifra es par la cifra y mayor a dos dígitos
    if not resto and len_num > 2:
        limite = len_num//2   # variable limite para poder acceder a la lista por mitad izquierda y derecha
        suma0 = [int(numero) for numero in mi_numero[:limite]]  # mitad izquiera
        suma1 = [int(numero) for numero in mi_numero[-limite:]]  # mitad derecha
        r = True if sum(suma0) == sum(suma1) else False  # si las sumas de las mitades es igual el retorno es verdadero

    #  Si la cifra son solo dos dígitos se comprueba si son iguales, si lo son, se retorna verdadero
    elif len_num == 2:
        r = True if int(mi_numero[0]) == int(mi_numero[1]) else False
    # La cifra es impar, y se retorna una excepción al usuario
    else:
        raise Exception("Número impar")
    return r


if __name__ == '__main__':
    try:
        n0 = 101110
        print("¿Es simétrico?", es_simetrico(n0))
    except TypeError as e1:
        print("Error 1: {}".format(str(e1)))
    except ValueError as e2:
        print("Error 2: {}".format(str(e2)))
    except SyntaxError as e3:
        print("Error 3: {}".format(str(e3)))
    except Exception as e4:
        print("Error 4: {}".format(str(e4)))

