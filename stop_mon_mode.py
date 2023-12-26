import subprocess
import optparse
import re

def get_user_input():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change")
    return parser.parse_args()


def get_mon_mode(user_interface):
    subprocess.call(["airmon-ng","stop",user_interface+"mon"])


(user_inputs,arguments) = get_user_input()
user_interface = user_inputs.interface
get_mon_mode(user_interface)
