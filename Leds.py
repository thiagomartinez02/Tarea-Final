import time


numero = 0
leds = [27,22,5,6]
boton = 17 
chan_list= [leds]


def binario(numero):
    return bin(numero)[2:].zfill(4)


print("GPIO.setmode(GPIO.BCM)")
print("GPIO.setup(boton, GPIO.IN)")
print("GPIO.setup(chan_list, GPIO.OUT)")


while True:
    print("if GPIO.input(boton) == GPIO.HIGH")
    bnumero = binario(numero)
    if numero == 9:
        numero = 0.
    else:
        numero = numero + 1
    for b in range(4):
        led = leds[b]
        valor = int(bnumero[b])
        print("GPIO.output", led, valor)

