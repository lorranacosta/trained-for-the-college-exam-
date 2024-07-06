#ej9 #parcial

#len


num = int(input("ingrese numero:"))

#con el numero directo 2968395

largo = len (str (num))

print ("")

ult = num%10
#num% para dar el ultimo numero
mid = (num//(10**(largo//2)))%10
#para sacar la cifra
pri = (num//(10**(largo -1)))
#-1 para sacar el digito del medio y menos uno
print ("El numero ingresado tiene" , largo, "cifras")
print ("La primera cifra es {}, la ultima es {} y la central es {} " .  format (pri, ult, mid))


