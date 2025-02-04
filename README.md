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
	 sudo apt update

## 3. Configure GitHub SSH Access

To interact with GitHub securely via SSH, follow these steps:

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
	git clone git@github.com:your-username/your-repo.git cd your-repo
From this point, all setup instructions will be run directly from within this repository.

## 6. Run the Initialization Script

To install required dependencies, execute the provided `init.sh` script:
	./init.sh

This script will:
- Update system packages.
- Install essential tools (`make`, `python3.12-venv`, `tree`).
# Installing Headless Chrome Browser 
## 7. Verify Setup

After running the setup, verify everything is working:
	git --version python3 --version tree --version
If any command fails, re-run the corresponding setup step.

---

### Notes:
- The `init.sh` script includes `sudo apt update`, so running it again after step 2 is redundant but ensures the system is fully updated.
- If any step fails, ensure you have proper permissions (use `sudo` when necessary).


# Installing Headless Chrome Browser

