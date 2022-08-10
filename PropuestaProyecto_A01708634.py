import time #importamos la librería tiempo para poder utilizar el comando de time.sleep()

def romanoEntero(num) -> int : #Función programada para pasar un número romano a entero
#     # Aquí se crea un hash map para ponerle valores numéricos a los caracteres específicos de los numeros romanos
    lookup = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    
    # En la variable N guardamos el tamaño del numero romano
    N = len(num)
    # La variable "i" representa que la cuenta iniciará desde el último caracter del numero romano
    i = N-1
    # La variable result se usará para guardar el valor del caracter en cuestión
    result = 0
    
    # El while nos sirve para que el valor de i llegue hasta 0 (hasta el principio del numero romano)
    while i >= 0:
        # Este if nos dice que si "i" no se encuentra en el último caracter y si el valor del numero romano en la posición "i" es menor al valor del numero romano adyacente a la
        # derecha, entonces al valor del resultado se le restará el valor del numero romano en la posición "i", finalmente restamos 1 a "i", para proseguir al siguiente numero.
        if i < N-1 and lookup[num[i]] < lookup[num[i+1]]:
            result -= lookup[num[i]]
            i-= 1
        # Este else nos sirve para sumar nuestro valor del numero romano en la posición "i" al resultado y restamos 1 a "i", para proseguir al siguiente numero. 
        else: 
            result += lookup[num[i]]
            i-= 1
    return result 

def enteroRomano(num): #Función programada para pasar un número entero a romano
    # Aquí hacemos un metodo diferente, declarando dos arreglos asignando todos los valores posibles que existen en la numerologia romana y poniendo el valor correspondiente en la
    # misma posicion de otro arreglo, declaramos una variable igual a 12, esto para que "i" se puede posicionar en el ultimo valor de cada arreglo
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
    i=12
    
    #Creamos una variable string para guardar el resultado en dicha variable
    result = ''
    
    # Mientras que el numero que se ingrese para convertir no sea igual a 0 y no sea un numero negativo, se llevará a cabo el ciclo
    while num != 0 and num > 0:
        # Si el valor del arreglo values en la posicion i es menor o igual al numero que se ingreso, entonces sumarle a la variable de resultado el caracter romano correspondiente
        # a la posicion i del arreglo roman. Si no es así (else) restarle uno a la variable "i" indicando que continuamos con el siguiente valor del arreglo values, para así
        # compararlo nuevamente con el numero que se ingresó
        if values[i] <= num:
            result += roman[i]
            num = num - values[i]
        else:
            i -= 1
    return result

def menu(): # Función que despliega un menú
    print ("1. Conversión de número romano a entero")
    print ("2. Conversión de número entero a romano")
    print ("3. Salir \n")
    
def main(): #Función en el cual se llaman las funciones necesarias programadas anteriormente para correr el código apropiadamente
    
    continua = True # Declaración de una variable tipo booleana para facilitar el proceso de avisarle al while cuando terminar
    while continua: # Este while correra mientras la variable continua sea verdadera
        menu()  # Se despliega el menu
        time.sleep(1) # Espera por un segundo antes de correr la siguiente instrucción del código
        opcion = int(input("Ingrese la opción que desee: \n")) # Declaración de variable que le permite ingresar un valor de tipo numérico al usuario
        if opcion == 1: #Si la opción que ingresó el usuario es igual a 1, significa que el usuario quiere transformar un número romano a entero, por lo cual se llamará a la función
            # de romanoEntero para que se lleve a cabo el proceso correspondiente
            numRomano = input("Ingrese el número romano que desee convertir: ") #Aquí se le pide al usuario ingresar el número romano deseado
            print ("Tu resultado es:", romanoEntero(numRomano),"\n")
            time.sleep (2) # Espera por 2 segundos antes de correr la siguiente instrucción del código
            seguir = input("¿Deseas continuar? ¿Si o No? ") # Aquí le pregunta al usuario si desea continuar y el usuario debe escribir Si o No
            if seguir in ["no","NO","No","nO"]: #Si la respuesta es NO, se termina el ciclo
                continua = False
            
        elif opcion == 2: #Si la opción que ingresó el usuario es igual a 2, significa que el usuario quiere transformar un número entero a romano, por lo cual se llamará a la función
            # de enteroRomano para que se lleve a cabo el proceso correspondiente
            numEntero = int(input("Ingrese el número entero que desee convertir: ")) #Aquí se le pide al usuario ingresar el número entero deseado
            print (enteroRomano(numEntero),"\n")
            time.sleep (2) # Espera por 2 segundos antes de correr la siguiente instrucción del código
            seguir = input("¿Deseas continuar? ¿Si o No? ") # Aquí le pregunta al usuario si desea continuar y el usuario debe escribir Si o No
            if seguir in ["no","NO","No","nO"]: #Si la respuesta es NO, se termina el ciclo y finaliza el programa
                continua = False
            
        elif opcion == 3: #Si la opción que ingresó el usuario es igual a 3, significa que el usuario no desea continuar y el programa se termina
            print ("Gracias por su tiempo. ¡Nos vemos pronto!")
            continua = False
        else:
            print ("Su opción no es válida. Intente de nuevo. \n") #Aquí se pone este else por si en el caso que el usuario no registró ninguno de las opciones disponibles, se
            # impirma el mensaje y reiterará el ciclo hasta que el usuario elija una opción disponible 
            time.sleep (2) # Espera por 2 segundos antes de correr el ciclo while de nueva cuenta
main() #Se llama a la función main 