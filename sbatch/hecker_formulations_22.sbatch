#!/bin/bash

#BATCH --job-name=hecker_formulations_22
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0:10:00
#SBATCH --mem=32GB
#SBATCH --output=../slurm/slurm_hecker_formulations_22_%j.out

module purge
module load matlab/2017a

# The argument is the ID of the file.
matlab -nosplash -nodesktop -nodisplay -r "file_id = 22; run('../hecker_formulations.m');"