#!/bin/bash

# Prompt if no IP is given
if [ -z "$1" ]; then
  read -p "Enter target IP address: " TARGET
else
  TARGET=$1
fi

TERMINAL="gnome-terminal" # Change if needed


# Nmap
$TERMINAL -- bash -c "echo '[*] Starting port and service discovery...'; nmap -sC -sV -Pn -T4 $TARGET; exec bash" &

# Gobuster
$TERMINAL -- bash -c "echo '[*] Discovering hidden webpages...'; gobuster dir -u http://$TARGET -w /usr/share/wordlists/dirb/common.txt -t 40; exec bash" & #change path if needed for commmon.txt

# Nikto
$TERMINAL -- bash -c "echo '[*] Checking for known vulnerabiltiies...'; nikto -h http://$TARGET; exec bash" &

# WhatWeb
$TERMINAL -- bash -c "echo '[*] Identifying web technologies...'; whatweb http://$TARGET; exec bash" &

echo "Live recon launched on $TARGET, standby.."


