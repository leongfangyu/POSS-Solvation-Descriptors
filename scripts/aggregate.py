import os
import csv

# =========================
# User input: scaling
# =========================
use_scaling = input("Do you want to scale Electrostatic Energy (SumEsValues)? (yes/no): ").strip().lower()

if use_scaling == "yes":
    try:
        scale_factor = float(input("Enter scaling factor for SumEsValues (e.g. 0.75): ").strip())
    except ValueError:
        raise ValueError("Scaling factor must be a numeric value.")
else:
    scale_factor = 1.0

# Create a list to store the final rows
final_rows = []

# Iterate through the result files
for file_name in os.listdir('.'):
    if file_name.endswith('_result.csv'):
        solvent = file_name.replace('_result.csv', '')
        with open(file_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header

            for row in reader:
                components = eval(row[0])          # Convert string to list
                deltaG = float(row[1])
                SumEsValues = float(row[2]) * scale_factor
                SumNesValues = float(row[3])

                # Create a dictionary for the current row
                row_data = {
                    'solvent': solvent,
                    'T8': 0, 'T10': 0, 'T12': 0,
                    'Methyl': 0, 'Isobutyl': 0, 'Isooctyl': 0, 'Phenyl': 0,
                    'Methacryloxypropyl': 0, 'Trifluoropropyl': 0,
                    'Acryloxypropyl': 0, 'Dimethylsilane': 0,
                    'Glycidyloxypropyl': 0, 'Phenylaminopropyl': 0,
                    'Aminopropyl': 0, 'Epoxycyclohexylethyl': 0,
                    'DeltaG': deltaG,
                    'SumEsValues': SumEsValues,
                    'SumNesValues': SumNesValues
                }

                # Count the occurrences of each component
                for component in components:
                    row_data[component] += 1

                final_rows.append(row_data)

# =========================
# Output file
# =========================
output_file = f"component_quantities{scale_factor}.csv"

with open(output_file, 'w', newline='') as csvfile:
    fieldnames = [
        'solvent', 'T8', 'T10', 'T12',
        'Methyl', 'Isobutyl', 'Isooctyl', 'Phenyl',
        'Methacryloxypropyl', 'Trifluoropropyl',
        'Acryloxypropyl', 'Dimethylsilane',
        'Glycidyloxypropyl', 'Phenylaminopropyl',
        'Aminopropyl', 'Epoxycyclohexylethyl',
        'DeltaG', 'SumEsValues', 'SumNesValues'
    ]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(final_rows)

print(f"Data aggregation completed. Results saved to {output_file}.")
