#!/usr/bin/env python

import time
import os
import automationhat as auto

# Turn the power light on
auto.light.power.on()

# Function that triggers relay one to ON
def relay_on():
    print("Turning the relay " + state + "!")
    print("The relay will stay on until you launch me again and turn it off.")
    print("Press CTRL+C to exit now.")
    while True:
        auto.light.warn.on()
        auto.relay.one.on()

# Fucntion that triggers relay one to OFF
def relay_off():
    print("Turning the relay " + state + "!")
    auto.light.warn.off()
    auto.relay.one.off()

state = raw_input("Do you want the relay ON or OFF? ")

try:
    if (state == "on") or (state == "ON") or (state == "On"):
        relay_on()
    elif (state == "off") or (state == "OFF") or (state == "Off"):
        relay_off()
        time.sleep(1)
        print("\nGoodbye!\n")
    else:
        print("Sorry, you must say on or off!\n")
        print("Exiting!\n")
except (KeyboardInterrupt, SystemExit):
    print("\nExiting!\n")
    auto.light.power.off()
    os._exit(1)