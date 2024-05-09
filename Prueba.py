import os
import time


# Precios de shushi 
PikachuRoll= 4500
OtakuRoll= 5000
PulpoVenenosoRoll = 5200
AnguilaEléctricaRoll = 4800

cantidadPika=0
cantidadOtaku=0
cantidadPulpo=0
cantidadAnguila=0

print("Bienvenidos a la Tienda de Sushi ")
while True:
    print("""Menu de Shushi
         1- Pikachu Roll $4500
         2- Otaku Roll $5000
         3- Pulpo Venenoso Roll $5200
         4- Anguila Eléctrica Roll $4800
         5-Salir""")
    opc=(input("Selecciona que sushi vas a llevar \n"))

    os.system("cls")
    time.sleep(2)

    if opc == "1":
        cantidadPika=int(input("Cuanta cantidad de Pikachu Roll vas a llevar \n"))
    
    
    if opc == "2":
        cantidadOtaku=int(input("Cuanta cantidad de Otaku Roll vas a llevar \n"))
    

    if opc == "3":
        cantidadPulpo=int(input("Cuanta cantidad de Pulpo Venenoso Roll vas a llevar \n"))
    

    if opc == "4":
        cantidadAnguila=int(input("Cuanta cantidad de Anguila Eléctrica Roll vas a llevar \n"))
    
    elif opc == "5":
        print("Salio del Menu que tenga Buen dia ")
        break

    precioPika=int(PikachuRoll*cantidadPika)
    precioOtaku=int(OtakuRoll*cantidadOtaku)
    precioPulpo=int(PulpoVenenosoRoll*cantidadPulpo)
    precioAguila=int(AnguilaEléctricaRoll*cantidadAnguila)
    CantidadProducto=int(cantidadPika+cantidadOtaku+cantidadPulpo+cantidadAnguila)
    subtotal=int(precioPika+precioOtaku+precioPulpo+precioAguila)
    Descuento=int(subtotal*soyotaku)
    Total=int(subtotal-Descuento)
    soyotaku=0.10


while True:
    codigo=input("Ponga el Codigo de Descuento \n")
    if codigo != "soyotaku":
        codigo=input("Codigo de Descuento Incorrecto deseas volver a intentar si/no \n")

    if codigo == "si":
        codigo=input("ingresa codigo de descuento \n")
    elif codigo == "no":
        print("No tiene Codigo de Descuento")
        break

if codigo == "soyotaku":
    print("Si tiene Descuento de 10%")

os.system("cls")
time.sleep(2)

print(f"""***************Boleta*************
      Toltal Productos : {CantidadProducto}
      **************************************
      Pikachu Roll : {cantidadPika}
      Otaku Roll : {cantidadOtaku}
      Pulpo Venenoso Roll : {cantidadPulpo}
      Anguila Eléctrica Roll : {cantidadAnguila}
      **************************************
      Subtotal por pagar : {subtotal}
      Descuento por código : {Descuento}
      TOTAL : {Total}""")