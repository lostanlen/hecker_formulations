import os
import sys

n_files = 72

# Loop over recording units.
for file_id in range(1, 1+n_files):

    # Define file path.
    job_name = "hecker_formulations_" + str(file_id).zfill(2)
    file_name = job_name + ".sbatch"
    file_path = os.path.join("sbatch", file_name)


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
        f.write("module load/matlab2017a\n")
        f.write("\n")
        f.write("# The argument is the ID of the file.\n")
        f.write("matlab -nosplash -nodesktop -nodisplay -r " +
            "\"file_id = '" + str(file_id).zfill(2) + "'; " +
            "run('../hecker_formulations');\"")
