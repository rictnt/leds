#!/usr/bin/env python
import RPi.GPIO as GPIO
#Configuramos los pines nombre del archivo led24on.py
GPIO.setmode(GPIO.BCM)
#Pin 24 como salida
GPIO.setup(24,GPIO.OUT)
#Pin ON
GPIO.output(24,False)
