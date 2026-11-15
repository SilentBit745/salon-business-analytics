
import pandas as pd
import statsmodels.formula.api as smf

# Load dataset
df = pd.read_csv("historical_did_weekly.csv")

# Keep only pre-intervention weeks
pre = df[df["period"] == "Pre"].copy()

# Create treatment indicator
pre["is_treatment"] = (pre["group"] == "Treatment").astype(int)

# Treatment-specific time trend
pre["treatment_trend"] = pre["is_treatment"] * pre["week"]

# Outcomes to test
outcomes = [
    "retention_rate",
    "revenue_per_visit",
    "no_show_rate"
]

print("\nPARALLEL TRENDS PRE-TEST")
print("=" * 50)

for outcome in outcomes:

    formula = (
        f"{outcome} ~ C(outlet_id) + C(week) + treatment_trend"
    )

    model = smf.ols(formula, data=pre).fit(
        cov_type="cluster",
        cov_kwds={"groups": pre["outlet_id"]}
    )

    coefficient = model.params["treatment_trend"]
    p_value = model.pvalues["treatment_trend"]
    ci = model.conf_int().loc["treatment_trend"]

    print(f"\nOutcome: {outcome}")
    print(f"Trend difference: {coefficient:.6f}")
    print(f"95% Confidence Interval: {ci[0]:.6f} to {ci[1]:.6f}")
    print(f"P-value: {p_value:.4f}")

    if p_value < 0.05:
        print("Result: Evidence of different pre-intervention trends")
    else:
        print("Result: No statistically significant trend difference")

print("\nPre-trend test completed.")