#!/bin/sh
#BATCH --mem-per-cpu 6g
#SBATCH -t 02:00:00
#SBATCH -o /faststorage/project/genint2_develop/GenerationInterval_V2/people/**USERNAME/logs/**USERNAME.out
#SBATCH -e /faststorage/project/genint2_develop/GenerationInterval_V2/people/**USERNAME/logs/**USERNAME.err
#SBATCH -J genint2_**USERNAME
#SBATCH -A genint2_develop

source ~/.bashrc
conda activate /faststorage/project/genint2_develop/GenerationInterval_V2/requirements/ssh_genint2/
uvicorn --app-dir /faststorage/project/genint2_develop/GenerationInterval_V2/src main:app