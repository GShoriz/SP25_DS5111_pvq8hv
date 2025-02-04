Data Science Class Project Repository

## Author Information

- **Author**: George Shoriz
- **Role**: Data Scientist
- **University**: University of Virginia Data Science
- **Course**: 25SP_DS5111

## Project Overview

This repository is part of a class project for the 25SP_DS5111 course at the University of Virginia Data Science program. The goal of this project is to build an end-to-end micro pipeline for data storage and processing, with an emphasis on both the tools and methodology used. 

We plan to research and execute a variety of tools and strategies, including: 

- **Version Control and Collaboration**: We use GitHub for source control and GitHub Actions for continuous integration and deployment. 
- **Data Transformation and Storage**: Using DBT (Data Build Tool) and Snowflake to manage, convert, and store data efficiently.
- **Command Line Operations**: Improving command-line skills for data manipulation and automated scripting. 
- **Software Development Best Practices**: Using testing frameworks and design principles to enable reliable software development. 
- **Integration with Data Science Workflows**: Combining classic command-line methodologies with new data science tools such as Jupyter Notebooks. 

The purpose of this project is not only to create a working data pipeline, but also to pause and get a thorough understanding of the many tools, methodologies, and procedures involved. This repository will help participants develop a fully functional cloud-based pipeline capable of harvesting data, processing it, and presenting actionable insights to a 'client'. This will provide a practical framework for understanding and implementing data science projects in a real-world environment.



# VM Setup and Bootstrap Sequence

## 1. Prerequisites

Before setting up the virtual machine (VM), ensure you have:
- A fresh Ubuntu VM instance.
- An active GitHub account.
- SSH access to your VM.

## 2. Initial Setup

The first step in setting up the VM is to update the package lists to ensure the latest versions of required packages are installed.
By running the following command:
-	**sudo apt update**
-	**sudo apt install make -y**
-	**sudo apt install python3.12-venv -y**
-	**sudo apt install tree**

- This can also be automatically  ran by calling on **init.sh** file located in the **scripts** folder which will be mentioned in step 6. 

## 3. Configure GitHub SSH Access

- To interact with GitHub securely via SSH, follow these steps on your VM:

1. Generate an SSH key:
	
	```bash
	ssh-keygen -t ed25519 -C "your-email@example.com"
	```

	- Press **Enter** to accept the default file name.
	- Press **Enter** again to skip the passphrase prompt.

2. Copy the SSH public key to GitHub:

	```bash
	cat ~/.ssh/id_ed25519.pub
	```

	- Copy the output.
	- Go to **GitHub** → **Settings** → **SSH and GPG Keys**.
	- Click **New SSH Key**, name it based on your VM (e.g., `VM-Setup`), and paste the key.

3. Test the SSH connection:
	
	```bash
	ssh -T -i ~/.ssh/id_ed25519 git@github.com
	```

- If successful, you should see a message confirming your GitHub username.

## 4. Set Up Git Credentials

- To configure Git with your user details in the Ubuntu console type the following (see **'setup_git_global_creds.sh'** for more details):

	- USER="your-email@example.com"
	- NAME="Your Name"
	
	- git config --global --list
	
	- git config --global user.email ${USER}
	- git config --global user.name ${NAME}

	- git config --global --list

- This ensures that commits are correctly attributed to you. Alternativly, you can create and update the **'setup_git_global_creds.sh'** with your USER and NAME and call it by going to the place of the file and running:

	```bash
	./setup_git_global_creds.sh
	```

## 5. Clone the Repository

- Now, you can clone this repository to your VM:

	```bash
	git clone git@github.com:GShoriz/SP25_DS5111_pvq8hv.git
	```

- **From this point, all setup instructions will be run directly from within this repository.**

## 6. Run the Initialization Script

- To install required dependencies, execute the provided `init.sh` script:

	```bash
	./init.sh
	```

This script will:
- Update system packages.
- Install essential tools (`make`, `python3.12-venv`, `tree`).
 
## 7. Verify Setup

- After running the setup, verify everything is working:
	- git --version
	- python3 --version 
	- tree --version

- **If any command fails, re-run the corresponding setup step.**

---

### Notes:
- The `init.sh` script includes `sudo apt update`,`sudo apt install make -y`, `sudo apt install python3.12-venv -y`, and `sudo apt install tree` so running it again after step 2 is redundant but ensures the system is fully updated.


# Chrome Headless Browser install

## 1. Setting Up '.gitignore'
- To prevent failed git pushes due to large files over 100mb, that the Chrome browser installer will output. we have to configure a '.gitignore' file. 
this command will create it.

	```bash
	nano .gitignore
	```

- Edit the .gitignore File add the following line:
	- **google-chrome-stable_current_amd64.deb**

### Note: 
- **At this point push all changes to your repository, before moving on to the next steps**

## 2. Installing Required Tools and Scripts
- Copy the `requirements.txt.`, `install_chrome_headless.sh`, and `makefile` from the **scripts** folder inside this repository.

- The `requirements.txt` includes necessary Python packages: 
	- pandas
	- lxml

## 3. Running Chrome Headless Script
- Run the `install_chrome_headless.sh` script to install Google Chrome in a headless configuration for web scraping tasks. First, navigate to where you've placed the file then run:

	```bash
	./install_chrome_headless.sh #if this doesn't work immediatley  run the follwoing command:
	chmod +x install_chrome_headless.sh 
	```
After installation, test it by running a quick dump of https://example.com (this is already incldued in the script)

## 4. Configure Environment with Makefile
- The `makefile` automates the environment setup and running tasks. Here's how to use it:

	```make
	#  Set up Python virtual environment and install dependencies
	make update

	#  Test installation by running a job to fetch stock gainers
	make ygainers.csv
	```
## 5. Validate Installation
- Confirm that all parts of the environment are correctly set up by checking the directory structure:

	```bash
	tree <your-project-repo> -I env
	```
### Explanation

- **Pre-requisites**: Introduces the initial requirements and `.gitignore` setup to handle large files properly.
- **Adding Scripts**: Describes how to add the makefile and requirements file to the project and what they do.
- **Installing Chrome Headless Browser**: Guides through the installation of Chrome for headless operations necessary for scraping tasks.
- **Validation**: Ensures the environment is running as indented. 
