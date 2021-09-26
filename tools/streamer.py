#!/usr/bin/python

import os
from time import sleep
import sys
home = os.environ['HOME']

os.system("sudo modprobe bcm2835-v4l2")

while True:
  while (os.system("ls /dev/video* 2>/dev/null") != 0) or (os.path.isfile(home + "/companion/start_video.sh")):
    sleep(5)
  arg_count = len(sys.argv)
  if arg_count == 1:
    params = "$(cat /home/pi/vidformat.param)"
  elif arg_count == 2:
    params = "$(cat /home/pi/{0})".format(sys.argv[1])
  elif arg_count == 3:
    params = "$(cat /home/pi/{0}) {1}".format(sys.argv[1], sys.argv[2])
  else:
    params = " ".join(sys.argv[1:]))
  os.system(home + "/companion/scripts/start_video.sh " + params)
  sleep(2)


