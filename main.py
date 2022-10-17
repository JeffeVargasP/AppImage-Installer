#   WELCOME TO THE APPIMAGE INSTALLER           #
#   This script will install AppImage files     #
#   to your Linux system.                       #
#   Created by:                                 #
#   - @JeffeVargasP                             #
#   License:                                    #
#   MIT                                         #
#   Version:                                    #
#   1.0                                         #
#   Date: 10/17/2022                            #

# Importing modules
import subprocess
from pathlib import Path

# Defining variables
home = Path.home()
download = f"{home}/Downloads"
appimage = f"{home}/AppImage"
appimage_desktop = f"{home}/.local/share/applications"

# Defining functions
def check_appimage():
    print("Checking if AppImage folder exists...")
    if Path(appimage).exists():
        print("AppImage folder exists!")
    else:
        print("AppImage folder does not exist, creating it...")
        Path(appimage).mkdir()
        print("AppImage folder created!")

def check_appimage_desktop():
    print("Checking if AppImage desktop folder exists...")
    if Path(appimage_desktop).exists():
        print("AppImage desktop folder exists!")
    else:
        print("AppImage desktop folder does not exist, creating it...")
        Path(appimage_desktop).mkdir()
        print("AppImage desktop folder created!")

def install_appimage():

    check_appimage()
    check_appimage_desktop()
    
    print("Looking for AppImage files in Downloads folder...")
    
    if (Path(download).glob("*.AppImage")):
        
        print("AppImage files found!")
        
        for file in Path(download).glob("*.AppImage"):

            filename = file.name.replace(".AppImage", "")

            print(f"Found {file.name}!")
    
            print(f"Creating a folder for {file.name}...")
    
            if (Path(f"{appimage}/{filename}")).exists():
                
                print(f"{filename} folder already exists!")

                print(f"Moving {file.name} to {appimage}...")
                file.replace(f"{appimage}/{filename}/{file.name}")

            else:
            
                Path(f"{appimage}/{filename}").mkdir()
            
                print(f"Moving {file.name} to {appimage}/{filename}...")

                file.replace(f"{appimage}/{filename}/{file.name}")
    
            print(f"Creating a desktop file for {file.name}...")
    
            if (Path(f"{appimage_desktop}/{filename}.desktop")).exists():
                
                print(f"{filename}.desktop file already exists!")

            else:

                with open(f"{appimage_desktop}/{file.name}.desktop", "w") as desktop_file:
                    desktop_file.write(f"""[Desktop Entry]

Name={filename}

Exec={appimage}/{file.name}/{file.name}

Icon={appimage}/{file.name}/{filename}.svg

Type=Application

Categories=Utility;Application;""")

            print(f"Waiting for {filename}.svg be pasted...")
            subprocess.check_output(f"open {appimage}/{filename}", shell=True)
            confirm = input("Press enter when you have pasted the icon: ")
            subprocess.check_output(f"killall nautilus", shell=True)
    else:

        print("No AppImage files found!")
        print("Exiting...")
        exit()

if __name__ == "__main__":
    install_appimage()