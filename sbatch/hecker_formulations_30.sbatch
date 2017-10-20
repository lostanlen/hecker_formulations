#!/bin/bash

#BATCH --job-name=hecker_formulations_30
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=0:10:00
#SBATCH --mem=32GB
#SBATCH --output=../slurm/slurm_hecker_formulations_30_%j.out

module purge
module load/matlab2017a

# The argument is the ID of the file.
matlab -nosplash -nodesktop -nodisplay -r "file_id = 30; run('../hecker_formulations.m');"