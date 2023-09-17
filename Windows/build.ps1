#  ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#  ┃                                                          ┃
#  ┃      Checking if python has been installed on local      ┃
#  ┃               machine. If not, install it.               ┃
#  ┃                                                          ┃
#  ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

if (-Not (Test-Path -Path "C:\Python39")) {
    Write-Output "Python is not installed. Installing..."
    # Download the Python installer
    Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe" -OutFile "python-installer.exe"
    # Run the installer
    Start-Process -FilePath "python-installer.exe" -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1"
    # Clean up the installer
    Remove-Item "python-installer.exe"
} else {
    Write-Output "Python is already installed."
}

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
