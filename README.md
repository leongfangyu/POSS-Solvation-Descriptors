
<div align="center">   
  
# Interaction mechanisms of POSS-based adsorbents with VOCs, CO<sub>2</sub>, CH<sub>4</sub>, and H<sub>2</sub>O: Theoretical insights and prediction method
</div>

 
## [Paper](https://doi.org/10.1016/j.gce.2024.10.009)
## Abstract
The dual nature of Polyhedral Oligomeric Silsesquioxane (POSS), with its cage framework and substituent groups, enables diverse interactions with liquid and gaseous pollutants. While Quantum Mechanical (QM) methods have been used for simpler POSS variants, evaluating all possible combinations of cages and substituents remains impractical. This study aims to fill the knowledge gap on how the polarity of liquid pollutants and the structural features of POSS influence the efficiency of separating Volatile Organic Compounds (VOCs) from aqueous streams in wastewater treatment processes. Using a comprehensive dataset on liquid-liquid adsorption selectivities, we developed a predictive model for estimating VOC-VOC and VOC-water partition coefficients across 1.424 × 10<sup>7</sup> POSS variants, achieving accuracy comparable to expensive QM methods. This model enables users to design novel POSS molecules tailored for wastewater treatment or VOC recovery quickly and efficiently. We explored adsorption mechanisms for CO<sub>2</sub>, H<sub>2</sub>O, and CH<sub>4</sub>, focusing on interactions between the cage and adsorbates, as well as between substituents and adsorbates. Our findings highlight that substituents are crucial for gas adsorption, with their electrostatic properties being a significant factor. While all substituents exhibited strong CO<sub>2</sub>/CH<sub>4</sub> selectivity, this selectivity diminishes in the presence of H<sub>2</sub>O. Additionally, gaseous pollutants are only effectively encapsulated when the POSS cage size exceeds T<sub>10</sub>. This work provides a framework for designing optimized POSS materials for specific separation applications, facilitating the efficient selection of structures for targeted gas and liquid capture.

