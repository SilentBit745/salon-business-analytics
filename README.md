
# Salon Business Analytics

## About the Project

Salon Business Analytics is a Python project that studies salon business data.

It helps us understand customer visits, popular services, revenue, and customer retention.

**Note:** All data used in this project is simulated. It is not real salon data.

## Project Goals

- Study salon business performance.
- Find popular services.
- Understand customer visits and retention.
- Analyse revenue and no show rates.
- Compare groups using A/B testing.
- Study business changes using DiD analysis.
- Make better decisions using data.

## How It Works

1. Load data from CSV files.
2. Clean the data.
3. Study customers, appointments, and revenue.
4. Create graphs.
5. Perform A/B testing.
6. Perform DiD analysis.
7. Understand the results.

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SciPy
- Statsmodels
- Jupyter Notebook

## Main Project Files

| File | Purpose |
|---|---|
| `salon_analysis.ipynb` | Complete analysis notebook |
| `main.py` | Creates DiD trend graphs |
| `pretrend_test.py` | Checks pre intervention trends |
| `did_estimation.py` | Calculates DiD results |
| `srm_test.py` | Checks group sizes |
| `segment_analysis.py` | Studies customer groups |
| `experiment_design.md` | Explains the A/B test plan |
| `decision_memo.md` | Gives business recommendations |
| `appointments_raw.csv` | Original appointment data |
| `appointments_cleaned.csv` | Cleaned appointment data |
| `ab_experiment.csv` | A/B testing data |
| `historical_did_weekly.csv` | Weekly DiD data |

## Main Analysis

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Customer Retention
- Revenue Analysis
- Data Visualisation
- A/B Testing
- Sample Ratio Mismatch (SRM) Test
- Customer Segment Analysis
- Difference-in-Differences (DiD)
- Pre Trend Testing

## How to Run the Project

### 1. Install Libraries

```bash
pip install pandas numpy matplotlib scipy statsmodels
```

### 2. Run the Python Files

```bash
python main.py
python pretrend_test.py
python did_estimation.py
python srm_test.py
python segment_analysis.py
```

### 3. Run the Notebook

Open `salon_analysis.ipynb` in Jupyter Notebook or VS Code and run the cells.

## Key Results

The simulated data showed:

- Facial generated the highest revenue.
- Customer retention was 85.85% among identifiable customers with completed appointments.
- The Treatment group had better retention and revenue in the A/B test.
- The DiD analysis showed positive changes in retention and revenue.
- The DiD analysis also showed a lower no show rate.

These results are based on simulated data, not a real salon business.

## Project Limitations

- The data is simulated.
- A/B testing and DiD use separate datasets.
- Results may be different in a real business.
- Statistical results should be interpreted carefully.
  
