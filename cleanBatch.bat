@echo off
title FSM Boost Tool
echo FSM Boost Tool Loading...

Start ""  "C:\Program Files (x86)\Steam\steam1.exe" "%steamdir%" -silent -login YOURLOGIN YOURPASSWORD -applaunch 730 -windowed -h 480 -w 640 -x 0 -y 0 -novid -nojoy -swapcores -d3d9ex -dxlevel 90 +snd_use_hrtf 0 -low -volume 0 +mat_queue_mode 0 -language english -noaafonts -nosound +sethdmodels 0 +violence_hblood 0 -lv +mat_disable_fancy_blending 1 -softparticlesdefaultoff -nohltv -limitvsconst +r_dynamic 0 -noaafonts -nohltv -nopreload -softparticlesdefaultoff -vrdisable -low +exec bots
