import os
import sys

n_files = 72

# Loop over recording units.
for file_id in range(1, 1+n_files):

    # Define file path.
    job_name = "hecker_formulations_" + str(file_id).zfill(2)
    file_name = job_name + ".sbatch"
    file_path = os.path.join(sbatch_dir, file_name)


    # Open file.
    with open(file_path, "w") as f:
        f.write("#!/bin/bash\n")
        f.write("\n")
        f.write("#BATCH --job-name=" + job_name + "\n")
        f.write("#SBATCH --nodes=1\n")
        f.write("#SBATCH --tasks-per-node=1\n")
        f.write("#SBATCH --cpus-per-task=1\n")
        f.write("#SBATCH --time=0:10:00\n")
        f.write("#SBATCH --mem=32GB\n")
        f.write("#SBATCH --output=../slurm/slurm_" + job_name + "_%j.out\n")
        f.write("\n")
        f.write("module purge\n")
        f.write("\n")
        f.write("# The argument is the name of the recording unit.\n")
        f.write("python " + script_path_with_args)
