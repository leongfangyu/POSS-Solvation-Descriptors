#!/usr/bin/env bash
#
# extract_smd_values.sh
#
# Extracts SMD solvation free-energy components from Gaussian 16 .out files.
#
# Expected input:
#   - Gaussian 16 output files with extension ".out"
#   - SMD solvation model enabled (SCRF=SMD)
#
# Output:
#   - output.txt : human-readable tab-delimited summary
#   - output.csv : machine-readable CSV summary
#
# Extracted quantities:
#   - DeltaG (solv)           [kcal/mol]
#   - Electrostatic           [kcal/mol]
#   - Non-electrostatic       [kcal/mol]
#   - Cavity surface area     [Å^2]
#   - Cavity volume           [Å^3]
#

set -u  # Treat unset variables as an error
shopt -s nullglob  # Avoid literal *.out if no files are found

# Output file names
OUTPUT_TXT="output.txt"
OUTPUT_CSV="output.csv"

# Remove existing output files
rm -f "$OUTPUT_TXT" "$OUTPUT_CSV"

# Write headers
printf "Filename\tDeltaG_solv\tElectrostatic\tNon_electrostatic\tCavity_surface_area\tCavity_volume\n" >> "$OUTPUT_TXT"
printf "Filename,DeltaG_solv,Electrostatic,Non_electrostatic,Cavity_surface_area,Cavity_volume\n" >> "$OUTPUT_CSV"

# Collect .out files
out_files=( *.out )

# Check if any .out files exist
if [ ${#out_files[@]} -eq 0 ]; then
    echo "ERROR: No Gaussian .out files found in the current directory."
    exit 1
fi

# Loop over all Gaussian output files
for file in "${out_files[@]}"; do

    # Extract values (first match only)
    electrostatic=$(grep -m 1 "Total electrostatic.*(kcal/mol) =" "$file" | awk '{print $NF}')
    non_electrostatic=$(grep -m 1 "Total non electrostatic.*(kcal/mol) =" "$file" | awk '{print $NF}')
    delta_g=$(grep -m 1 "DeltaG (solv).* (kcal/mol) =" "$file" | awk '{print $NF}')
    surface_area=$(grep -m 1 "GePol: Cavity surface area" "$file" | awk '{print $(NF-1)}')
    cavity_volume=$(grep -m 1 "GePol: Cavity volume" "$file" | awk '{print $(NF-1)}')

    # Replace missing values with NA
    electrostatic=${electrostatic:-NA}
    non_electrostatic=${non_electrostatic:-NA}
    delta_g=${delta_g:-NA}
    surface_area=${surface_area:-NA}
    cavity_volume=${cavity_volume:-NA}

    # Write to output files
    printf "%s\t%s\t%s\t%s\t%s\t%s\n" \
        "$file" "$delta_g" "$electrostatic" "$non_electrostatic" "$surface_area" "$cavity_volume" >> "$OUTPUT_TXT"

    printf "%s,%s,%s,%s,%s,%s\n" \
        "$file" "$delta_g" "$electrostatic" "$non_electrostatic" "$surface_area" "$cavity_volume" >> "$OUTPUT_CSV"

done

# Print summary to screen
cat "$OUTPUT_TXT"
