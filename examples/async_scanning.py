import time

from jarbas_house import House
from jarbas_house.devices.ewelink import scan_ewelink
from jarbas_house.devices.tplink import scan_kasa
from jarbas_house.devices.magic_home import scan_magichome
from jarbas_house.devices.scan import scan_bluetooth, scan_wifi

house = House(verbose=False)
# only add what you have devices for
house.add_scanner(scan_wifi)
house.add_scanner(scan_bluetooth)
house.add_scanner(scan_magichome)
house.add_scanner(scan_kasa)
house.add_scanner(scan_ewelink)


# add reaction handlers

def on_new(device):
    print("New device {device}".format(device=device))


house.on_new_device(on_new)


def on_lost(device):
    print("Lost device {device}".format(device=device))


house.on_device_lost(on_lost)

# update a timestamp or something
# house.on_device_seen(func)

# something changed in the device
# house.on_device_updated(func)

house.start()
try:
    while True:
        # Do some cool stuff!
        time.sleep(5)
except KeyboardInterrupt:
    house.stop()
    house.remove_handlers()
