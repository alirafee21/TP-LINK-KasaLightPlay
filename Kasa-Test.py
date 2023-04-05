import asyncio
from kasa import *

from kasa.exceptions import SmartDeviceException


# found_devices = asyncio.run(Discover.discover())
# address = []
# for dev in found_devices:
#     address.append(dev)
# if address:

def toggle_light():
    try:
        bulb = SmartBulb("192.168.2.238")
        asyncio.run(bulb.update())
        # asyncio.run(bulb.turn_off())
        state = bulb.is_on
        if state:
             asyncio.run(bulb.turn_off())
        else:
            asyncio.run(bulb.turn_on())
        #
        # asyncio.run(bulb.turn_on())
    except SmartDeviceException as e:
        print(e)

toggle_light()

# if __name__ == "main":
#     toggle_light()
