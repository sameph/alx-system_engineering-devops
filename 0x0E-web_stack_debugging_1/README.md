Debugging Nginx Port 80 Issue

Introduction
This repository contains a task related to debugging and fixing an issue with Nginx not listening on port 80 in an Ubuntu container. The goal is to utilize debugging skills to identify and resolve the problem, and subsequently, create a Bash script to automate the fix.

Task Description
1. Identify the Issue
Using debugging skills, investigate and determine the root cause of Nginx not listening on port 80 within the Ubuntu container.

2. Install Necessary Tools
If required, install any tools necessary for debugging. You have the flexibility to start and destroy containers as needed during the debugging process.

3. Write a Bash Script
Create a Bash script that automates the process of configuring the server to ensure Nginx is running and listening on port 80 for all active IPv4 IPs.

Requirements
Nginx must be running.
Nginx should be configured to listen on port 80 for all active IPv4 IPs.
The Bash script should be concise and execute the minimum number of commands necessary to achieve the desired configuration.
Getting Started
Follow the steps below to complete the task:

Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/your-username/nginx-port-80-debug.git
Navigate to the project directory.

bash
Copy code
cd nginx-port-80-debug
Start debugging the Nginx port 80 issue in the Ubuntu container.

Implement the fix manually.

Once the manual fix is successful, create a Bash script (fix_nginx_port.sh) with the necessary commands to automate the process.

Test the Bash script to ensure it successfully configures Nginx to listen on port 80.

Commit and push your changes to the repository.

Conclusion
This repository serves as a practical exercise to enhance debugging skills and automation with Bash scripting. The goal is to contribute a solution that ensures Nginx is correctly configured to listen on port 80 for all active IPv4 IPs.