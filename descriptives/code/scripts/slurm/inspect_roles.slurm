#!/bin/bash
#SBATCH --job-name=inspect_roles
#SBATCH --output=/scratch/zt1/project/estarr-prj/user/rylan/portfolio/code/output/%x_%j.out
#SBATCH --error=/scratch/zt1/project/estarr-prj/user/rylan/portfolio/code/err/%x_%j.err
#SBATCH --time=00:15:00
#SBATCH --mem=16G
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

/scratch/zt1/project/estarr-prj/user/rylan/envs/text-analysis/bin/python3 \
    /scratch/zt1/project/estarr-prj/user/rylan/portfolio/code/scripts/python/inspect_roles.py
