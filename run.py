import time
from api.api import app
from gpio_control.gpio_control import turn_on_relays

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


