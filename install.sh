#!/bin/bash

# MIT License

# Copyright (C) 2019, Arissploit Team. All Rights Reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

CE="\033[0m"
RS="\033[1;31m"
YS="\033[1;33m"
NV="\033[1;37m"

WHO="$( whoami )"

if [[ "$WHO" != "root" ]]
then
sleep 1
echo -e "$RS"run it as"$CE" "$YS"root"$CE"
sleep 1
echo -e "$RS"or use"$CE" "$YS"sudo"$CE"
sleep 1
exit
fi

cd ~ 
if [[ -d arissploit ]]
then
clear
cd arissploit
else
{
git clone https://github.com/entynetproject/arissploit.git
} &> /dev/null
cd arissploit 
chmod +x install.sh
fi

printf '\033]2;arissploit INSTALLER\a'
clear
cat ~/arissploit/banner/banner.txt
echo -e "\033[1;33mBy Arissploit Team\033[0m"
sleep 3
echo -e "More on our site:"
sleep 3
echo -e "==> \033[1;33mhttp://entynetproject.simplesite.com/\033[0m"
sleep 3
echo -e "Creators of Arissploit Framework (\033[4;33marissploit team\033[0m):"
sleep 3
echo -e "\033[4;34mEntynetproject\033[0m - Main Developer"
sleep 3
echo -e "Press \033[1;33many key\033[0m to install arissploit"
read -n 1

clear
{
cp bin/arissploit /bin
chmod +x /bin/arissploit
cp bin/arissploit /usr/local/bin
chmod +x /usr/local/bin/arissploit
} &> /dev/null

sleep 1
echo -e "Select your architecture ("$YS"amd"$CE"/"$YS"intel"$CE"/"$YS"arm"$CE")."
echo -e "Arissploit supports "$YS"amd"$CE", "$YS"intel"$CE" and "$YS"arm"$CE" architectures."
echo -e "Select your architecture to install compatible dependencies."
read -p $'(\033[4;93march\033[0m)> ' CONF

if [[ "$CONF" = "amd" ]]
then
sleep 1
clear
cd install
sleep 1
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
pip install -r requirements.txt
else
apt-get update
apt-get install python
apt-get install git
apt-get install wget
apt-get install python2-pip
apt-get install perl
apt-get install Build essential
apt-get install libany-uri-escape-perl
apt-get install libhtml-html5-entities-perl
apt-get install libhtml-entities-numbered-perl
apt-get install libhtml-parser-perl
apt-get install libwww-perl
apt-get install php
apt-get install libdnet
apt-get install ethtool
apt-get install aircrack-ng
apt-get install ettercap-text-only
apt-get install dsniff
apt-get install xterm
apt-get install driftnet
apt-get install tcpdump
apt-get install libnetfilter-queue-dev
apt-get install python3.5-dev
apt-get install hcitool
apt-get install sslstrip
sleep 0.5
pip install -r requirements.txt
fi
fi

if [[ "$CONF" = "arm" ]]
then
sleep 1
clear
cd install
sleep 1
if [[ -d /System/Library/CoreServices/SpringBoard.app ]]
then
pip install -r requirements.txt
else
pkg update
pkg install git
pkg install wget
pkg install python
pkg install python2
pkg install perl
pkg install php
pkg install libdnet
pkg install ethtool
pkg install aircrack-ng
pkg install ettercap-text-only
pkg install dsniff
pkg install xterm
pkg install driftnet
pkg install tcpdump
pkg install libnetfilter-queue-dev
pkg install python3.5-dev
pkg install hcitool
pkg install sslstrip
sleep 0.5
pip install -r requirements.txt
fi
fi

if [[ "$CONF" = "intel" ]]
then
sleep 1
clear
cd install
sleep 1
if [[ -d /System/Library/CoreServices/Finder.app ]]
then
pip install -r requirements.txt
else
apt-get update
apt-get install python
apt-get install git
apt-get install wget
apt-get install python2-pip
apt-get install perl
apt-get install Build essential
apt-get install libany-uri-escape-perl
apt-get install libhtml-html5-entities-perl
apt-get install libhtml-entities-numbered-perl
apt-get install libhtml-parser-perl
apt-get install libwww-perl
apt-get install php
apt-get install libdnet
apt-get install ethtool
apt-get install aircrack-ng
apt-get install ettercap-text-only
apt-get install dsniff
apt-get install xterm
apt-get install driftnet
apt-get install tcpdump
apt-get install libnetfilter-queue-dev
apt-get install python3.5-dev
apt-get install hcitool
apt-get install sslstrip
sleep 0.5
pip install -r requirements.txt
fi
fi

clear

printf '\033]2;Arissploit INSTALLER\a'
sleep 3
echo -e "Open a NEW terminal and type '"$YS"arissploit"$CE"' to launch the framework"
sleep 2
