#! /usr/bin/env python3
from BarItem import BarItem
import time
import subprocess



class Time(BarItem):
    output_format = ""
    output = {}

    def __init__(self, output_format="%H:%M"):
        BarItem.__init__(self, "Time")
        self.output['name'] = "Time"
        self.output_format = output_format
        self.update()

    def update(self):
        time_string = time.strftime(self.output_format)
        self.output['full_text'] = time_string

    def get_json(self):
        return self.output

class Battery(BarItem):
    output = {}

    def __init__(self, number=0):
        BarItem.__init__(self, "Battery")
        self.output['name'] = "Battery"
        self.number = number

    def update(self):
        args = ("cat", "/sys/class/power_supply/BAT0/energy_full")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        bat_full = popen.stdout.read().decode("utf-8").strip()
        args = ("cat", "/sys/class/power_supply/BAT0/energy_now")
        popen = subprocess.Popen(args, stdout=subprocess.PIPE)
        popen.wait()
        bat_now = popen.stdout.read().decode("utf-8").strip()
        percentage = '%.1f' % ((int(bat_now) / int(bat_full)) * 100)
        self.output['full_text'] = "Battery: " + percentage + "%"

    def get_json(self):
        return self.output

