#!/usr/bin/env python3

import sys, socket, getpass, platform, psutil, time, calendar
from cpuinfo import cpuinfo
from colored import fg, bg, attr

#Getting specs

HostName = socket.gethostname()
UserName = getpass.getuser()
Ver = platform.release()
Sys = platform.system()
Bit = platform.processor()
OS = platform.linux_distribution()

i = 7

Lines = [Line.rstrip('\n') for Line in open('UbuntuSpec.settings')]

Options = [S for S in Lines if not S.startswith('#')]

Color1 = Options[0].split(': ')[1]
Color2 = Options[1].split(': ')[1]
Color3 = Options[2].split(': ')[1]
ColorTitle = Options[3].split(': ')[1]
ColorAt = Options[4].split(': ')[1]
ColorInfo = Options[5].split(': ')[1]

#18
c = 0
while 


