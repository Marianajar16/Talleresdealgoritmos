from datetime import date
from datetime import datetime
#-----------------------------------fecha del sistema
#dia actual
today = date.today()
#fecha hoy
dia_act=today.day
mes_act=today.month
año_act=today.year
#entradas
fecha_nacimiento=input("Digite en este formato la fecha de nacimiento: año/mes/dia ")
(año,mes,dia)=fecha_nacimiento.split("/")
año_nac=int(año)
mes_nac=int(mes)
dia_nac=int(dia)
#caja negra
#______________________________edad
edad=0
if(mes_act==mes_nac):
    if(dia_nac>=dia_act):
        edad=año_act-año_nac
    else:
        edad=(año_act-año_nac)
elif(mes_act>mes_nac):
    edad=(año_act-año_nac)
else:
    edad=(año_act-año_nac)-1
#________________________________signo sodiacal 
signo=""
if((dia_nac>=21 and mes_nac>=1) and (dia_nac<=19 and mes_nac<=2)):
    signo="Acuario"
elif((dia_nac>=20 and mes_nac>=2) or (dia_nac<=19 and mes_nac<=3)):
    signo="Piscis"
elif((dia_nac>=21 and mes_nac>=3) or (dia_nac<=20 and mes_nac<=4)):
    signo="Aries"
elif((dia_nac>=21 and mes_nac>=4) or (dia_nac<=21 and mes_nac<=5)):
    signo="Tauro"
elif((dia_nac>=22 and mes_nac>=5) or (dia_nac<=21 and mes_nac<=6)):
    signo="Geminis"
elif((dia_nac>=22 and mes_nac>=6) or (dia_nac<=22 and mes_nac<=7)):
    signo="Cancer"
elif((dia_nac>=23 and mes_nac>=7) or (dia_nac<=23 and mes_nac<=8)):
    signo="Leo"
elif((dia_nac>=24 and mes_nac>=8) or (dia_nac<=22 and mes_nac<=9)):
    signo="Virgo"
elif((dia_nac>=23 and mes_nac>=9) or (dia_nac<=22 and mes_nac<=10)):
    signo="Libra"
elif((dia_nac>=23 and mes_nac>=10) or (dia_nac<=21 and mes_nac<=11)):
    signo="Escorpion"
elif((dia_nac>=22 and mes_nac>=11) or (dia_nac<=21 and mes_nac<=12)):
    signo="Sagitario" 
elif((dia_nac>=22 and mes_nac>=12) or (dia_nac<=20 and mes_nac<=1)):
    signo="Capricornio"
#salida

print(f"Siendo que su fecha de nacimiento es {fecha_nacimiento}, su signo zodiacal corresponde a {signo} y tiene {edad} años")


