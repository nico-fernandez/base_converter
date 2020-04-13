print("¿Qué base querés convertir a las demás?")
print()
print("D = Decimal")
print("B = Binario")
print("O = Octal")
print("H = Hexadecimal")
print()
b = input("Ingrese una base: ")
print()



# En este if quiero convertir de Binaria a las demás bases
if b == 'B':
    print("Ingrese el número en la base que eligío: ")
    num = input()
    dec = int(num, 2) # Convierto primero a decimal
    print("En base decimal: ", dec)
    print("En base hexadecimal: ", format(dec, 'x'))
    print("En base octal: ", format(dec, 'o'))

# En este if quiero convertir de Hexadecimal a las demás bases
elif b == 'H':
    print("Ingrese el número en la base que eligío: ")
    num = input()
    dec = int(num, 16) # Convierto primero a decimal
    print("En base decimal: ", dec)
    print("En base binaria: ", format(dec, 'b'))
    print("En base octal: ", format(dec, 'o'))

# En este if quiero convertir de Hexadecimal a las demás bases
elif b == 'O':
    print("Ingrese el número en la base que eligío: ")
    num = input()
    dec = int(num, 8) # Convierto primero a decimal
    print("En base decimal: ", dec)
    print("En base hexadecimal: ", format(dec, 'x'))
    print("En base binaria: ", format(dec, 'b'))

# En este if quiero convertir de Decimal a las demás bases.
elif b == 'D':
    print("Ingrese el número en la base que eligío: ")
    num = int(input())
    print("En base binaria: ", format(num, 'b'))
    print("En base hexadecimal: ", format(num, 'x'))
    print("En base octal: ", format(num, 'o'))

else:
    print("No se puede realizar la conversion")