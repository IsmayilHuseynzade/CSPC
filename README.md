# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW/Lab /.

## Setup
Create the environment for a given lab:
conda env create -f PW/Lab\ /environment.yml
conda activate cspc

---

## PW1 - Lab A: Reproducible Foundations

What I built:

Speed comparison (loop vs NumPy):
 loop : 1.8410 s
 numpy : 0.0002 s
 speed-up: 11813.5 x faster




**Tests:** all passing? (yes / no)
yes

**Conclusion:**
Today i learned how to work with conda and how to use using git command like
push,branch,add.Also i wrote test using pytest and saw how much numpy is faster

## PW1 - Lab B: Data, Plotting, and Automation

Report:
 - Data Observation: The scatter plot of observerd data matches with the analytical decay law
 - Automation: I built snakemake file automates plotting process and rebuilds the figure only when the input data or script changes



## PW2 - Lab A: Motion from Tracking Data
Report:
- Mean Acceleration: I got -8.58 m/s²
- Noise Observation: The acceleration is extremely noisy because taking two derivatives    small  errors present in the original position data
- Integration Result:By integrating the  acceleration  back to position, I recovered  original position with a max difference of only 0.78 m

## PW2 - Lab B

 # Part 2: Three routes to a minimum
 - do the methods agree?:All methods found the minimum for f(x),but not for g(x). in g(x) success depended on algorithm and starting point
 - Did Newton land on a minimum or another stationary point?:
 when starting from  x=0 on g(x)  newton found a local maximum instead of a minimum
 - how did the starting point change the result?:Changing the starting point changed where the algorithms ended up. in hard function

# Part 5: Titration equivalence point
- by calculating the maximum slope  of the titration curve using `np.gradient`,  equivalence point was found to be at  50 mL


## PW3

# Session 1: Characterising the Data

1. Load the data with pandas
i loaded succesfully using pandas

2. The shape of each variable



age: The distribution is nearly symmetric and bell-shaped, peaking around the late 50s.

cholestorol:  distribution is left-skewed. the majority of patients are clustered in a normal to high range

Resting Blood Pressure: shows  slight right skew. most values are clustered around 120-140 , but  few patients has much higher

Thalach:   distribution left-skewed. 

3. Are they normally distributed?

Verdict: None of the four continuous variables (age, chol, trestbps, thalach) are normally distributed.

Reasoning: Visual inspection of the histograms reveals that chol, trestbps, and thalach are heavily skewed, while age has multiple peaks rather than a perfect bell curve. This visual evidence is confirmed numerically by the Shapiro-Wilk test, which returned a p-value < 0.05 for all four variables, indicating a statistically significant departure from normality.

## Session 2 Findings

Task 4 (Heart Rate): Used the Mann-Whitney U test due to non-normal data. Heart disease patients have a significantly lower max heart rate (Healthy mean: [Mean]±[SE], Disease mean: [Mean]±[SE], p=[p-val]).

Task 5 (Age Correlation): Used Spearman correlation. Age and max heart rate are negatively correlated; as age increases, max heart rate decreases (r=[r-val], p=[p-val]).

Tasks 6 & 7 (Chemical Mystery): Naively, [Chemical 1] seemed like the cause. However, after controlling for pollution_index (filtering for 40-60), [Chemical 2] is the actual cause. Its correlation remained strong at [r-val], while [Chemical 1] dropped to [r-val], showing it was just a confounding variable.