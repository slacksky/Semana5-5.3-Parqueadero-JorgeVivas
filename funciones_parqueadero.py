from collections import namedtuple
import stack_puestos as stack
import typing

Puesto = namedtuple('Puesto','nivel numero')


def crear_parqueadero(numero_niveles,cantidad_puestos):
  parqueadero=stack.Stack()
  cont_niveles=1
  while cont_niveles <= numero_niveles:
    cont_vehiculos=1
    while cont_vehiculos <= cantidad_puestos:
      parqueadero.push(Puesto(cont_niveles,cont_vehiculos))
      cont_vehiculos+=1
    cont_niveles+=1
  ##aqui se genera la "matriz" del parking
  print(parqueadero.length())
  return parqueadero

def obtener_puesto_libre(parqueadero):
  puesto= parqueadero.top()
  parqueadero.pop()
  return puesto

def ingresar_puesto_libre(parqueadero,puesto):
  parqueadero.push(puesto)

  


def ocupar_puesto_parqueadero(placa,parqueadero,vehiculos_en_parqueadero): 
  if vehiculos_en_parqueadero.get(placa)==None:
    puesto_libre=obtener_puesto_libre(parqueadero)
    vehiculos_en_parqueadero[placa]=puesto_libre
    return placa,puesto_libre
  else:
    return None

def liberar_puesto_parqueadero(placa,parqueadero,vehiculos_en_parqueadero):
  if vehiculos_en_parqueadero.get(placa)!=None:
    puesto_libre=vehiculos_en_parqueadero[placa]
    del vehiculos_en_parqueadero[placa]
    ingresar_puesto_libre(parqueadero,puesto_libre)

vehiculos_en_parqueadero=typing.Dict[str, str]

"""inspired by the teachers's IOW review logic

def verificar_puesto_libre(parqueadero):
  if parqueadero.length() > :
    return True
  else:
    return False

def verificar_placa(placa):
  if placa.find("-") == 3:
    separados =placa.split("-")
    if len(separadaos[1]== 3)and len(separados[0])==3 and separados[1].isnumeric() and separados[0].isalpha():
      return True
  return False


## 
def menu_funciones():
  print("para ingresar el vehiculo ingrese 1")
  print("para retirar el vehiculo ingrese 2")
  print("para sailr ingrese salir")

  accion=1
  while accion== 1 or accion== 2:
    if"""