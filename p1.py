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
         5-Terminar Compra
         6-Salir""")
    opc=(input("Selecciona que sushi vas a llevar \n"))
    
    os.system("cls")
    time.sleep(1)

    if opc == "1":
        cantidadPika=int(input("Cuanta cantidad de Pikachu Roll vas a llevar \n"))
        os.system("cls")
        time.sleep(1)
        print("Selecciona en el Menu si quieres seguir Comprando o terminar Compra o Salir " )
        
    
    
    elif opc == "2":
        cantidadOtaku=int(input("Cuanta cantidad de Otaku Roll vas a llevar \n"))
        os.system("cls")
        time.sleep(1)
        print("Selecciona en el Menu si quieres seguir Comprando o terminar Compra o Salir " )

    

    elif opc == "3":
        cantidadPulpo=int(input("Cuanta cantidad de Pulpo Venenoso Roll vas a llevar \n"))
        os.system("cls")
        time.sleep(1)
        print("Selecciona en el Menu si quieres seguir Comprando o terminar Compra o Salir " )
        
    

    elif opc == "4":
        cantidadAnguila=int(input("Cuanta cantidad de Anguila Eléctrica Roll vas a llevar \n"))
        os.system("cls")
        time.sleep(1)
        print("Selecciona en el Menu si quieres seguir Comprando o terminar Compra o Salir " )

    
    elif opc == "5":
        print("Terminar Compra")
        TieneCodg=input("Tiene codigo de Descuento \n a)Si \n b)No \n")
        if TieneCodg == "b":
                os.system("cls")
                time.sleep(1)
                print("No tiene Codigo de Descuento")
                print(f"""
***************Boleta*************
Toltal Productos : {CantidadProducto}
**************************************
Pikachu Roll : {cantidadPika}
Otaku Roll : {cantidadOtaku}
Pulpo Venenoso Roll : {cantidadPulpo}
Anguila Eléctrica Roll : {cantidadAnguila}
**************************************
Subtotal por pagar : {subtotal}
Descuento por código : 0
TOTAL : {subtotal}""")
                break
        elif TieneCodg == "a":
            os.system("cls")
            time.sleep(1)
            codigo=input("Ingresa Codigo de Descuento \n")
            if codigo == "soyotaku":
                print(f"Tienes un 10% de Descuento")
                print(f"""
***************Boleta*****************
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
                break
            else:
                print('codigo invalido presione "x" para reintentar')
                codop=input('Ponga X para Reintentar \n')
                if codop == 'x' or codop == 'X':
                    print('muy bien')
                    while codop == 'x' or codop == 'X':
                      code= input('ingrese el codigo \n')
                      if code == 'soyotaku':
                          os.system("cls")
                          time.sleep(1)
                          print('bien tienes un descuento del 10%')
                          print(f"""
***************Boleta*****************
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
                          break
        break   
                       
    else:
        print("Salio del Menu que tenga un Buen Dia")
        break

    precioPika=int(PikachuRoll*cantidadPika)
    precioOtaku=int(OtakuRoll*cantidadOtaku)
    precioPulpo=int(PulpoVenenosoRoll*cantidadPulpo)
    precioAguila=int(AnguilaEléctricaRoll*cantidadAnguila)
    CantidadProducto=int(cantidadPika+cantidadOtaku+cantidadPulpo+cantidadAnguila)
    subtotal=int(precioPika+precioOtaku+precioPulpo+precioAguila)
    Descodigo=0.10
    Descuento=float(subtotal*Descodigo)
    Total=float(subtotal-Descuento)
