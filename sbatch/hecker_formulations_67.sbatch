#!/bin/bash

#BATCH --job-name=hecker_formulations_67
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --mem=32GB
#SBATCH --output=../slurm/slurm_hecker_formulations_67_%j.out

module purge
module load matlab/2017a

# The argument is the ID of the file.
matlab -nosplash -nodesktop -nodisplay -r "file_id = 67; run('../hecker_formulations.m');"