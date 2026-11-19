
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv("ab_experiment.csv")

# Create customer groups
df["membership_group"] = df["membership_flag"].map({
    0: "Non-Members",
    1: "Members"
})

df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 29, 44, 100],
    labels=["Below 30", "30-44", "45+"]
)

df["visit_group"] = pd.cut(
    df["prior_90d_visits"],
    bins=[-1, 1, 3, float("inf")],
    labels=["0-1 Visits", "2-3 Visits", "4+ Visits"]
)

# Function to compare retention
def analyse_segment(data, column):

    for name, group in data.groupby(column, observed=True):

        control = group[group["assigned_group"] == "Control"]
        treatment = group[group["assigned_group"] == "Treatment"]

        n1 = len(control)
        n2 = len(treatment)

        if n1 == 0 or n2 == 0:
            continue

        p1 = control["retained_30d"].mean()
        p2 = treatment["retained_30d"].mean()

        difference = p2 - p1

        se = np.sqrt(
            p1 * (1 - p1) / n1 +
            p2 * (1 - p2) / n2
        )

        lower = difference - 1.96 * se
        upper = difference + 1.96 * se

        print("\nSegment:", name)
        print("Control retention:", round(p1 * 100, 2), "%")
        print("Treatment retention:", round(p2 * 100, 2), "%")
        print("Improvement:", round(difference * 100, 2), "percentage points")
        print("95% CI:", round(lower * 100, 2), "to",
              round(upper * 100, 2), "percentage points")


# Analyse all customer groups
print("MEMBERSHIP ANALYSIS")
analyse_segment(df, "membership_group")

print("\nAGE ANALYSIS")
analyse_segment(df, "age_group")

print("\nPREVIOUS VISITS ANALYSIS")
analyse_segment(df, "visit_group")
