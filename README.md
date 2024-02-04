# Installation

# UNIX/Linux

If you have the pip3 module installed
```sh
python3 -m pip install -r requirements.txt
```
If you do not have the pip3 module installed please run the following commands before installing.

```sh
# On Debian based distros
sudo apt install python3-pip
#Fedora
sudo yam install python3-pip
#Arch virtual enviorments should not require root or sudo
python -m venv path/to/venv
# Arch w/ Pacman, should not require root or sudo
pacman -S python-pip

``` 

#MacOS
```sh
python -m pip install-r requirements.txt
```

# Windows
```sh
py -m pip install -r requirements.txt
```

# Usage

```sh
cd ./my_folder/
python main.py
```
