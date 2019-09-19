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
# brightness will go up and down
for device in house.scan_devices():
    devices.append(device)
    if hasattr(device, "beacon"):
        print("Beacon mode {device}".format(device=device))
        device.beacon()

sleep(30)

for device in devices:
    device.reset()
