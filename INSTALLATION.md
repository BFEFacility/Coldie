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
8. **Ctrl+C** the proxy since there is more work to do (**setup**, **phone setup** etc.)
   
RECOMMENDED. You can put the binary in a easy-to-remember place which doesn't get cleaned up. You can put it in `/bin` or the directory of the binaries.

## Installation on Macintosh systems

For Macintosh systems, the steps of installations are the exact same as in Linux. If Python is not installed, use this command: `brew install python`. Your version of Python (you can have many, just use pip3 to install all packages and Python 3 for all operations! 

## Setup

**You will need to edit the Python binary. For people who have Python experience, skip this section. For those who need a guided experience, proceed.**

1. Open the Python binary (file) in your preferred text editor. If it's an IDE or a text editor that supports Python, this phase will be better and easier to do.
2. You need to edit the variables. **A big chunk of them** are *False* since they are not enabled by default (the script checks if the variables are False and does not do anything if so). You need to change the falsy values (booleans) to truthy values!
3. This is the current chunk of code you need to change which only includes the variables that make an effect. Comments are included:

```
apiURL = "https://e1e6.playfabapi.com" # The URL of the API
apiCloudScriptURL = apiURL + "/Client/ExecuteCloudScript" # The cloud script's API endpoint which manages the execution of essential scripts

retrieveData = "getInitialData" # The only cloud script function which gets the initial data of the game (account included) which spans to a lot of hard-to-decode JSON full of metadata
bomberium = False # Amount of bomberium (visual)
freespins = False # Amount of free (non-VIP) spins (visual)
vipspins = False # Amount of 150 gem (VIP) spins (visual)
seasonPass = False # Is season pass enabled? (cannot claim rewards, fashion show rewards doubled and VIP icon is shown)
XP = False # XP which determines the level (not the rank) which gives you pretty good multiplayer benefits
gems = False # Gems (known as EL) (visual)
medals = False # Medals, also known as trophies in the game code (visual, chests can't be claimed (visual unless you've reached that medal range), matchmaking changes (unconfirmed), not on leaderboard) 
alwaysBots = False # Always match with bots; no match or medal limitations -> TODO: Test it in higher medal range
costumes = False # Get all costumes (it's a string value by design and requirement), this has been disabled since it has an extremely high chance of a kickloop (instant kick from any type of play, different from a ban) (AFFECTED, UNRECOMMENDED)
recommendedVersion = True # Always sets your version of the game to the recommended version of the game which allows you to play the game in any version of Bomber Friends (does not bring back features, just allows play)

fashionPointHandler = "addFashionPoints" # The cloud function which handles fashion show point claiming after an entry has been made.
fashionPoints = 100 # The number of fashion points (maximum: 100, smart server-side validation refuses bad values and causes kick)
ad = True # Doubles the number of fashion points

tutorialWon = "tutorialWon" # The cloud function which handles if the tutorial is won
injectedTutorialWon = False # Determines if the rewards of the tutorial will be injected (visual)
injectedTutorialWonBO = 999999 # Determines the BO (bomberium, coins) won by the injected tutorial (visual)
injectedTutorialWonMedals = 999999 # Medals won by injected tutorial (visual)
```

This code will be explained shortly.

4. **apiUrl** and **apiCloudScriptURL** are variables which hold the API endpoint (you don't need to worry about them). You will need to change the variables below it:

bomberium = *put a integer here* (bomberium = 1000000)
freespins = *put a integer here* (freespins = 1000000)
vipspins = *put a integer here* (vipspins = 1000000)
seasonPass = *put a boolean here (like True/False)* (seasonPass = True)
XP = *put a integer here* (XP = 100000)
gems = *put a integer here* (gems = 1000000)
medals = *put a integer here* (medals = 1000000)
alwaysBots = *put a boolean here (like True/False)* (alwaysBots = True)
costumes = *put a boolean here (like True/False*) (costumes = False)
recommendedVersion = *put a boolean here (like True/False)* (recommendedVersion = True)

fashionPoints = *put a integer here (between 1-100)* (fashionPoints = 100)
ad = *put a boolean here (like True/False)* (ad = True)

**These last variables are only for new players and they're visual. There's no good reason for most players to change these values and only new players can be affected by these last exploits! They are also (mostly) undocumented in value ranges**

injectedTutorialWon = *put a boolean here (like True/False)* (injectedTutorialWon = False)
injectedTutorialWonBO = *put a integer here* (injectedTutorialWonBO = 999999)
injectedTutorialWonMedals = *put a integer here* (injectedTutorialWonMedals = 999999)

**KEEP IN MIND**: These values are simply examples of what to change. They guide you through the whole process with the expected values and they show example values. Not every value has been fully tested (with the range of it). Rule of thumb is not to put floats into integers. **DON'T BE DUMB, DO AS TOLD AND AS EXPECTED!**

5. Once changed, save the changes. That's it. All you needed to change was a couple of variables. Now, the script can correctly and precisely check and actually **modify** (since falsy values do not actually modify it)

6. Run **mitmproxy** or **mitmweb** now with the way it was ran previously.

All you need to know for the installation is that you simply need to have **Python** installed and **mitmproxy**, which most systems have for installation.

## Usage

You can now use it on your iOS or Android device! The proxy needs to be turned on (along with the machine) when using it. 

1. Open your device settings
2. Go to your proxy settings (most likely found in Internet or Wi-Fi section). You will use this proxy to sniff and modify game traffic as it does. Keep in mind both devices need to be in the same network, be able to communicate to each other (not blocked!) and not cause IP range problems or such problems. This part will be very important!
3. Change your proxy IP and port in the settings to this:

Proxy IP: 192.168.100.42 -> Example IP range for some private networks

Proxy Port: 8080 -> This is the default mitmproxy port, mitmweb uses :8081 for the web UI. If you have changed the port number, set it to that port number.

4. Check if you have internet connection. You may notice weird issues with your web browser telling you that you cannot connect with it since your connection is insecure. However, that's an **mitmproxy** issue (it's not an issue, it's SSL pinning or certificate distrust) and do not open up issues/contributions etc. about any **mitmproxy**-specific problem that cannot be fixed!
5. If you do, reload the game if it was opened before. Open the game if it was not opened before. Give it some time to load and it will open up!
