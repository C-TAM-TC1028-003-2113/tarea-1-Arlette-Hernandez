def main():
    # escribe tu código abajo de esta línea
    palabras= int(input("Dame el número de palabras: "))
    descuento=0.10
    restodeldescuento=9
    entero=1000
    costoporpalabra=60/500
    descuentofinal= costoporpalabra*descuento
    costo=descuentofinal*restodeldescuento
    costofinal=costo*entero
    print("El costo del descuento es:",costofinal)






if __name__ == '__main__':
    main()
