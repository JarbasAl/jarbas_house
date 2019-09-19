from jarbas_house import House
from jarbas_house.devices.ewelink import scan_ewelink
from jarbas_house.devices.tplink import scan_kasa
from jarbas_house.devices.magic_home import scan_magichome

from time import sleep

house = House()
# only add what you have devices for
house.add_scanner(scan_magichome)
house.add_scanner(scan_kasa)
house.add_scanner(scan_ewelink)

devices = []
for device in house.scan_devices():
    devices.append(device)
    if hasattr(device, "random_color_cycle"):
        print("Randomly Cycling colors in {device}".format(device=device))
        device.random_color_cycle()
    elif hasattr(device, "color_cycle"):
        print("Cycling colors in {device}".format(device=device))
        device.color_cycle()
    elif hasattr(device, "blink"):
        print("Blinking {device}".format(device=device))
        device.blink()
    # if you are evil just toggle all devices in a loop, possibly damaging stuff connected to smart plugs
    # don't do that

sleep(30)

for device in devices:
    device.reset()
