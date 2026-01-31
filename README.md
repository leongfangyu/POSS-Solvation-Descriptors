# High-throughput-G-estimation-and-compositional-enumeration-of-POSS-structures
This repository contains Python scripts for the combinatorial generation of polyhedral oligomeric silsesquioxane (POSS) structures, estimation of their solvation free-energy descriptors (ΔG), and aggregation of results into machine-learning-ready datasets. The workflow enumerates POSS cage–substituent compositions, computes additive energetic descriptors based on pre-tabulated Es and Nes values, and organizes the results for downstream analysis, screening, or data-driven modeling.


## Workflow overview

1. **`main2.py` — Data aggregation and feature construction**
   - Reads solvent-specific result files (`*_result.csv`)
   - Converts POSS component lists into explicit cage and substituent counts
   - Produces a unified tabular dataset (`component_quantities*.csv`)
   - Output is suitable for regression, screening, and data-driven modeling

2. **`extract.py` — Interactive ΔG lookup and log P calculation**
   - Queries the aggregated dataset for user-defined POSS compositions
   - Returns ΔG values with an empirical correction factor
   - Optionally computes solvent–solvent partition coefficients (log P)
   - Designed for exploratory and interpretive analysis



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

