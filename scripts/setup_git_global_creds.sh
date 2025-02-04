#! /usr/bin/bash

USER="your-email@example.com"

NAME="Your Name"

git config --global --list

git config --global user.email ${USER}

git config --global user.name ${NAME}

git config --global --list
