#!/usr/bin/env bash
#
# extractvf.sh
#
# Extract electronic and (when available) thermochemical energy values
# from Gaussian 16 output files (.log, .out) for adsorption-energy analysis.
#
# Supported calculations:
#   - Single-point (SP)
#   - Geometry optimization (Opt)
#   - Frequency or Opt+Freq (thermochemistry)
#
# Output:
#   - adsorption_energy_components.csv
#
# Notes:
#   - Thermochemical quantities are extracted ONLY if frequency results exist.
#   - Optimization-only jobs will contain electronic energies only.
#   - On macOS external drives, run using:
#       bash extractvf.sh
#

set -euo pipefail
shopt -s nullglob

OUTPUT_CSV="adsorption_energy_components.csv"
rm -f "$OUTPUT_CSV"

echo "Filename,SCF_Energy_Hartree,ZeroPoint_Energy_Hartree,Thermal_Energy_Correction,Thermal_Enthalpy_Correction,Thermal_Gibbs_Correction,Electronic+ZPE,Electronic+Thermal_Energy,Electronic+Thermal_Enthalpy,Electronic+Thermal_Free_Energy" \
> "$OUTPUT_CSV"

echo "Scanning Gaussian output files (*.log, *.out)..."
echo

for file in *.out *.log; do
    [[ -f "$file" ]] || continue

    echo "Processing: $file"

    # --- Final SCF energy (LAST occurrence)
    scf_energy=$(grep "SCF Done:" "$file" | tail -n 1 | awk '{print $5}' || true)

    # --- Thermochemistry (only if frequency calculation exists)
    if grep -q "Zero-point correction" "$file"; then
        zpe=$(grep "Zero-point correction" "$file" | tail -n 1 | awk '{print $NF}' || true)
        tc_energy=$(grep "Thermal correction to Energy" "$file" | tail -n 1 | awk '{print $NF}' || true)
        tc_enthalpy=$(grep "Thermal correction to Enthalpy" "$file" | tail -n 1 | awk '{print $NF}' || true)
        tc_gibbs=$(grep "Thermal correction to Gibbs Free Energy" "$file" | tail -n 1 | awk '{print $NF}' || true)
        e_zpe=$(grep "Sum of electronic and zero-point Energies" "$file" | tail -n 1 | awk '{print $NF}' || true)
        e_thermal=$(grep "Sum of electronic and thermal Energies" "$file" | tail -n 1 | awk '{print $NF}' || true)
        e_enthalpy=$(grep "Sum of electronic and thermal Enthalpies" "$file" | tail -n 1 | awk '{print $NF}' || true)
        e_free=$(grep "Sum of electronic and thermal Free Energies" "$file" | tail -n 1 | awk '{print $NF}' || true)
    else
        zpe="NA"
        tc_energy="NA"
        tc_enthalpy="NA"
        tc_gibbs="NA"
        e_zpe="NA"
        e_thermal="NA"
        e_enthalpy="NA"
        e_free="NA"
    fi

    echo "$file,${scf_energy:-NA},$zpe,$tc_energy,$tc_enthalpy,$tc_gibbs,$e_zpe,$e_thermal,$e_enthalpy,$e_free" \
    >> "$OUTPUT_CSV"

done

echo
echo "Extraction complete."
echo "Results written to: $OUTPUT_CSV"
echo
echo "========== CSV CONTENT =========="
cat "$OUTPUT_CSV"
echo "================================="
