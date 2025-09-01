# Chapter 2: The Temptation of Speed – Shipping Without Ethics

import matplotlib.pyplot as plt

# Define risks with (likelihood, impact)
risks = {
    "Bias in dataset": (0.8, 0.9),
    "Privacy violation": (0.7, 1.0),
    "System downtime": (0.6, 0.4),
    "Deceptive design": (0.9, 0.7),
    "Rare catastrophic misuse": (0.2, 1.0)
}
# Plot risk points
plt.figure(figsize=(8, 6))
for risk, (likelihood, impact) in risks.items():
    plt.scatter(likelihood, impact, s=100, label=risk)
# Add labels and grid
plt.xlabel("Likelihood (0–1)")
plt.ylabel("Impact (0–1)")
plt.title("AI Ethics Risk Map")
plt.grid(True)
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))
plt.show()
