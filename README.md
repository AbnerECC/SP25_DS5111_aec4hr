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
- Within the project use the "Make" command to view the Makefile
- The make update command includes everything thast should be needed to update the environment
- Use the "make ygainers.csv" command to parse the html file into a csv
- An example of what the repo should look like after running this project setup is pasted below
- SP25_DS5111_aec4hr
├── LICENSE
├── Makefile
├── README.md
├── google-chrome-stable_current_amd64.deb
├── init.sh
├── install_chrome_headless.sh
├── requirements.txt
├── wjsgainers.html
└── ygainers.html

1 directory, 9 files
