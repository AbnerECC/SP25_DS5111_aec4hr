# SP25_DS5111_aec4hr

This repository is for applying automation techniques for data science. 

## **Relevant Scripting Setup**


- When setting up a new virtual machine user should run "sudo apt update" manually

- Additionally, create git creds and create an ssh key with scripts you've used instructions from this link 
- https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- Clone this repo to run future actions using scripts saved here
- Run the init.sh script located in this repo to begin

## **Project Setup**

- Within the project run the install_chrome_headless.sh script to install a chrome headles browser and check that the example works
- The requirements.txt file includes the pandas libraries that are needed to run the code. These requirements will be executed within the makefile
- Within the project use the "Make" command to run the Makefile
- The make update command includes everything thast should be needed to run the project
- An example of what the repo should look like after running this project setup is pasted below
- SP25_DS5111_aec4hr
├── LICENSE
├── Makefile
├── README.md
├── bin
│   ├── __pycache__
│   └── normalize_csv.py
├── env
│   ├── bin
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   └── pyvenv.cfg
├── google-chrome-stable_current_amd64.deb
├── init.sh

## Automation

- A linter and pytest script have been added to assist with testing for potential issues.
- Using the make lint command in the home directory will call the linter to check the performance of the script normalize_csv script
- Using the make test command in the home directory will call both the linter and a pytest that checks for various possible issues with the normalize_csv script


## Status

[![Feature Validation](https://github.com/AbnerECC/SP25_DS5111_aec4hr/actions/workflows/validations.yml/badge.svg?branch=LAB-03_csv_normalizer)](https://github.com/AbnerECC/SP25_DS5111_aec4hr/actions/workflows/validations.yml)
