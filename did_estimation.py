
import pandas as pd
import statsmodels.formula.api as smf

# Load dataset
df = pd.read_csv("historical_did_weekly.csv")

# Create treatment and post-intervention variables
df["treatment"] = (df["group"] == "Treatment").astype(int)
df["post"] = df["post_intervention"].astype(int)

# DiD interaction
df["treatment_post"] = df["treatment"] * df["post"]

# Metrics to analyse
outcomes = [
    "retention_rate",
    "revenue_per_visit",
    "no_show_rate"
]

print("\nDIFFERENCE-IN-DIFFERENCES RESULTS")
print("=" * 55)

for outcome in outcomes:

    formula = (
        f"{outcome} ~ treatment_post + C(outlet_id) + C(week)"
    )

    model = smf.ols(formula, data=df).fit(
        cov_type="cluster",
        cov_kwds={"groups": df["outlet_id"]}
    )

    estimate = model.params["treatment_post"]
    p_value = model.pvalues["treatment_post"]
    ci = model.conf_int().loc["treatment_post"]

    print(f"\nMetric: {outcome}")
    print(f"DiD Estimate: {estimate:.6f}")
    print(f"95% Confidence Interval: {ci[0]:.6f} to {ci[1]:.6f}")
    print(f"P-value: {p_value:.4f}")

    if p_value < 0.05:
        print("Result: Statistically significant treatment effect")
    else:
        print("Result: No statistically significant treatment effect")

print("\nDiD analysis completed.")
