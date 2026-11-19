
# Salon Business Analytics

## About the Project

Salon Business Analytics is a Python project that studies salon business data.

It helps us understand how a salon is performing, what customers like, how much revenue different services generate, and how customer retention can improve.

All datasets used in this project are simulated (not real salon records).

## What Is This Project For?

This project helps to:

- Understand salon business performance.
- Find popular salon services.
- Analyse customer visits and retention.
- Study revenue and no-show rates.
- Compare two groups using A/B testing.
- Measure the effect of a business change using DiD analysis.
- Make better business decisions using data.

## How Does It Work?

The project follows these steps:

1. **Load Data:** Read salon data from CSV files.
2. **Clean Data:** Remove duplicate records and check missing values.
3. **Analyse Data:** Study appointments, customers and revenue.
4. **Create Graphs:** Show important results using charts.
5. **A/B Testing:** Compare Control and Treatment groups.
6. **DiD Analysis:** Compare business results before and after an intervention.
7. **Findings:** Understand results and suggest improvements.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Statsmodels

## Main Project Files

| File | Purpose |
|---|---|
| `main.py` | Main analysis and graphs |
| `pretrend_test.py` | Checks pre intervention trends |
| `did_estimation.py` | Calculates DiD results |
| `appointments_raw.csv` | Original appointment data |
| `appointments_cleaned.csv` | Cleaned appointment data |
| `ab_experiment.csv` | A/B testing data |
| `historical_did_weekly.csv` | Weekly data for DiD analysis |
| `outlets.csv` | Salon outlet details |
| `stylists.csv` | Stylist details |
| `product_sales.csv` | Product sales data |

## Key Analysis

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Customer Retention
- Revenue Analysis
- Data Visualisation
- A/B Testing
- Difference-in-Differences (DiD)

## How to Run the Project

### 1. Install Python Libraries

```bash
pip install pandas numpy matplotlib scipy statsmodels
```

### 2. Run the Main Analysis

```bash
python main.py
```

### 3. Run the Pre-Trend Test

```bash
python pretrend_test.py
```

### 4. Run DiD Analysis

```bash
python did_estimation.py
```

## Project Results

The simulated analysis showed:

- Facial was the highest revenue generating service.
- Returning customers made up 85.85% of identifiable customers with completed appointments.
- The A/B experiment showed improved retention and revenue in the Treatment group.
- The DiD analysis showed positive changes in retention and revenue, and a reduction in no show rates.

These are results from simulated data, not actual salon business performance.

## Project Limitations

- The datasets are simulated.
- A/B testing and DiD use separate datasets.
- Results may differ in a real salon business.
- Statistical results need careful interpretation.
