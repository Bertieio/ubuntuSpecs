#!/usr/bin/env python3

import socket, getpass, platform, psutil, time, calendar
from colored import fg, bg, attr

Disk = psutil.disk_usage('/')

DiskTotal = round(Disk[0] / 1000000000,2)
DiskTaken = round(Disk[1] / 1000000000,2)
DiskFree = round(Disk[2] / 1000000000,2)
DiskPercent = Disk[3] 

BootTime =  psutil.boot_time()
NowTime = calendar.timegm(time.gmtime())

UpTime = NowTime - BootTime


intervals = (
    ('W', 604800),  # 60 * 60 * 24 * 7
    ('D', 86400),    # 60 * 60 * 24
    ('H', 3600),    # 60 * 60
    ('M', 60),
    ('S', 1),
    )

def display_time(seconds, granularity=4444):
    result = []

    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            if value == 1:
                name = name.rstrip('s')
            result.append("{} {}".format(round(value,0), name))
    return ', '.join(result[:granularity])


FormedTime =  display_time(UpTime)

HostName = socket.gethostname()
UserName = getpass.getuser()
Ver = platform.release()
Sys = platform.system()
Bit = platform.processor()
OS = platform.linux_distribution()

#Colors! Use the ANCI codes found here https://github.com/dslackw/colored

#ubuntu
DarkColor = 201
MedColor = 135
LightColor = 15

FontColor = 201
AtColor = 15
#
print("{}                          ./+o+-".format(fg(DarkColor)))
print("{}                  yyyyy-{} -yyyyyy+".format(fg(MedColor), fg(DarkColor)))
print("{}               ://+//////{}-yyyyyyo       {}{}{}@{}{}".format(fg(MedColor), fg(DarkColor), fg(FontColor), UserName, fg(AtColor), fg(FontColor), HostName))
print("{}           .++{} .:/++++++/-.{}+sss/`       {}OS: {} {} {}".format(fg(LightColor), fg(MedColor), fg(DarkColor),fg(FontColor), OS[0], OS[1], OS[2]))
print("{}         .:++o:{}  /++++++++/:--:/-       {}Kernel: {} {} {}".format(fg(LightColor), fg(MedColor),fg(FontColor), Bit, Sys, Ver))
print("{}        o:+o+:++.{}`..```.-/oo+++++/      {}Disk: {}\{} GB - {}%".format(fg(LightColor), fg(MedColor), fg(FontColor), DiskFree, DiskTotal, DiskPercent ))
print("{}       .:+o:+o/.          {}`+sssoo+/     {}Uptime: {}".format(fg(LightColor), fg(MedColor), fg(FontColor), FormedTime))
print("{}  .++/+:{}+oo+o:`            {} /sssooo.".format(fg(MedColor), fg(LightColor), fg(MedColor)))
print("{} /+++//+:{}`oo+o              {} /::--:.".format(fg(MedColor), fg(LightColor), fg(MedColor)))
print("{} \+/+o+++{}`o++o              {} ++////.".format(fg(MedColor), fg(LightColor), fg(DarkColor)))
print("{}  .++.o+{}++oo+:`            {} /dddhhh.".format(fg(MedColor), fg(LightColor), fg(DarkColor)))
print("{}       .+.o+oo:.         {} `oddhhhh+".format(fg(LightColor), fg(DarkColor)))
print("{}        \+.++o+o`{}`-````.:ohdhhhhh+".format(fg(LightColor), fg(DarkColor)))
print("{}         `:o+++ {}`ohhhhhhhhyo++os:".format(fg(LightColor), fg(DarkColor)))
print("{}           .o:`{}.syhhhhhhh/{}.oo++o`".format(fg(LightColor), fg(DarkColor), fg(LightColor)))
print("{}               /osyyyyyyo{}++ooo+++/".format(fg(DarkColor), fg(LightColor)))
print("{}                   ````` {}+oo+++o\:".format(fg(DarkColor), fg(LightColor)))
print("{}                          `oo++.".format(fg(LightColor)))
