# Data Science Class Project Repository

## Author Information

- **Author**: George Shoriz
- **Role**: Data Scientist
- **University**: University of Virginia Data Science
- **Course**: 25SP_DS5111

## Project Overview

This repository is part of a class project for the 25SP_DS5111 course. The details of the project are to be determined, but the repository will be used for storing, sharing, and documenting all relevant project files and findings. This project aims to serve as a resource for researchers, developers, students, and anyone interested in data science.

Stay tuned for updates on project specifics and instructions on how to set up and use the various files and scripts contained in this repository.



# VM Setup and Bootstrap Sequence

## 1. Prerequisites

Before setting up the virtual machine (VM), ensure you have:
- A fresh Ubuntu VM instance.
- An active GitHub account.
- SSH access to your VM.

## 2. Initial Setup

The first step in setting up the VM is to update the package lists to ensure the latest versions of required packages are installed.
By running the following command:
	**sudo apt update**
	**sudo apt install make -y**
	**sudo apt install python3.12-venv -y**
	**sudo apt install tree**
This can also be automatically  ran by calling on **init.sh** file located in the **scripts** folder which will be mentioned in step 6. 

## 3. Configure GitHub SSH Access

To interact with GitHub securely via SSH, follow these steps on your VM:

1. Generate an SSH key:
	ssh-keygen -t ed25519 -C "your-email@example.com"

- Press **Enter** to accept the default file name.
- Press **Enter** again to skip the passphrase prompt.

2. Copy the SSH public key to GitHub:
	cat ~/.ssh/id_ed25519.pub
- Copy the output.
- Go to **GitHub** → **Settings** → **SSH and GPG Keys**.
- Click **New SSH Key**, name it based on your VM (e.g., `VM-Setup`), and paste the key.

3. Test the SSH connection:
	ssh -T -i ~/.ssh/id_ed25519 git@github.com
If successful, you should see a message confirming your GitHub username.

## 4. Set Up Git Credentials

To configure Git with your user details:
	USER="your-email@example.com" NAME="Your Name"

	git config --global user.email "${USER}" git config --global user.name "${NAME}"

	git config --global --list
This ensures that commits are correctly attributed to you.

## 5. Clone the Repository

Now, you can clone this repository to your VM:
	git clone git@github.com:GShoriz/SP25_DS5111_pvq8hv.git
From this point, all setup instructions will be run directly from within this repository.

## 6. Run the Initialization Script

To install required dependencies, execute the provided `init.sh` script:
	./init.sh

This script will:
- Update system packages.
- Install essential tools (`make`, `python3.12-venv`, `tree`).
 
## 7. Verify Setup

After running the setup, verify everything is working:
	git --version python3 --version tree --version
If any command fails, re-run the corresponding setup step.

---

### Notes:
- The `init.sh` script includes `sudo apt update`, so running it again after step 2 is redundant but ensures the system is fully updated.
- If any step fails, ensure you have proper permissions (use `sudo` when necessary).

# Chrome Headless Browser install

## 1. Setting Up '.gitignore'
- To prevent failed git pushes due to large files over 100mb, that the Chrome browser installer will output. we have to configure a '.gitignore' file. 
this command will create it.
   ```bash
   nano .gitignore

- Edit the .gitignore File add the following line:
**google-chrome-stable_current_amd64.deb**

### Note: 
- **At this point push all changes to your repository, before moving on to the next steps**

## 2. Adding Scripts to Your Repository
- Copy the 'install_chrome_headless.sh', 'requirements.txt.', and 'makefile' from the **scripts** folder inside this repository.

- Run the install_chrome_headless.sh script to install Google Chrome in a headless configuration for web scraping tasks. first navigate to where you've placed the file then run:
```bash
./install_chrome_headless.sh #if this doesn't work immediatley run the follwoing command chmod +x install_chrome_headless.sh 

After installtion, test it by running a quick dump of https//example.com

- The requirements.txt includes necessary Python packages: 
- 	pandas
-	lxml
**Install them by running:**
```bash
pip install -r requirements.txt

- 

- The Makefile automates the environment setup and running tasks. Here's how to use it:

```make
#  Set up Python virtual environment and install dependencies
make update

#  Test installation by running a job to fetch stock gainers
make ygainers.csv
