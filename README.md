# High-throughput-G-estimation-and-compositional-enumeration-of-POSS-structures
This repository contains Python scripts for the combinatorial generation of polyhedral oligomeric silsesquioxane (POSS) structures, estimation of their solvation free-energy descriptors (ΔG), and aggregation of results into machine-learning-ready datasets. The workflow enumerates POSS cage–substituent compositions, computes additive energetic descriptors based on pre-tabulated Es and Nes values, and organizes the results for downstream analysis, screening, or data-driven modeling.


## Workflow overview

1. `main1.py` — ΔG generation  
   - Reads descriptor data from an Excel file (one sheet per solvent)  
   - Enumerates POSS cage–substituent compositions  
   - Computes ΔG using an additive model:  
     ΔG = ΣEs + ΣNes  
   - Outputs solvent-specific CSV files (`*_result.csv`)

2. `main2.py` — Data aggregation  
   - Reads all `*_result.csv` files  
   - Converts component lists into explicit component-count features  
   - Produces a unified dataset (`component_quantities*.csv`)

3. `extract.py` — ΔG query and partition analysis  
   - Interactive script  
   - Allows users to select cage size and substituent quantities  
   - Retrieves ΔG values from the aggregated dataset  
   - Optionally computes solvent–solvent partition coefficients (log P)



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
If this work is helpful for your research, please cite [Interaction mechanisms of POSS-based adsorbents with VOCs, CO2, CH4, and H2O: Theoretical insights and prediction method
](https://doi.org/10.1016/j.gce.2024.10.009).



### BibTex
If this work is helpful for your research, please consider citing the following BibTeX entry.

```
@article{leong2024interaction,
  title={Interaction mechanisms of POSS-based adsorbents with VOCs, CO2, CH4, and H2O: Theoretical insights and prediction method},
  author={Leong, Fang Yu and Low, Liang Ee and Chew, Irene Mei Leng},
  journal={Green Chemical Engineering},
  year={2024},
  publisher={Elsevier},
}

