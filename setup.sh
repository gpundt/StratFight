#!/usr/bin/bash
#####
# Griffin Pundt
# Setup script to install necessary packages for StratFight
#####

### Global Variables ###
APT_PACKAGES=("python3-venv" "python3-pip")

### Colors ###
RESET="\e[0m"
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"

graceful_exit() {
	echo -e "${RED}*Closing*${RESET}"
	exit 1
}

successful() {
	echo -e "\t - ${GREEN}*Successful*${RESET}\n"
}

install_apt_packages() {
    echo -e "${YELLOW}[*] Installing apt Packages [*]${RESET}"
	for package in "${APT_PACKAGES[@]}"; do
		echo -e "\t - ${YELLOW}*Installing ${package}*${RESET}"
		if ! sudo apt install "${package}" -y; then
			echo -e "${RED}[!] Error Installing ${package} [!]${RESET}"
			graceful_exit
		fi
	successful
	done
}

main() {
    install_apt_packages
    echo -e "${GREEN}*Finished*${RESET}\n"
}

main