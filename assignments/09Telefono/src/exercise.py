def main():
    # escribe tu código abajo de esta línea
    msj=int(input("Dame el número de mensajes: "))
    m=float(input("Dame el número de megas: "))
    minutos=int(input("Dame el numero de minutos¨: "))

    mensajes=0.80*msj
    megas=0.80*m
    min=0.80*minutos

    costomensual= mensajes+megas+min
    print("El costo mensual es:",costomensual)

if __name__ == '__main__':
    main()
