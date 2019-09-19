from jarbas_house import House
from jarbas_house.devices import Bulb
from jarbas_house.devices.tplink import scan_kasa
from jarbas_house.devices.magic_home import scan_magichome

house = House()
# only add what you have devices for
# note, ewelink mosquito killer is also considered a light bulb
house.add_scanner(scan_magichome)
house.add_scanner(scan_kasa)

for d in house.scan_devices():
    # turn all light bulbs off
    if isinstance(d, Bulb) and d.is_off:
        print("turning light on {device}".format(device=d))
        d.turn_on()