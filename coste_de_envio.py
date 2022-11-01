total = 0

coste_envio = 0

print ("¡Hola! Siga las instrucciones para obtener el coste total de su pedido\n")

total = int (input ("Indique a continuación el precio del producto: "))

while True:
  
  localizacion = (input ("\nSi reside dentro de la península ibérica o baleares escriba 'peninsula'. Si reside en canarias escriba 'canarias' y en el caso de residir fuera de España escriba 'fuera': "))
  
  if localizacion == "canarias":
    break
  elif localizacion == "fuera":
    break
  elif localizacion == "peninsula":
    break
  else:
    print ("\nOps... no te he entendido. Prueba otra vez.\n")

if localizacion == "peninsula":
  coste_envio += 5
  print ("\nCoste de envío peninsular aplicado!")

elif localizacion == "canarias":
  coste_envio += 10
  print ("\nCoste de envío a canarias aplicado!")

else:
  coste_envio += 15
  print ("\nCoste de envío internacional aplicado!")


print (f"\nEl total de su pedido es de {total + coste_envio} €")
