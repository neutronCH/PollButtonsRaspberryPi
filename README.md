# PollButtonsRaspberryPi
A small script in python to poll buttons on a raspberry pi

# How to use
* Install package python3-rpi.gpio and screen
  ```
  sudo apt-get update
  sudo apt-get install python3-rpi.gpio
  sudo apt-get install screen
  ```
* Create a startup script
  ```
  #!/bin/sh

  #start screen
  su - pi -c "/usr/bin/screen -dmS Poll_Buttons"
  
  #send commands to screen
  su - pi -c "/usr/bin/screen -S Poll_Buttons -X stuff $'cd /home/pi/poll_buttons\n'"
  su - pi -c "/usr/bin/screen -S Poll_Buttons -X stuff $'python3 poll_buttons.py\n'"
  ```
* Add following line to /etc/rc.local
  ```
  sudo bash /home/pi/autostart.sh
  ```