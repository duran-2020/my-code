#!/usr/bin/bash

#ask for commit message
echo "Enter the commit msg: "

#save input to var message
read message

#git commands executed
git add *
git commit -m "$message"
git push origin HEAD
