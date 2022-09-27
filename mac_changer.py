import subprocess
import optparse
import regex as re


def get_usr_input():
    prase_obj = optparse.OptionParser()
    prase_obj.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    prase_obj.add_option("-m", "--mac", dest="MAC address", help="New MAC address")
    prase_obj.add_option("-h", "--help", dest="help", help="Help")

    return prase_obj.parse_args()


def change_mac(user_interface, new_mac):
    print("[+] Changing MAC address for " + user_interface + " to " + new_mac)
    subprocess.call(["ifconfig", user_interface, "down"])
    print("[+] Interface " + user_interface + " is down")
    subprocess.call(["ifconfig", user_interface, "hw", "ether", new_mac])
    print("[+] MAC address for " + user_interface + " is changed to " + new_mac)
    subprocess.call(["ifconfig", user_interface, "up"])
    print("[+] Interface " + user_interface + " is up")


def control_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")


print("MAC Changer Started!")
(user_input, arguments) = get_usr_input()
change_mac(user_input.interface, user_input.MAC_address)
final_mac = control_mac(str(user_input.interface))

if final_mac == user_input.MAC_address:
    print("[+] MAC address was successfully changed to " + final_mac)
else:
    print("[-] MAC address did not get changed")
