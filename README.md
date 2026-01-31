# High-throughput-G-estimation-and-compositional-enumeration-of-POSS-structures
This repository contains Python scripts for the combinatorial generation of polyhedral oligomeric silsesquioxane (POSS) structures, estimation of their solvation free-energy descriptors (ΔG), and aggregation of results into machine-learning-ready datasets. The workflow enumerates POSS cage–substituent compositions, computes additive energetic descriptors based on pre-tabulated Es and Nes values, and organizes the results for downstream analysis, screening, or data-driven modeling.


## Workflow overview
1. readsolventdata.py

Reads descriptor data from an Excel file (one sheet per solvent)
Enumerates all valid POSS compositions for T8, T10, and T12 cages
Computes ΔG = ΣEs + ΣNes for each structure
Outputs solvent-specific CSV files (*_result.csv)

2. unify.py

Reads all *_result.csv files
Converts component lists into explicit component counts
Produces a unified dataset (component_quantities*.csv)

3. findPOSS.py

Interactive script
Allows users to select cage size and substituent quantities
Queries the aggregated dataset to retrieve ΔG and descriptor values


