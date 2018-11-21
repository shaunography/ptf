#!/usr/bin/env python
#####################################
# Installation module for MailSniper
#####################################

# AUTHOR OF MODULE NAME
AUTHOR="Shaun Webber (Shaunography)"

# DESCRIPTION OF THE MODULE
DESCRIPTION="This module will install/update MailSniper - MailSniper is a penetration testing tool for searching through email in a Microsoft Exchange environment for specific terms (passwords, insider intel, network architecture information, etc.). It can be used as a non-administrative user to search their own email, or by an Exchange administrator to search the mailboxes of every user in a domain."

# INSTALL TYPE GIT, SVN, FILE DOWNLOAD
# OPTIONS = GIT, SVN, FILE
INSTALL_TYPE="GIT"

# LOCATION OF THE FILE OR GIT/SVN REPOSITORY
REPOSITORY_LOCATION="https://github.com/dafthack/MailSniper"

# WHERE DO YOU WANT TO INSTALL IT
INSTALL_LOCATION="mailsniper"

# DEPENDS FOR DEBIAN INSTALLS
DEBIAN="git"

# DEPENDS FOR FEDORA INSTALLS
FEDORA="git"

# COMMANDS TO RUN AFTER
AFTER_COMMANDS=""

# THIS WILL CREATE AN AUTOMATIC LAUNCHER FOR THE TOOL
LAUNCHER=""