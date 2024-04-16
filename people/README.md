# Tutorial for running Generation Interval V2 on remote cluster via ssh tunelling

During the development of Generation Interval V2, the app will be runnable in a HPC cluster and accessible through ssh tunnelling. This document will serve as a tutorial to run Generation Interval V2 this way, please read the whole tutorial before first usage to ensure the correct functioning, I'll try to be brief:

## 1. Copy the directory new_user

Use the following command (bash HPC terminal):

<code>cp -r /faststorage/project/genint2_develop/GenerationInterval_V2/people/new_user /faststorage/project/genint2_develop/GenerationInterval_V2/people/**OWN_USERNAME**</code>

The directory contains:

- logs: Directory to store output and error while running the server.
- results: Directory to store results while using Generation Interval V2.
- job_USERNAME.sh: Bash script that runs the application on the HPC cluster.
- tunnel_genint2.sh: Bash script that should be run from the user's local machine.

## 2. Install conda environment

Use the following command (bash HPC terminal):

<code>conda env create -f /faststorage/project/genint2_develop/GenerationInterval_V2/ssh_genint2.yaml</code>

This will install the neccessary packages through conda.

## 3. Modify job_new_user.sh

Modify the file "job_new_user.sh" inside the newly copied folder:

1- Change the name to job_USERNAME.sh
2- Inside the file, change all the wildcards "**USERNAME" into the username you have chosen for the directory.
3- Save and close the file

## 4. Modify and download tunnel_genint2.sh

1- Download the file "tunnel_genint2.sh" to your local machine.
2- Inside the file, change all the wildcards "**USERNAME" into the username you have chosen for the directory.
3- Define the port you want to use (default is 2208, change it to a different number).
4- (Optional) delete tunnel_genint2.sh from the cluster.

## 5. Good to go!

Run the app from your favourite shell with:

<code>bash tunnel_genint2.sh</code>

Then open a browser at 127.0.0.1:SELECTED_PORT and it should be up and running!