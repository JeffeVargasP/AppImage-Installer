# AppImage-Installer

AppImage-Installer is a simple tool to install AppImages in Linux.

Using AppImage-Installer is very simple, just run the following command:

```python3 main.py```

## LIBRARIES

All libs is default in python3

- subprocess
- pathlib

## EXPLANIATION

The code follow the next steps:

check_appimage function will use the lib pathlib to check if the path AppImage exists then will ignore, if not will create the folder with ```Path.mkdir()``` .

check_appimage_desktop function will use the lib pathlib to check if the path for the shortcut exists then will ignore, if not will create the folder with ```Path.mkdir()``` .

install_appimage function will made all the process works, verifying if .AppImage file exists, AppImage folder (Installation folder) and the shortcut folder, if not will create the folders, then will copy the .AppImage file to the AppImage folder and will create the shortcut in the shortcut folder.

The shortcut must to be downloaded, renamed and moved to the shortcut folder by the user.

## LICENSE

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

Made with ❤️, 😡 and 😴 by [JeffeVargasP](https://github.com/JeffeVargasP)