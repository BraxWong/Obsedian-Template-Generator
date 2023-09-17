#!/bin/sh

#  ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#  ┃                                                          ┃
#  ┃      Checking if python has been installed on local      ┃
#  ┃               machine. If not, install it.               ┃
#  ┃                                                          ┃
#  ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

if command -v python3 &> /dev/null ; then
  echo "Python is installed."
else
  sudo apt-get update
  sudo apt-get install python3
fi

#  ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#  ┃                                                          ┃
#  ┃             #Installing project dependencies             ┃
#  ┃                                                          ┃
#  ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

pip install customtkinter
pip install tk
pip install pathvalidate
pip install pyinstaller

#  ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#  ┃                                                          ┃
#  ┃         #Building the project using pyinstaller          ┃
#  ┃                                                          ┃
#  ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

cd ..
pyinstaller --noconfirm --onedir --windowed src/main.py
