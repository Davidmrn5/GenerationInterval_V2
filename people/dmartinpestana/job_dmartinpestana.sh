#!/bin/sh
#BATCH --mem-per-cpu 6g
#SBATCH -t 02:00:00
#SBATCH -o /faststorage/project/genint2_develop/GenerationInterval_V2/people/dmartinpestana/logs/dmartinpestana.out
#SBATCH -e /faststorage/project/genint2_develop/GenerationInterval_V2/people/dmartinpestana/logs/dmartinpestana.err
#SBATCH -J genint2_dmartinpestana
#SBATCH -A genint2_develop

source ~/.bashrc
conda activate /home/dmartinpestana/miniforge3/envs/genint2_ssh/
cd /faststorage/project/genint2_develop/GenerationInterval_V2/
uvicorn --app-dir /faststorage/project/genint2_develop/GenerationInterval_V2/src main:app --reload
