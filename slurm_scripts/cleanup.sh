#!/bin/bash

### TC1 Job Script ###
 
#SBATCH --partition=UGGPU-TC1
#SBATCH --qos=normal
#SBATCH --gres=gpu:1

### Specify Memory allocate to this job ###
#SBATCH --mem=10G

### Optional: Default CPU assign = 1; Specify if want to apply more for computation###
### Remove 1st # at next line for the option to take effect ###
##SBATCH --ntasks-per-node=2

### Specify number of node to compute ###
#SBATCH --nodes=1

### Optional: Specify node to execute the job ###
### Remove 1st # at next line for the option to take effect ###
##SBATCH --nodelist=TC1N07

### Specify Time Limit, format: <min> or <min>:<sec> or <hr>:<min>:<sec> or <days>-<hr>:<min>:<sec> or <days>-<hr> ### 
#SBATCH --time=360

### Specify name for the job, filename format for output and error ###
#SBATCH --job-name=CleanupJob
#SBATCH --output=output_cleanup.out
#SBATCH --error=error_cleanup.err

### Must load the required CUDA module if want to use available CUDA in TC1 for computation ###
module load cuda/12.9

### Script for computation ###
module load anaconda
source activate SocialJax
python cleanup.py