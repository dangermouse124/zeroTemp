Facing the front:
1 - gnd
2 - data
3 - vcc

1. At the command prompt, enter: sudo nano /boot/config.txt, then add this to the bottom of the file:

dtoverlay=w1–gpio

2. Exit Nano, and reboot the Pi (sudo reboot)

3. Log in to the Pi again, and at the command prompt enter sudo modprobe w1–gpio

4. Then enter sudo modprobe w1-therm

5. Change directories to the /sys/bus/w1/devices directory by entering: cd /sys/bus/w1/devices

6. Now enter ls to list the devices:

7. Now enter cd 28-XXXXXXXXXXXX (change the X’s to your own address)

Enter cat w1_slave which will show the raw temperature reading output by the sensor: