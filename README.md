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
- Noise Observation: The acceleration is extremely noisy because taking two derivatives  magnifies the small measurement errors present in the original position data
- Integration Result:By integrating the  acceleration  back to position, I recovered  original position with a max difference of only 0.78 m