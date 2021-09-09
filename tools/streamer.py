#!/usr/bin/python

import os
from time import sleep
import sys
home = os.environ['HOME']

os.system("sudo modprobe bcm2835-v4l2")

while True:
  while (os.system("ls /dev/video* 2>/dev/null") != 0) or (os.path.isfile(home + "/companion/start_video.sh")):
    sleep(5)
  if len(sys.argv) == 1:
    params = "$(cat /home/pi/vidformat.param)"
  elif len(sys.argv) == 2:
    params = "$(cat /home/pi/{0})".format(sys.argv[1])
  else:
    params = " ".join(sys.argv[1:]))
  os.system(home + "/companion/scripts/start_video.sh " + params
  sleep(2)


