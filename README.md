# High-throughput-G-estimation-and-compositional-enumeration-of-POSS-structures
This repository contains Python scripts for the combinatorial generation of polyhedral oligomeric silsesquioxane (POSS) structures, estimation of their solvation free-energy descriptors (ΔG), and aggregation of results into machine-learning-ready datasets. The workflow enumerates POSS cage–substituent compositions, computes additive energetic descriptors based on pre-tabulated Es and Nes values, and organizes the results for downstream analysis, screening, or data-driven modeling.


## Workflow overview

1. `readsolventdata.py`
   - Reads descriptor data from an Excel file (one sheet per solvent)
   - Computes ΔG = ΣEs + ΣNes for each structure
   - Outputs solvent-specific CSV files (*_result.csv)

2. `unify.py`
   - Reads all *_result.csv files
   - Converts component lists into explicit component counts
   - Produces a unified dataset (component_quantities*.csv)

3. `findPOSS.py`
   - Interactive script
   - Allows users to select cage size and substituent quantities
   - Queries the aggregated dataset to retrieve ΔG and descriptor values


## Requirements
- Python 3.8 or later
* pandas
+ openpyxl

## Installation
> pip install pandas openpyxl

## Usage
Step 1: Generate POSS ΔG data
> python readsolventdata.py

Step 2: Aggregate component quantities
> python unify.py

Step 3: Query the dataset interactively
> python findPOSS.py


> [!NOTE]
> ΔG values are computed using an additive descriptor model.
> This code does not perform molecular dynamics or quantum calculations.
> Descriptor values must be supplied by the user.

## Citation
If you use this code in academic work, please cite or acknowledge the authors accordingly.
<https://doi.org/10.1016/j.gce.2024.10.009/>

### BibTex
@article{leong2024interaction,
  title={Interaction mechanisms of POSS-based adsorbents with VOCs, CO2, CH4, and H2O: Theoretical insights and prediction method},
  author={Leong, Fang Yu and Low, Liang Ee and Chew, Irene Mei Leng},
  journal={Green Chemical Engineering},
  year={2024},
  publisher={Elsevier}
}





