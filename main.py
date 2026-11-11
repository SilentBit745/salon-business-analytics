
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("historical_did_weekly.csv")

metrics = [
    "retention_rate",
    "revenue_per_visit",
    "no_show_rate"
]

for metric in metrics:

    weekly_data = df.groupby(
        ["week", "group"]
    )[metric].mean().unstack()

    weekly_data.plot(
        marker="o",
        title="Parallel Trends Check: " + metric
    )

    plt.axvline(
        x=13.5,
        linestyle="--",
        label="Intervention"
    )

    plt.xlabel("Week")
    plt.ylabel(metric)
    plt.legend()
    plt.tight_layout()

    filename = metric + "_trend.png"
    plt.savefig(filename)
    plt.show()

print("PARALLEL TRENDS GRAPHS SAVED!")
