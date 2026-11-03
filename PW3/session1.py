import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats



# Load Heart_disease_cleveland_new.csv into a DataFrame
df = pd.read_csv("Heart_disease_cleveland_new.csv")

# Print its shape and first rows
print(f"Shape: {df.shape}")
print(df.head())

# Isolate the four continuous columns
continuous_cols = ["age", "chol", "trestbps", "thalach"]
df_continuous = df[continuous_cols]



# Create a figure with 4 panels
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot a histogram for each continuous variable
for ax, col in zip(axes.flatten(), continuous_cols):
    ax.hist(df_continuous[col].dropna(), bins=20, edgecolor='black')
    ax.set_title(f"Distribution of {col}")

plt.tight_layout()
plt.show()


print("\nShapiro-Wilk Normality Test:")
for col in continuous_cols:
    stat, p = stats.shapiro(df_continuous[col].dropna())
    is_normal = "Approximately Normal" if p > 0.05 else "Not Normal"
    print(f"{col}: p-value = {p:.4g} ({is_normal})")