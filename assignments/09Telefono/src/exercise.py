def main():
    # escribe tu código abajo de esta línea
    mensajes=int(input("Dame el número de mensajes: "))
    megas=float(input("Dame el número de megas: "))
    minutos=int(input("Dame el numero de minutos¨: "))

    msj=0.80*mensajes
    m=0.80*megas
    min=0.80*minutos

    mensualidad= msj+m+min
    print("El costo mensual es:",mensualidad)




if __name__ == '__main__':
    main()
