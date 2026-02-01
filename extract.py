import csv

# Read the component_quantities.csv and store the data in a list of dictionaries
data = []
with open('scaled.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)

# Initialize the solvents list
solvents = list(set(row['solvent'] for row in data))

# Get user input for requiring a partition coefficient
require_partition = input("Require Partition Coefficient? (y/n): ")

if require_partition.lower() == 'n':
    # Get the unique solvent names
    print("\nSelect a solvent:")
    print("0. All solvents")
    for idx, solvent in enumerate(solvents, start=1):
        print(f"{idx}. {solvent}")
    selected_solvent_idx = int(input("Enter the index of the solvent: "))
    if selected_solvent_idx == 0:
        selected_solvent = "all"
    else:
        selected_solvent = solvents[selected_solvent_idx - 1]

    # Get user input for cage size selection
    cage_sizes = ['T8', 'T10', 'T12']
    print("\nSelect a cage size:")
    for idx, cage_size in enumerate(cage_sizes, start=1):
        print(f"{idx}. {cage_size}")
    selected_cage_size_idx = int(input("Enter the index of the cage size: ")) - 1
    selected_cage_size = cage_sizes[selected_cage_size_idx]

    # Generate the cage size values based on the user's selection
    cage_size_values = ['0', '0', '0']
    cage_size_values[selected_cage_size_idx] = '1'

    # Get user input for substituent types and quantities
    substituents = ['Methyl', 'Isobutyl', 'Isooctyl', 'Phenyl', 'Methacryloxypropyl', 'Trifluoropropyl', 'Acryloxypropyl', 'Dimethylsilane', 'Glycidyloxypropyl', 'Phenylaminopropyl', 'Aminopropyl', 'Epoxycyclohexylethyl']

    input_matrix = [0] * (1 + len(cage_size_values) + len(substituents))

    # Set the selected solvent, cage size values, and substituent quantities
    input_matrix[0] = selected_solvent
    for idx, value in enumerate(cage_size_values, start=1):
        input_matrix[idx] = value

    print("\nEnter the quantity for each substituent (type 'done' when finished):")
    for idx, substituent in enumerate(substituents, start=1 + len(cage_size_values)):
        quantity = input(f"Enter the quantity for {substituent}: ")
        if quantity.lower() == 'done':
            break
        input_matrix[idx] = quantity

    # Convert the input matrix to a list of strings for comparison
    input_matrix_str = [str(item) if isinstance(item, (int, float)) else item for item in input_matrix]

    # Find the corresponding row in data
    matching_rows = []
    for row in data:
        row_values = [row['solvent']] + cage_size_values + [row[substituent] for substituent in substituents]
        if selected_solvent == "all" or input_matrix_str == row_values:
            matching_rows.append(row)

    # Output the corresponding ΔG value with the addition of 1.89
    for matching_row in matching_rows:
        deltaG = float(matching_row['DeltaG']) + 1.89  # Add 1.89
        SumEsValues = float(matching_row['SumEsValues'])
        SumNesValues = float(matching_row['SumNesValues'])
        print(f"\nΔG value in {matching_row['solvent']}: {deltaG} kcal/mol with correction factor of 1.89 kcal/mol. The ΔG<sub>es</sub> is {SumEsValues} kcal/mol and the G<sub>CDS</sub>  is {SumNesValues}.")

elif require_partition.lower() == 'y':
    # Get user input for two solvents
    print("\nSelect two solvents:")
    for idx, solvent in enumerate(solvents, start=1):
        print(f"{idx}. {solvent}")
    selected_solvent1_idx = int(input("Enter the index of the first solvent: ")) - 1
    selected_solvent2_idx = int(input("Enter the index of the second solvent: ")) - 1
    selected_solvent1 = solvents[selected_solvent1_idx]
    selected_solvent2 = solvents[selected_solvent2_idx]

    # Get user input for cage size selection
    cage_sizes = ['T8', 'T10', 'T12']
    print("\nSelect a cage size:")
    for idx, cage_size in enumerate(cage_sizes, start=1):
        print(f"{idx}. {cage_size}")
    selected_cage_size_idx = int(input("Enter the index of the cage size: ")) - 1
    selected_cage_size = cage_sizes[selected_cage_size_idx]

    # Generate the cage size values based on user's selection
    cage_size_values = ['0', '0', '0']
    cage_size_values[selected_cage_size_idx] = '1'

    # Get user input for substituent types and quantities (assumes same quantities for both solvents)
    substituents = ['Methyl', 'Isobutyl', 'Isooctyl', 'Phenyl', 'Methacryloxypropyl', 'Trifluoropropyl', 'Acryloxypropyl', 'Dimethylsilane', 'Glycidyloxypropyl', 'Phenylaminopropyl', 'Aminopropyl', 'Epoxycyclohexylethyl']

    input_quantities = {}
    print("\nEnter the quantity for each substituent (type 'done' when finished):")
    for substituent in substituents:
        quantity = input(f"Enter the quantity for {substituent}: ")
        if quantity.lower() == 'done':
            break
        input_quantities[substituent] = quantity

    # Initialize the matrices with zeros
    input_matrix1 = [0] * (1 + len(cage_size_values) + len(substituents))
    input_matrix2 = [0] * (1 + len(cage_size_values) + len(substituents))

    # Set the selected solvents, cage size values, and substituent quantities for each matrix
    input_matrix1[0] = selected_solvent1
    for idx, value in enumerate(cage_size_values, start=1):
        input_matrix1[idx] = value
    for idx, substituent in enumerate(substituents, start=1 + len(cage_size_values)):
        input_matrix1[idx] = input_quantities.get(substituent, '0')

    input_matrix2[0] = selected_solvent2
    for idx, value in enumerate(cage_size_values, start=1):
        input_matrix2[idx] = value
    for idx, substituent in enumerate(substituents, start=1 + len(cage_size_values)):
        input_matrix2[idx] = input_quantities.get(substituent, '0')

    # Convert input matrices to lists of strings for comparison
    input_matrix_str1 = [str(item) if isinstance(item, (int, float)) else item for item in input_matrix1]
    input_matrix_str2 = [str(item) if isinstance(item, (int, float)) else item for item in input_matrix2]

    # Find the corresponding rows in data for each solvent
    matching_rows1 = []
    matching_rows2 = []
    for row in data:
        row_values = [row['solvent']] + cage_size_values + [row[substituent] for substituent in substituents]

        if input_matrix_str1 == row_values:
            matching_rows1.append(row)

        if input_matrix_str2 == row_values:
            matching_rows2.append(row)

    # Output the corresponding ΔG values for each solvent
    if matching_rows1:
        deltaG1 = float(matching_rows1[0]['DeltaG']) + 1.89
        print(f"\nΔG value in {selected_solvent1}: {deltaG1} kcal/mol")
    else:
        print("No matching data found for the first selected solvent inputs.")

    if matching_rows2:
        deltaG2 = float(matching_rows2[0]['DeltaG']) + 1.89
        print(f"\nΔG value in {selected_solvent2}: {deltaG2} kcal/mol")
    else:
        print("No matching data found for the second selected solvent inputs.")

    # Calculate LogP1 and LogP2 values
    deltaG1 = float(matching_rows1[0]['DeltaG']) if matching_rows1 else 0
    deltaG2 = float(matching_rows2[0]['DeltaG']) if matching_rows2 else 0

    # Constants
    R = 0.001987  # kcal/(mol*K)
    T = 298.15  # K

    # Calculate LogP values
    LogP1 = -((deltaG1 - deltaG2)) / (2.303 * R * T)
    LogP2 = -((deltaG2 - deltaG1))/ (2.303 * R * T)

    # Display LogP values with corresponding solvent names
    solvent1_name = matching_rows1[0]['solvent'] if matching_rows1 else ''
    solvent2_name = matching_rows2[0]['solvent'] if matching_rows2 else ''

    print(f"LogP({solvent1_name}-{solvent2_name}): {LogP1}")
    print(f"LogP({solvent2_name}-{solvent1_name}): {LogP2}")

else:
    print("Invalid input. Please choose either 'y' or 'n' for requiring a partition coefficient.")
