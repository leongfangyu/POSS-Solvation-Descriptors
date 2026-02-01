
<div align="center">   
  
# Interaction mechanisms of POSS-based adsorbents with VOCs, CO<sub>2</sub>, CH<sub>4</sub>, and H<sub>2</sub>O: Theoretical insights and prediction method
</div>

 
## [Paper](https://doi.org/10.1016/j.gce.2024.10.009)
## Abstract
The dual nature of Polyhedral Oligomeric Silsesquioxane (POSS), with its cage framework and substituent groups, enables diverse interactions with liquid and gaseous pollutants. While Quantum Mechanical (QM) methods have been used for simpler POSS variants, evaluating all possible combinations of cages and substituents remains impractical. This study aims to fill the knowledge gap on how the polarity of liquid pollutants and the structural features of POSS influence the efficiency of separating Volatile Organic Compounds (VOCs) from aqueous streams in wastewater treatment processes. Using a comprehensive dataset on liquid-liquid adsorption selectivities, we developed a predictive model for estimating VOC-VOC and VOC-water partition coefficients across 1.424 × 10<sup>7</sup> POSS variants, achieving accuracy comparable to expensive QM methods. This model enables users to design novel POSS molecules tailored for wastewater treatment or VOC recovery quickly and efficiently. We explored adsorption mechanisms for CO<sub>2</sub>, H<sub>2</sub>O, and CH<sub>4</sub>, focusing on interactions between the cage and adsorbates, as well as between substituents and adsorbates. Our findings highlight that substituents are crucial for gas adsorption, with their electrostatic properties being a significant factor. While all substituents exhibited strong CO<sub>2</sub>/CH<sub>4</sub> selectivity, this selectivity diminishes in the presence of H<sub>2</sub>O. Additionally, gaseous pollutants are only effectively encapsulated when the POSS cage size exceeds T<sub>10</sub>. This work provides a framework for designing optimized POSS materials for specific separation applications, facilitating the efficient selection of structures for targeted gas and liquid capture.

![abstract](https://github.com/user-attachments/assets/f42bca64-f5e6-4072-b55a-856d3aea8b8a)



## Description
This repository contains Python scripts for the combinatorial generation of polyhedral oligomeric silsesquioxane (POSS) structures, estimation of their solvation free-energy descriptors (ΔG), and aggregation of results into machine-learning-ready datasets. The workflow enumerates POSS cage–substituent compositions, computes additive energetic descriptors based on pre-tabulated Es and Nes values, and organizes the results for downstream analysis, screening, or data-driven modeling.


## Workflow overview

1. **`aggregate.py` — Data aggregation and electrostatic scaling**
   - Reads solvent-specific result files (`*_result.csv`)
   - Converts POSS component lists into explicit cage and substituent counts
   - Optionally applies a user-defined scaling factor to electrostatic energy terms (SumEsValues)
   - Produces a unified tabular dataset (`component_quantities<scale>.csv`)
   - Output is suitable for regression, screening, and data-driven modeling

2. **`extract.py` — Interactive ΔG lookup and partition-coefficient calculation**
   - Queries the aggregated dataset for user-defined POSS compositions
   - Returns ΔG values with an empirical correction factor
   - Optionally computes solvent–solvent partition coefficients (log P)
   - Designed for exploratory and interpretive thermodynamic analysis


### Electrostatic energy scaling (recommended)

During data aggregation, an optional empirical scaling factor can be applied to the electrostatic energy contribution (SumEsValues). Based on experimental validation reported in our [paper](https://doi.org/10.1016/j.gce.2024.10.009), a scaling factor of **0.75** for SumEsValues was found to provide improved agreement between predicted and experimental partition coefficients. Unless otherwise stated, users are recommended to adopt a scaling factor of **0.75** when generating aggregated datasets for quantitative analysis.

### Input data availability (required)

The usage of **`aggregate.py`** requires a complete set of solvent-specific result files in the form of:
These files are **not stored directly in this repository** due to their size.  
All required `_result.csv` files can be downloaded from the following Google Drive folder:

👉 **Download link:**  
https://drive.google.com/drive/folders/1wvTEkxSdcAfQ0RCoQuKzsjw7KjPtImRR

Before running `aggregate.py`, users must:

1. Download all `_result.csv` files from the Google Drive link above  
2. Place all downloaded files in the **same directory as `aggregate.py`**

The aggregation script automatically scans the current directory and processes all files matching the pattern `_result.csv`.

## Requirements
- Python 3.8 or later
* pandas
+ openpyxl

## Installation
> pip install pandas openpyxl

## Usage

### Step 0: Download required input data
Download all solvent-specific `_result.csv` files from the Google Drive link provided above and place them in the same directory as `aggregate.py`.

### Step 1: Aggregate POSS component quantities
> python aggregate.py

### Step 2: Query the dataset interactively
> python extract.py


> [!NOTE]
> - ΔG values are computed using an additive descriptor model (ΣEs + ΣNes).
> - An empirical scaling factor (recommended value: **0.75**) can be applied to electrostatic energy contributions based on experimental validation reported in the associated publication.
> - This code does not perform molecular dynamics or quantum chemistry calculations.
> - Solvent-specific `_result.csv` files must be downloaded separately before running `aggregate.py`.

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

