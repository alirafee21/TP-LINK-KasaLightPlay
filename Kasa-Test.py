import asyncio
from kasa import *
# from pyHS100.smartdevice import SmartDeviceException
from kasa.exceptions import SmartDeviceException
# found_devices = asyncio.run(Discover.discover())
# address = []
# for dev in found_devices:
#     address.append(dev)
# if address:


try:
    bulb = SmartBulb("192.168.2.238")
    asyncio.run(bulb.update())
    # asyncio.run(bulb.turn_off())
    asyncio.run(bulb.turn_on())
except SmartDeviceException as e:
    print(e)
