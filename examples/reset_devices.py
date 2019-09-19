from jarbas_house import House
from jarbas_house.devices.tplink import scan_kasa
from jarbas_house.devices.magic_home import scan_magichome

house = House()
# only add what you have devices for

house.add_scanner(scan_magichome)
house.add_scanner(scan_kasa)

for d in house.scan_devices():
    # reset everything in the house to default state
    print("reseting {device} to default state".format(device=d))
    d.reset()
