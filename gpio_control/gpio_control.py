import RPi.GPIO as GPIO
import json

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

GPIO.output(3, GPIO.HIGH)
GPIO.output(5, GPIO.HIGH)
GPIO.output(7, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)
GPIO.output(19, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)


def turn_on_relays():
    with open("api/resources/relays.json", "r") as json_file:
        data = json.load(json_file)

    for i in range(len(data)):
        if data[i]['state'] == "on":
            GPIO.output(int(data[i]['relay_number']), GPIO.LOW)


def turn_off_relays():
    with open("api/resources/relays.json", "r") as json_file:
        data = json.load(json_file)

    for i in range(len(data)):
        if data[i]['state'] == "off":
            GPIO.output(int(data[i]['relay_number']), GPIO.HIGH)