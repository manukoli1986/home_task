# Scenario1

## Introduction 

Python code which will print the number from 1 to 10 in random order

<!--- BEGIN_TF_DOCS --->

## Requirements

| Name | Version |
|------|---------|
| python | 3.8 |

## Prerequisite

Install python on your <b>Linux</b> or </b>Mac</b> machines (workstation) by folllowing below instructions.

### Install Python 3 on Linux

```
-> Implementation

$ sudo apt update  				                            #Update and Refresh Repository Lists
$ sudo apt install software-properties-common	            #Install Supporting Software
$ sudo add-apt-repository ppa:deadsnakes/ppa	            #Add Deadsnakes PPA
$ sudo apt install python3.8 		        	            #Install Python 3
$ python --version				                            #Check installed python version

```
### Installing Python 3 on Mac OS X

Before installing Python, you’ll need to install GCC. GCC can be obtained by downloading Xcode, the smaller Command Line Tools (must have an Apple account) or the even smaller OSX-GCC-Installer package.

```
-> Implementation
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"     # Install Homebrew
$ export PATH="/usr/local/opt/python/libexec/bin:$PATH"                                                 # Set PATH Environment
$ $ brew install python                                                                                 # Install python 3
$ python  --version                                                                                    # To check python version

```

For more information please follow refrence links:
* [Install python on Linux](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
* [Install python on Mac](https://realpython.com/installing-python/#how-to-install-python-on-macos)

## Run the python application in terminal

```
#########   OUTPUT    #########

$ git clone https://github.com/manukoli1986/home_task.git
$ cd scenario1/
$ ls
app.py  README.md
$ python app.py 
[9, 8, 4, 3, 6, 5, 10, 2, 7, 1]
$ python app.py 
[6, 2, 10, 1, 7, 3, 4, 9, 5, 8]
```

# Best practice
- We can modify python code with more informations like Logging  and argument of numbers. 
- We can run this code on container and pass the argument of numbers.
