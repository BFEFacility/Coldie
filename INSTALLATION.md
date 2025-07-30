# The full installation guide of Coldie

This file serves as the **official installation guide** of Coldie. The best part of **Coldie** is that mitmproxy can be installed in a wide range of systems and ways. These tutorials are for **GNU/Linux (or Linux)-based operating systems** and for **Windows-based operating systems** but it should work on any system and instance (such as Docker and pipx) **mitmproxy** supports. They include the simplest way to install the binary. These tutorials are simple and informative. Lastly, **mitmweb** is used instead of **mitmproxy** since **mitmweb** is easier to setup, use and debug in some instances than **mitmproxy**. This also includes the setup of the installation and some debugging tips!

## Prerequisites

1. Windows/Linux/macOS machine to install, setup and run the Coldie proxy (or any other **machine** supported by mitmproxy)
2. Android/iOS phone to play the game using the Coldie proxy (or any other phone that supports **Bomber Friends** and **proxies**)
3. File editor (IDE recommended) to setup the proxy code to your needs in a guided way (the editing of the Python code which will be in a guided way)

## Recommended Knowledge

1. Greater than or equal to Very basic knowledge of Python to edit variables in your own to be able to play with the code

**This will sound very hard but it is a one-time setup, it will leave you more satisfied and happier (with your work and time) than any mod APK will! Not to mention, this is the only choice of hacking in iOS devices.**

## Installation on Linux or GNU/Linux systems

**This system is different from Windows, this tutorial will further assume you have a terminal! Terminals can be found anywhere on the GUI and CLI.**

1. Firstly, install **Python 3** and **pip**. If your OS doesn't use **Python 3** (it's not installed due to package or library dependencies), install it. **Coldie** uses Python 3 for it's syntax, features (ternary operator was since Python 2.5) and the shebang. Install it from your package manager or from: https://www.python.org/downloads/.
2. You need to install **Coldie** first to have the **mitmproxy** script and the exact version of **mitmproxy** (and it's dependencies) needed. Go to this URL: **https://github.com/sandStoop/Coldie** and click the Code button. After doing that, click the **Download ZIP** button.
3. It will download the ZIP in your preferred directory or it will have you choose the path. The recommended path would be **Documents**. Keep the name *as is*, **Coldie-main.zip** to ensure this tutorial is smoother.
4. You should unzip the file to find everything of the main branch inside of it. You can do it through the file manager or the terminal. If you want to do it in the terminal, go to the directory you download **Coldie** to and run this: `unzip Coldie-main.zip` or unzip it from your file manager (likely by right clicking here and clicking **Extract To**).
5. Open the **Coldie-main** folder in your terminal by running: `cd ./Coldie-main`
6. After doing that, run this command: `pip install -r requirements.txt` (recommended: `pip3 install -r requirements.txt`). This command uses **pip**, Python's package manager which installs, updates and manages libraries and dependencies to **install** every package (library) which includes all of it's dependencies listed in the file. **Keep in mind the file uses a very special format to get all the libraries and dependencies of the Coldie file and you cannot do this to every file!**

For step 5, if this error appears:

error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
    python3-xyz, where xyz is the package you are trying to
    install.
    
    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.
    
    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.
    
    See /usr/share/doc/python3.11/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.

That means your system is a fork of another system and the system is externally managed. You should check this StackOverflow post which provides many solutions to this issue: https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-every-time-i-use-pip-3. I'd recommend setting up a Virtual Environment (search it up or find out how to do in the provided post) to fix this error and the breakage of such packages. The most reckless yet laziest solution would be to use the *--break-system-packages* flag which could risk breaking your Python installation or OS. However, the rule of thumb is that if you see any errors about conflicts, remove the installed packages and nothing will have ever happened.

7. You are all done! To set the proxy up, run this command: `mitmweb --script ./Coldie.py` or `mitmweb -s ./Coldie.py`. You only need the binary now since every relevant package (and CLI tool) the code uses has been installed. You can now remove the other files which are unnecessary for the actual tool to run except the binary and all of it's packages. **Keep the proxy on when it should be on and off when it should be off when playing**
   
RECOMMENDED. You can put the binary in a easy-to-remember place which doesn't get cleaned up. You can put it in `/bin` or the directory of the binaries.

## Installation on Windows systems

**The installation of Windows operating systems will be added later due to further testing of it's implementation of mitmproxy and it's Python API. Please wait!**

For Macintosh systems, the steps of installations are the exact same as in Linux. If Python is not installed, use this command: `brew install python`. Your version of Python (you can have many, just use pip3 to install all packages and Python 3 for all operations! 

All you need to know for the installation is that you simply need to have **Python** installed and **mitmproxy**, which most systems have for installation.
