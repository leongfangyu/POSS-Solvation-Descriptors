import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import matplotlib as mpl

mpl.rcParams['font.family'] = 'Arial'

"""
plot_fig6_parity.py

Reproduces the parity plot shown in Figure 6 of:

"Interaction mechanisms of POSS-based adsorbents with VOCs, CO2, CH4, and H2O:
Theoretical insights and prediction method"

This script compares SMD-derived ΔG_solv values against fragment-based
predicted ΔG_solv values for unstudied POSS variants.
"""

# CSV file containing SMD reference and model-predicted ΔG_solv values
data = pd.read_csv('parity.csv')

# Extract SMD and Model columns
smd_values = data['SMD']
model_values = data['Model']

# Calculate mean absolute error
mean_error = (model_values - smd_values).abs().mean()

# Calculate R-squared (R2) value
slope, intercept, r_value, p_value, std_err = linregress(smd_values, model_values)
r_squared = r_value ** 2

# Plot the parity plot
plt.figure(figsize=(8, 8))

plt.scatter(
    smd_values, smd_values,
    color='lime', edgecolors='darkgreen',
    alpha=0.7, s=120, marker='*',
    label='SMD-determined $\Delta G_{\mathrm{solv}}$'
)

plt.scatter(
    smd_values, model_values,
    color='magenta', edgecolors='rebeccapurple',
    s=40, alpha=0.7, marker='o',
    label='Predicted $\Delta G_{\mathrm{solv}}$'
)

plt.plot(
    smd_values, smd_values,
    color='black', alpha=0.6, linestyle='--',
    label='Parity line'
)

plt.xlabel(
    'SMD-determined $\Delta G_{\mathrm{solv}}$ (kcal mol$^{-1}$)',
    fontsize=14
)
plt.ylabel(
    'Predicted $\Delta G_{\mathrm{solv}}$ (kcal mol$^{-1}$)',
    fontsize=14
)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.grid(True)

# Clean legend: only real plotted artists
legend = plt.legend(loc='best', fontsize=14)
for text in legend.get_texts():
    text.set_fontfamily('Arial')

# Text annotations (not part of legend)
plt.text(
    0.05, 0.75, 'N = 160',
    transform=plt.gca().transAxes,
    fontsize=14, fontfamily='Arial'
)
plt.text(
    0.05, 0.72, f'MAE: {mean_error:.2f} kcal mol$^{{-1}}$',
    transform=plt.gca().transAxes,
    fontsize=14, fontfamily='Arial'
)
plt.text(
    0.05, 0.69, f'R$^2$: {r_squared:.2f}',
    transform=plt.gca().transAxes,
    fontsize=14, fontfamily='Arial'
)

plt.tight_layout()
plt.savefig('parity_plot_high_res.png', dpi=2000)
plt.close()
