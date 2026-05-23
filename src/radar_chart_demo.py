import numpy as np
import matplotlib.pyplot as plt

# Expected / hypothetical simulation outcome
# Scale: 1 to 5 Big Five trait averages
traits = ["Openness", "Conscientiousness", "Extraversion", "Agreeableness", "Neuroticism"]

# Applicant pool: broader, more balanced personality distribution
applicant_pool = [3.4, 3.3, 3.1, 3.2, 2.9]

# Hired workforce after repeated scoring that favors "culture fit" / conventional success profile
# This intentionally shows narrowing toward preferred traits, not final measured results.
hired_workforce = [2.9, 4.3, 3.8, 3.6, 2.2]

# Close the radar loop
angles = np.linspace(0, 2 * np.pi, len(traits), endpoint=False).tolist()
applicant_values = applicant_pool + applicant_pool[:1]
hired_values = hired_workforce + hired_workforce[:1]
angles += angles[:1]

fig = plt.figure(figsize=(8, 8))
ax = plt.subplot(111, polar=True)

# Plot lines and filled areas
ax.plot(angles, applicant_values, linewidth=2, label="Applicant Pool")
ax.fill(angles, applicant_values, alpha=0.18)

ax.plot(angles, hired_values, linewidth=2, label="Hired Workforce After Simulation")
ax.fill(angles, hired_values, alpha=0.18)

# Labels and scale
ax.set_xticks(angles[:-1])
ax.set_xticklabels(traits, fontsize=11)
ax.set_ylim(1, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=9)

# Title and annotation
plt.title(
    "Expected Simulation Outcome: Trait-Weighted Hiring Narrows Workforce Profile",
    fontsize=14,
    pad=25
)

ax.legend(loc="upper right", bbox_to_anchor=(1.28, 1.12))

# Add small caption
fig.text(
    0.5, 0.04,
    "Hypothetical visualization: repeated scoring around preferred traits may reduce variation and create a narrower workforce profile.",
    ha="center",
    fontsize=10
)

output_path = "/mnt/data/expected_simulation_radar_chart.png"
plt.tight_layout(rect=[0, 0.07, 1, 1])
plt.savefig(output_path, dpi=200, bbox_inches="tight")
plt.show()

output_path
