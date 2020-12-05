# import RPi.GPIO as GPIO
import json

from api.resources.get_resources import get_all_relays


# GPIO.setmode(GPIO.BOARD)
#
# GPIO.setup(3, GPIO.OUT)
# GPIO.setup(5, GPIO.OUT)
# GPIO.setup(7, GPIO.OUT)
# GPIO.setup(11, GPIO.OUT)
# GPIO.setup(13, GPIO.OUT)
# GPIO.setup(15, GPIO.OUT)
# GPIO.setup(19, GPIO.OUT)
# GPIO.setup(21, GPIO.OUT)
#
# GPIO.output(3, GPIO.LOW)
# GPIO.output(5, GPIO.LOW)
# GPIO.output(7, GPIO.LOW)
# GPIO.output(11, GPIO.LOW)
# GPIO.output(13, GPIO.LOW)
# GPIO.output(15, GPIO.LOW)
# GPIO.output(19, GPIO.LOW)
# GPIO.output(21, GPIO.LOW)

def turn_on_relays():
    with open("raspberryAPI/api/resources/relays.json", "r") as json_file:
        get_relays = json.load(json_file)


    print(get_relays)


turn_on_relays()
