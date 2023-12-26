import subprocess
import optparse
import re

def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change")
    return parser.parse_args()

def change_mon_mode(user_interface):
    subprocess.call(["airmon-ng","start",user_interface])

def control_new_mode(interface):

    iwconfig = subprocess.check_output(["iwconfig", interface])
    new_mode = re.search(r"\w\w\w\w:\w\w\w\w\w\w\w", str(iwconfig))

    if new_mode:
        return new_mode.group(0)
    else:
        return None

print("ChangeMonMode started !")

(user_inputs,arguments) = get_user_input()
user_interface = user_inputs.interface
change_mon_mode(user_interface)

