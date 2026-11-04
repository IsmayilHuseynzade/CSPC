import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load datasets
df_heart = pd.read_csv("Heart_disease_cleveland_new.csv")
df_chem = pd.read_csv("chemicals_cancer.csv")

# ==========================================
# Task 4: Is the effect real?
# ==========================================
# Split thalach by target group
thalach_disease = df_heart[df_heart['target'] == 1]['thalach'].dropna()
thalach_healthy = df_heart[df_heart['target'] == 0]['thalach'].dropna()

# Mann-Whitney U test (used because data is not normally distributed)
stat_mw, p_val_mw = stats.mannwhitneyu(thalach_disease, thalach_healthy)
print(f"Task 4 - Mann-Whitney U p-value: {p_val_mw:.4g}")

# Calculate means and standard errors
mean_d, se_d = thalach_disease.mean(), thalach_disease.sem()
mean_h, se_h = thalach_healthy.mean(), thalach_healthy.sem()
print(f"Task 4 - Disease Mean: {mean_d:.2f} ± {se_d:.2f}")
print(f"Task 4 - Healthy Mean: {mean_h:.2f} ± {se_h:.2f}")

# Plot means with uncertainty
plt.figure(figsize=(6, 5))
plt.bar(['Disease (1)', 'Healthy (0)'], [mean_d, mean_h], 
        yerr=[se_d, se_h], capsize=10, color=['salmon', 'lightblue'], edgecolor='black')
plt.title('Mean Max Heart Rate (thalach) by Group')
plt.ylabel('Mean thalach')
plt.show()

# ==========================================
# Task 5: Do two things move together?
# ==========================================
# Spearman correlation (used because variables are not normal)
corr_spearman, p_val_sp = stats.spearmanr(df_heart['age'].dropna(), df_heart['thalach'].dropna())
print(f"\nTask 5 - Age vs Thalach Spearman Correlation: {corr_spearman:.4f} (p-value: {p_val_sp:.4g})")

# Plot age vs thalach
plt.figure(figsize=(6, 5))
plt.scatter(df_heart['age'], df_heart['thalach'], alpha=0.6, edgecolor='black')
plt.title('Age vs Maximum Heart Rate (thalach)')
plt.xlabel('Age')
plt.ylabel('Max Heart Rate (thalach)')
plt.show()

# ==========================================
# Task 6: The naive analysis
# ==========================================
# Quantify associations using Pearson correlation
benzene_corr = df_chem['benzene'].corr(df_chem['malignancy'])
cadmium_corr = df_chem['cadmium'].corr(df_chem['malignancy'])
print(f"\nTask 6 - Naive Correlation -> Benzene: {benzene_corr:.4f}, Cadmium: {cadmium_corr:.4f}")

# ==========================================
# Task 7: Look again
# ==========================================
# Filter to account for the confounding variable (pollution_index)
df_chem_filtered = df_chem[(df_chem['pollution_index'] > 40) & (df_chem['pollution_index'] < 60)]

# Recompute associations
benzene_corr_adj = df_chem_filtered['benzene'].corr(df_chem_filtered['malignancy'])
cadmium_corr_adj = df_chem_filtered['cadmium'].corr(df_chem_filtered['malignancy'])
print(f"Task 7 - Adjusted Correlation -> Benzene: {benzene_corr_adj:.4f}, Cadmium: {cadmium_corr_adj:.4f}")