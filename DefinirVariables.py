#DefinirVariables

#var=2
#var2=2

#estructura de decision

#if (var==1):
#    print('se cumplio')
#elif(var==5):
#    print('se cumplio')
#else:
#    print('no se cumplio')

#var="hello uala"

#print(var.replace('l','6'))


#En base a un numero que se ingrese, me devuelva si es mayor o menor a 100
"""
try:
    var= int(input("Ingrese algo:"))

    if (var>=100):

        print('el numero ingresado es MAYOR o igual que 100')
        
    elif (var<=100):

        print('el numero ingresado es MENOR o igual que 100')
except:
    print ("no es un numero")
"""


#para el jueves hacer una calculadora, que se ingresen 2 valores por teclado int o float
"""
try:
    valor1 = float(input("Ingrese el primer número "))
    valor2 = float(input("ingrese el segundo número ")) 
    opcion = input("Seleccionar opcion de operatoria: 1 para suma, 2 para resta, 3 para multiplicación, 4 para division, 5 para salir: ")
    if opcion == "1":
        total = valor1 + valor2
        print("La suma es: ", total)
    elif opcion == "2":
        total = valor1 - valor2 
        print("La resta es: ", total)
    elif opcion == "3":
        total = valor1 * valor2
        print("La multiplicación da: ", total)
    elif opcion == "4":
        total = valor1 / valor2
        print("La division es: ", total)
    elif opcion == "5":
        print("Programa terminado")
    else: 
        print("opción incorrecta")
except:
    print ("no es un numero")
"""

#Estructura FOR
''''
lista=[
            ['matias acuna', '26', 'mendoza'],
            ['maxi miranda', '25', 'cordoba']
        ]

lista.append([input () for col in range (4)])

print (lista)
'''

lista1=[]
for i in range (1, 11,1):
    lista.append()

for numero in lista:
    res=numero%2
    if(res!=0):
        print(f"El numero {numero} es impar")
    else:
        print(f"El numero{numero} es par")  

