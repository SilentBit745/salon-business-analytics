SALON EXPERIMENT & CAUSAL ANALYSIS — SIMULATED DATASET PACK

IMPORTANT
All files in this pack are synthetic/simulated data created for learning and project practice.
They are NOT actual YuvaIntern records, not actual customer data, and not evidence about a real salon.
Clearly label all reports, charts and conclusions as based on simulated data.

FILES
1. appointments_raw.csv
   300,300 rows (300,000 generated records + 300 intentionally duplicated rows).
   Appointment, outlet, client, stylist, service, status, price and no-show fields.
   Walk-ins intentionally have blank client_id values. Some stylist_id values are missing.
   Service names vary; service_category is the standardized category for analysis.
   No-shows are represented within cancelled appointments using cancellation_reason='no_show' and no_show_flag=1.

2. product_sales.csv
   120,000 product sale rows linked to appointment IDs, with product, quantity and sales fields.

3. outlets.csv
   22 fictional outlets. 11 treatment outlets and 11 control outlets for the historical DiD exercise.

4. stylists.csv
   110 fictional stylists linked to outlets.

5. ab_experiment.csv
   24,000 client-level rows from a simulated randomized experiment, with exactly balanced treatment/control assignment overall.
   Primary outcome suggestion: retained_30d.
   Guardrails: revenue_per_visit and no_show_rate.
   Baseline variables: membership_flag, age, prior_90d_visits, baseline_90d_spend.

6. historical_did_weekly.csv
   Weekly outlet-level data for 26 weeks: 13 pre-intervention and 13 post-intervention weeks.
   Treatment outlets receive a simulated change from week 14; control outlets do not.
   Outcomes: retention_rate, revenue_per_visit, no_show_rate.
   Use pre-period trends to discuss the parallel-trends assumption.

SUGGESTED FIRST STEPS
- Load appointments_raw.csv with pandas.
- Check shape, missing values and duplicates.
- Do not delete walk-ins just because client_id is blank.
- Remove exact duplicate appointment rows using appointment_id or duplicated-row checks.
- Standardize service names using service_category.
- Join product_sales.csv to appointments_raw.csv using appointment_id when needed.
- For A/B analysis, check group counts and baseline balance before estimating effects.
- For DiD, plot pre-period trends for treatment and control groups before estimating the post-period effect.

DATA LIMITATIONS
The experiment and historical data are simulated separately for teaching. They are not guaranteed to describe the same clients or exact intervention. Do not combine them as if they were one real operational dataset.