![abstract](https://github.com/user-attachments/assets/f42bca64-f5e6-4072-b55a-856d3aea8b8a)



## Technical scope

This repository provides a **Python-based workflow for scientific data
processing, dataset construction, and visualization** in the context of
fragment-based solvation free-energy modeling for POSS structures.

The implemented workflows include:

- **High-throughput data aggregation**
  - Parsing and merging large solvent-specific CSV datasets
  - Automated feature construction (ΣEs, ΣNes, and scaled ΔG descriptors)
  - Generation of machine-learning-ready tabular datasets

- **Programmatic dataset generation**
  - Combinatorial enumeration of POSS cage–substituent compositions
  - Deterministic construction of descriptor-based datasets across multiple solvents
  - Structured export for regression, screening, and downstream modeling

- **Scientific data analysis and visualization**
  - Interactive querying of predicted solvation free energies
  - Reproduction of validation figures (e.g., parity plots in Fig. 6)
  - Quantitative comparison between quantum-chemical reference data and model predictions

In addition, the repository includes auxiliary scripts for **post-processing
Gaussian 16 outputs**, enabling direct integration between quantum-chemistry
calculations and Python-based data analysis pipelines.


## Workflow overview

1. **`scripts/aggregate.py` — Data aggregation and electrostatic scaling**
   - Reads solvent-specific result files (`*_result.csv`)
   - Converts POSS component lists into explicit cage and substituent counts
   - Optionally applies a user-defined scaling factor to electrostatic energy terms (SumEsValues)
   - Produces a unified tabular dataset (`component_quantities<scale>.csv`)
   - Output is suitable for regression, screening, and data-driven modeling

2. **`scripts/extract.py` — Interactive ΔG lookup and partition-coefficient calculation**
   - Queries the aggregated dataset for user-defined POSS compositions
   - Returns ΔG values with an empirical correction factor
   - Optionally computes POSS–solvent partition coefficients (log P)
   - Designed for exploratory and interpretive thermodynamic analysis

3. **`scripts/extract_SMD.sh` — Extraction of SMD results from Gaussian 16 outputs**
   - Scans all Gaussian 16 output files (`*.out`) in the current directory
   - Extracts SMD solvation free-energy components, including:
     - ΔG<sub>solv</sub>
     - electrostatic and non-electrostatic contributions
     - cavity surface area and cavity volume
   - Writes both human-readable (`output.txt`) and machine-readable (`output.csv`) summaries
   - Intended for preprocessing and validation of quantum-chemistry reference data

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
```bash
pip install pandas openpyxl
```

## Usage

### Step 0: Download required input data
Download all solvent-specific `_result.csv` files from the Google Drive link provided above and place them in the same directory as `scripts/aggregate.py`.

### Step 1: Aggregate POSS component quantities
```bash
cd scripts
python aggregate.py
```

### Step 2: Query the dataset interactively
```bash
python extract.py
```

### Optional: Reproduce Fig. 6 parity plot (validation)
Reproducing Fig. 6 requires the user to construct a `parity.csv` file manually.
This file is **not provided** in the repository because it depends on user-generated quantum chemistry results.

The required `parity.csv` must contain **two columns**:
- `SMD`  
  Solvation free energies (ΔG<sub>solv</sub>) calculated using **Gaussian 16**
  with the SMD implicit solvent model. In the associated publication, SMD values were obtained using the keyword:
  #p m062x/6-31g(d) scrf=(smd,solvent=acetone, read, externaliteration,dovacuum) geom=connectivity
- `Model`  
  Predicted ΔG<sub>solv</sub> values obtained from the fragment-based model, extracted using `scripts/extract.py`. Once `parity.csv` has been prepared and placed in the `scripts/` directory, the parity plot can be generated using:

```bash
cd scripts
python plot_fig6_parity.py
```

### Optional: Extract SMD reference data from Gaussian 16 outputs

For users who perform their own Gaussian 16 calculations with the SMD implicit
solvent model, the repository provides a shell script to extract solvation
free-energy components directly from Gaussian output files.

To use this script:

```bash
cd scripts
chmod +x extract_SMD.sh
./extract_SMD.sh
```

> [!NOTE]
> - ΔG values are computed using an additive descriptor model (ΣEs + ΣNes).
> - An empirical scaling factor (recommended value: **0.75**) can be applied to electrostatic energy contributions based on experimental validation reported in the associated publication.
> - This code does not perform molecular dynamics or quantum chemistry calculations.
> - Solvent-specific `_result.csv` files must be downloaded separately before running `aggregate.py`.

## Citation
If this work is helpful for your research, please cite [Interaction mechanisms of POSS-based adsorbents with VOCs, CO2, CH4, and H2O: Theoretical insights and prediction method
](https://doi.org/10.1016/j.gce.2024.10.009).


### Generation of solvent-specific `_result.csv` files (background)
The solvent-specific result files (`*_result.csv`) used by `scripts/aggregate.py` were generated in a **separate preprocessing step** that is **not included in this repository**. These files were produced using an internal Python workflow together with an Excel file, which contains **SMD-calculated interaction energy descriptors** for individual POSS substituents and cage structures in
**eight different solvents**. The generation process follows the conceptual steps below:
1. **Quantum-chemistry-derived descriptor input**  
   `.xlsx` contains pre-tabulated electrostatic (Es) and non-electrostatic
   (Nes) interaction energy contributions for:
   - individual POSS substituents
   - POSS cage structures (T8, T10, T12)
   across multiple solvents, obtained from SMD calculations.
2. **Combinatorial enumeration of POSS structures**  
   For each POSS cage type (T8, T10, T12), all possible substituent combinations
   with repetition were enumerated to generate a large library of POSS
   cage–substituent compositions.
3. **Additive free-energy estimation**  
   For each POSS composition and solvent, the solvation free energy (ΔG) was
   estimated using an additive descriptor model:

   ΔG = ΣEs + ΣNes

   where the summations run over the cage and all substituents in the POSS
   structure.

5. **Per-solvent result export**  
   For each solvent, the computed POSS compositions and their corresponding energetic descriptors were written to a separate CSV file in the format: `<solvent>_result.csv` Each file contains: the full list of POSS components, the estimated ΔG value, the summed electrostatic contribution (SumEsValues), and the summed non-electrostatic contribution (SumNesValues). Due to the **large size of the combinatorial dataset** and the dependence on quantum-chemistry-derived input data, the generation script and raw descriptor Excel file are **not distributed in this repository**. Instead, the resulting `*_result.csv` files are provided separately for downstream aggregation, analysis, and validation.


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

