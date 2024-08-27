# Tools Setup Overview

This page includes an overview of all the steps for the Tools setup and some important things to remember-- specific to Rahul Verma.

## Setup

To start writing code, there is a lot of setup steps involved: called SDLC (Software Development Lifecycle).

This follows 5 steps:
1. Linux Terminal
2. Shell Commands
3. Clcone Project
4. Package Manager
5. SDLC Established

### Shell Commands

Current system for Rahul: Linux

Common Linux commands and their meaning
- ``ls``: Lists all files in the current directory
- ``pwd``: Outputs the current working directory
- ``mkdir``: Command that allows user to create new directories
- ``cd``: Used to change directories
- ``git``: Used for version control
- ``cat``: Displays a current file's content

Version Control Deep Dive
Version control commands interact with git to keep a history of your code.

- ``git clone``: Copy a git repository to your local machine
- ``git pull`` Update your local copy with the latest changes
- ``git commit`` Save changes to files in local repository
- ``git push`` Update cloud repository with current committed local repository

Package Manager Commands

Since my current system is linux, I will use homebrew. If homebrew is not installed, follow the below steps:
- In terminal, type ``/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"``
- Enter password and follow instruction prompts
- Verify installation with ``brew doctor`` or ``brew --version`` to get the brew version

Common Brew commands
- ``brew list``: List installed packages
- ``brew search <package>``: Search for specified packages
- ``brew update``: Update Brew
- ``brew upgrade``: Upgrade installed packages
- ``brew uninstall <package>``: Uninstall a package

Setting up Dev Tools - MacOs
This command is used to setup tools on macos:
```
cd ./scripts
./activate_macos.sh
````


