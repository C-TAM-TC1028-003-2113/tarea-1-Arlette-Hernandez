def main():
    # escribe tu código abajo de esta línea
    saldomes= float(input("Dame el saldo del mes anterior: "))
    ingresos= float(input("Dame el ingreso: "))
    egresos= float(input("Dame el egreso: "))
    numcheques= int(input("Dame el numero de cheques expedidos: "))
    cheque= numcheques*13
    descuento= 9.46875
    saldofinal= (saldomes-cheque)+(ingresos-egresos)
    saldomes= saldofinal-descuento
    print("Dame el saldo final del mes:",saldomes)




if __name__ == '__main__':
    main()
