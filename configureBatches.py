# Instructions
# 1. - Download this file and put it inside your FSM folder.
# 2. - Create accounts.txt and input your accounts as username:password new line username2:password
# 3. - Run the script

import os
from termcolor import colored


def log(message):
    print(colored("[logs]", "yellow"), message)


CleanConfig = """
@echo off
title FSM Boost Tool
echo FSM Boost Tool Loading...

Start ""  "C:\Program Files (x86)\Steam\steam1.exe" "%steamdir%" -silent -login YOURLOGIN YOURPASSWORD -applaunch 730 -windowed -h 480 -w 640 -x 0 -y 0 -novid -nojoy -swapcores -d3d9ex -dxlevel 90 +snd_use_hrtf 0 -low -volume 0 +mat_queue_mode 0 -language english -noaafonts -nosound +sethdmodels 0 +violence_hblood 0 -lv +mat_disable_fancy_blending 1 -softparticlesdefaultoff -nohltv -limitvsconst +r_dynamic 0 -noaafonts -nohltv -nopreload -softparticlesdefaultoff -vrdisable -low +exec bots

"""



BATCHLOC = './Files/Bot Accounts'
log("Started Cleaning batch files...")
for filename in os.listdir(BATCHLOC):
    filepath = os.path.join(BATCHLOC, filename)
    if os.path.isfile(filepath):
        with open(filepath, 'w') as f:
            log("Cleaning: " + filename)
            f.write(CleanConfig)
log("Finsihed Cleaning batch Files")


if os.path.isfile("accounts.txt"):
    log("Found accounts.txt")
    with open("accounts.txt", "r") as f:
        userpass = f.read().strip().split("\n")

    # Loop over each batch file in the directory
    for filename in os.listdir("./Files/Bot Accounts"):
        if filename.endswith(".bat"):
            batch_filename = os.path.join("./Files/Bot Accounts", filename)

            index = int(filename[3]) - 1
            username, password = userpass[index].split(":")

            with open(batch_filename, "r") as f:
                contents = f.read()
            new_contents = contents.replace(
                "YOURLOGIN", username).replace("YOURPASSWORD", password)
            with open(batch_filename, "w") as f:
                f.write(new_contents)
                log('Replacing Login information for ' + batch_filename)

else:
    print("Missing accounts.txt - Create and fill out accounts.txt before trying again")
    quit()
