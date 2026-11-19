
import pandas as pd
from scipy.stats import chisquare

# Load experiment data
df = pd.read_csv("ab_experiment.csv")

# Count customers in each group
counts = df["assigned_group"].value_counts()

control = counts.get("Control", 0)
treatment = counts.get("Treatment", 0)

# Expected group sizes (50:50)
total = control + treatment
expected = [total / 2, total / 2]

# Perform SRM test
chi_stat, p_value = chisquare(
    [control, treatment],
    f_exp=expected
)

print("Sample Ratio Mismatch Test")
print("--------------------------")
print("Control:", control)
print("Treatment:", treatment)
print("Chi-square:", chi_stat)
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: SRM detected. Group sizes are not balanced.")
else:
    print("Result: No SRM detected. Group sizes are balanced.")
