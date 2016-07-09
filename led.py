#Teste porta Raspberry
#LED

#tempo que fica aceso ou apagado
tempo = 2

#Biblioteca da GPIO
import RPi.GPIO as GPIO

#Biblioteca de tempo
import time
GPIO.setmode(GPIO.BOARD)

#Saída: pino 12
GPIO.setup(12,GPIO.OUT)

#rotina para acender o led
def acendeled(pino_led):
    GPIO.output(pino_led,1)
    return
#rotina para apagar o led
def apagaled(pino_led):
    GPIO.output(pino_led,0)
    return
#Inicia loop
while(1):
  #Acende o led
  acendeled(12)
  #Aguarda segundo
  time.sleep(tempo)
  #apaga o led
  apagaled(12)
  #Aguarda meio segundo e reinicia o processo
  time.sleep(tempo)
