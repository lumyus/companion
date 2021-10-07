# companion

This repository is the Blue Robotics version of the [ArduPilot/companion](https://github.com/ArduPilot/companion) repository. This is the code that runs on the Raspberry Pi in the BlueROV2. Currently, this repository only provides an implementation for the Raspberry Pi Computer.

# Compatibility + Caveats

This branch **unofficially** enables installing the companion software onto an RPi3B+ or RPi4 device. It uses the updates from https://github.com/bluerobotics/companion/pull/284, but has been rebased onto version 0.0.29 of companion.

The main companion software is currently undergoing a major rewrite, part of which will include official support for RPi4. This branch allows running most of the **current** companion, but is unlikely to be updated beyond the current state (because official support and better software are on the way).

To make this installation work **the [terminal over browser](https://www.ardusub.com/reference/companion/terminal-over-browser.html) and [git](https://www.ardusub.com/reference/companion/git.html) pages from the web interface were REMOVED.** Consequentially, direct control of the Raspberry Pi must be done using SSH or a keyboard+monitor, and transferring to e.g. the `dvl` branch is not a simple process.

# Installation

1. Connect a microSD card to your computer (at least 4GB)
2. Use [Raspberry Pi imager](https://www.raspberrypi.org/software/) to flash Raspberry Pi OS Lite onto the SD card
3. Eject the SD card and re-insert it
4. Add an empty file 'ssh' to the SD card, to enable SSH communication
5. Eject the SD card and insert it into the Raspberry Pi
6. Power up the Raspberry Pi and make an ethernet connection to your computer
7. SSH in with the default credentials (if on Unix/running MDNS, run `ssh pi@raspberrypi.local` and type in the password `raspberry` - Windows requires determining the IP address) - it is recommended to set a new password using the `passwd` command.
8. Run `sudo raspi-config` to set your `Localisation` (navigate with arrow keys, use `Enter`/`Return` to confirm)
9. Reboot when prompted, and [set up a wifi connection](https://www.raspberrypi.org/documentation/computers/configuration.html#wireless-networking-command-line)
10. Download and run the installation script (takes quite a while, possibly 30-90 minutes)
    ```
    wget https://raw.githubusercontent.com/ES-Alexander/companion/setup-clean2/scripts/install.sh
    chmod +x install.sh
    ./install.sh
    ```
11. Reboot to complete (e.g. `sudo reboot`)
