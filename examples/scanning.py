from pprint import pprint

from jarbas_house import House

from jarbas_house.devices.ewelink import scan_ewelink
from jarbas_house.devices.tplink import scan_kasa
from jarbas_house.devices.magic_home import scan_magichome
from jarbas_house.devices.scan import scan_bluetooth, scan_wifi

house = House()
# only add what you have devices for
#house.add_scanner(scan_wifi)
#house.add_scanner(scan_bluetooth)
house.add_scanner(scan_magichome)
#house.add_scanner(scan_kasa)
#house.add_scanner(scan_ewelink)


for d in house.scan_devices():
    # do something fun with the devices
    pprint(d.as_dict)