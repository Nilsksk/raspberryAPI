import time
from api.api import app
from gpio_control.gpio_control import turn_on_relays

if __name__ == '__main__':
    app.run()

while(True):
    time.sleep(5)
    turn_on_relays()


